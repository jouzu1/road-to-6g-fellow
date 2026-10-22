"""
Lab 01: Papan Catur Modulasi Digital (BPSK, QPSK, 16-QAM) & Simulasi Kanal AWGN
Track: Level 1 — Modulasi Digital & Kanal Nirkabel
Author: Amelia (Senior Dev) & Dr. Aris (Principal Telecom Architect)
Audited by: Quinn (QA Architect)
Repository: jouzu1/road-to-6g-fellow
"""

import numpy as np
import scipy.special as sp
import os
import sys

# Pastikan output konsol mendukung karakter UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


class ModulationScheme:
    """
    Kelas basis untuk skema modulasi digital dengan pemetaan Gray Coding
    dan normalisasi daya rata-rata simbol (E[|s|^2] = 1).
    """
    def __init__(self, name: str, bits_per_symbol: int, constellation: np.ndarray, bit_labels: np.ndarray):
        self.name = name
        self.k = bits_per_symbol
        self.M = 2 ** self.k
        self.constellation = constellation  # Complex array [M]
        self.bit_labels = bit_labels        # Int array [M, k]

        # Verifikasi normalisasi daya rata-rata simbol (E[|s|^2] = 1.0)
        avg_power = np.mean(np.abs(self.constellation) ** 2)
        assert np.isclose(avg_power, 1.0, atol=1e-5), f"Daya rata-rata {name} tidak ternormalisasi! ({avg_power})"

    def modulate(self, bits: np.ndarray) -> np.ndarray:
        """
        Memetakan array bit biner 1D menjadi array simbol kompleks 1D.
        """
        assert len(bits) % self.k == 0, f"Jumlah bit ({len(bits)}) harus kelipatan {self.k}"
        grouped = bits.reshape(-1, self.k)
        
        # Temukan indeks konstelasi yang cocok dengan pola bit
        # Cara efisien: ubah bit ke integer index
        indices = np.zeros(len(grouped), dtype=int)
        for i, label in enumerate(self.bit_labels):
            match = np.all(grouped == label, axis=1)
            indices[match] = i
            
        return self.constellation[indices]

    def demodulate(self, received: np.ndarray) -> np.ndarray:
        """
        Detektor Maximum Likelihood (Minimum Euclidean Distance Slicer).
        """
        # Hitung jarak Euclidean kuadrat ke semua titik konstelasi: |y - s_m|^2
        distances = np.abs(received[:, np.newaxis] - self.constellation[np.newaxis, :]) ** 2
        detected_indices = np.argmin(distances, axis=1)
        detected_bits = self.bit_labels[detected_indices].flatten()
        return detected_bits


def build_bpsk() -> ModulationScheme:
    """
    BPSK (Binary Phase Shift Keying):
    1 bit per simbol.
    Bit 0 -> +1.0
    Bit 1 -> -1.0
    Normalisasi: 1.0
    """
    constellation = np.array([1.0 + 0.0j, -1.0 + 0.0j], dtype=np.complex128)
    bit_labels = np.array([[0], [1]], dtype=int)
    return ModulationScheme("BPSK", 1, constellation, bit_labels)


def build_qpsk() -> ModulationScheme:
    """
    QPSK (Quadrature Phase Shift Keying) dengan Gray Coding:
    2 bit per simbol.
    00 -> (+1 + 1j) / sqrt(2)
    01 -> (-1 + 1j) / sqrt(2)
    11 -> (-1 - 1j) / sqrt(2)
    10 -> (+1 - 1j) / sqrt(2)
    Normalisasi: 1 / sqrt(2)
    """
    norm = np.sqrt(2.0)
    constellation = np.array([
        ( 1.0 + 1.0j) / norm,  # 00
        (-1.0 + 1.0j) / norm,  # 01
        (-1.0 - 1.0j) / norm,  # 11
        ( 1.0 - 1.0j) / norm   # 10
    ], dtype=np.complex128)
    bit_labels = np.array([
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0]
    ], dtype=int)
    return ModulationScheme("QPSK", 2, constellation, bit_labels)


def build_16qam() -> ModulationScheme:
    """
    16-QAM dengan Gray Coding pada sumbu I dan Q:
    4 bit per simbol.
    Bit [b0, b1] memetakan I: 00 -> -3, 01 -> -1, 11 -> +1, 10 -> +3
    Bit [b2, b3] memetakan Q: 00 -> -3, 01 -> -1, 11 -> +1, 10 -> +3
    Daya rata-rata sebelum normalisasi: (1^2 + 3^2)/2 = 5 per dimensi, total = 10.
    Faktor normalisasi: 1 / sqrt(10)
    """
    norm = np.sqrt(10.0)
    levels = np.array([-3.0, -1.0, 1.0, 3.0])
    gray_bits = np.array([
        [0, 0],  # -3
        [0, 1],  # -1
        [1, 1],  # +1
        [1, 0]   # +3
    ])
    
    constellation = []
    bit_labels = []
    
    for i_idx, i_val in enumerate(levels):
        for q_idx, q_val in enumerate(levels):
            sym = (i_val + 1j * q_val) / norm
            bits = np.concatenate([gray_bits[i_idx], gray_bits[q_idx]])
            constellation.append(sym)
            bit_labels.append(bits)
            
    return ModulationScheme("16-QAM", 4, np.array(constellation, dtype=np.complex128), np.array(bit_labels, dtype=int))


def simulate_awgn(mod_scheme: ModulationScheme, eb_n0_db_range: np.ndarray, num_bits: int = 100000):
    """
    Simulasi transmisi Monte Carlo melintasi kanal AWGN.
    """
    # Pastikan num_bits kelipatan k
    num_bits = (num_bits // mod_scheme.k) * mod_scheme.k
    tx_bits = np.random.randint(0, 2, size=num_bits)
    tx_symbols = mod_scheme.modulate(tx_bits)

    sim_ber = []
    sim_ser = []

    for eb_n0_db in eb_n0_db_range:
        # Konversi Eb/N0 (dB) ke skala linier
        eb_n0_lin = 10.0 ** (eb_n0_db / 10.0)
        # Es/N0 = k * Eb/N0
        es_n0_lin = mod_scheme.k * eb_n0_lin
        
        # Untuk Es = 1 (karena ternormalisasi), N0 = 1 / es_n0_lin
        n0 = 1.0 / es_n0_lin
        # Variansi noise per dimensi kompleks (sigma_I^2 = sigma_Q^2 = N0 / 2)
        noise_sigma = np.sqrt(n0 / 2.0)
        
        # Pembangkitan desah Gaussian Kompleks
        noise = noise_sigma * (np.random.randn(len(tx_symbols)) + 1j * np.random.randn(len(tx_symbols)))
        rx_symbols = tx_symbols + noise
        
        # Demodulasi detektor jarak minimum
        rx_bits = mod_scheme.demodulate(rx_symbols)
        
        # Hitung Bit Error Rate (BER)
        bit_errors = np.sum(tx_bits != rx_bits)
        ber = bit_errors / num_bits
        sim_ber.append(ber)
        
    return np.array(sim_ber)


def q_function(x):
    """Fungsi Q(x) analitis dari Teori Peluang Gaussian."""
    return 0.5 * sp.erfc(x / np.sqrt(2.0))


def main():
    print("=" * 70)
    print("📡 LAB 01: SIMULASI MONTE CARLO MODULASI DIGITAL & KANAL AWGN")
    print("Insinyur: Amelia (💻) | Review: Dr. Aris (📡) & Quinn (🧪)")
    print("=" * 70)
    
    eb_n0_db_range = np.arange(0, 13, 2)  # [0, 2, 4, 6, 8, 10, 12] dB
    num_bits = 200000  # 200 ribu bit per pengujian SNR
    
    schemes = [build_bpsk(), build_qpsk(), build_16qam()]
    results = {}
    
    for scheme in schemes:
        print(f"🚀 Menjalankan simulasi untuk {scheme.name} ({scheme.k} bits/symbol)...")
        results[scheme.name] = simulate_awgn(scheme, eb_n0_db_range, num_bits=num_bits)
        
    # Hitung nilai teoritis untuk BPSK / QPSK: Pb = Q(sqrt(2 * Eb/N0))
    eb_n0_lin = 10.0 ** (eb_n0_db_range / 10.0)
    theo_ber_bpsk = q_function(np.sqrt(2.0 * eb_n0_lin))
    
    print("\n📊 HASIL EVALUASI BER (Bit Error Rate) vs Eb/N0:")
    print("-" * 70)
    print(f"{'Eb/N0 (dB)':<12} | {'BPSK (Sim)':<14} | {'QPSK (Sim)':<14} | {'16-QAM (Sim)':<14} | {'Teori BPSK/QPSK':<16}")
    print("-" * 70)
    for i, snr_db in enumerate(eb_n0_db_range):
        print(f"{snr_db:<12.1f} | {results['BPSK'][i]:<14.6e} | {results['QPSK'][i]:<14.6e} | {results['16-QAM'][i]:<14.6e} | {theo_ber_bpsk[i]:<16.6e}")
    print("-" * 70)
    
    print("\n💡 OBSERVASI KRITIS LAB (Mentor Dr. Aris 📡):")
    print("1. Nilai BER BPSK dan QPSK identik secara teoritis pada nilai Eb/N0 yang sama!")
    print("   -> Trik ortogonalitas I/Q memungkinkan QPSK mengirim bit 2x lebih banyak tanpa penalti daya per bit.")
    print("2. 16-QAM membutuhkan Eb/N0 sekitar 4 dB lebih tinggi untuk mencapai BER yang sama dibanding QPSK.")
    print("   -> Trade-off efisiensi spektral (4 bit/simbol): jarak antar titik lebih rapat, butuh proteksi kanal lebih kuat.")

    if HAS_MATPLOTLIB:
        out_dir = os.path.dirname(os.path.abspath(__file__))
        plot_path = os.path.join(out_dir, "ber_curve_awgn.png")
        plt.figure(figsize=(9, 6))
        plt.semilogy(eb_n0_db_range, results['BPSK'], 'bo-', label='BPSK (Simulasi Monte Carlo)')
        plt.semilogy(eb_n0_db_range, results['QPSK'], 'rs--', label='QPSK (Simulasi Monte Carlo)')
        plt.semilogy(eb_n0_db_range, results['16-QAM'], 'g^-', label='16-QAM (Simulasi Monte Carlo)')
        plt.semilogy(eb_n0_db_range, theo_ber_bpsk, 'k:', linewidth=2, label='Teori Batas Analitis Q-Function')
        
        plt.grid(True, which='both', linestyle='--', alpha=0.6)
        plt.xlabel('Eb/N0 (dB)', fontsize=12)
        plt.ylabel('Bit Error Rate (BER)', fontsize=12)
        plt.title('Kurva Waterfall Kinerja Modulasi Digital di Kanal AWGN', fontsize=14)
        plt.ylim([1e-6, 1.0])
        plt.legend(fontsize=11)
        plt.tight_layout()
        plt.savefig(plot_path, dpi=200)
        plt.close()
        print(f"\n📈 Grafik kurva BER berhasil disimpan ke: {plot_path}")


if __name__ == "__main__":
    main()
