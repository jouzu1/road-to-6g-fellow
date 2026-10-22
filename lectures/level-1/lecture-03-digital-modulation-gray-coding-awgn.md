# 📡 KULIAH 3: Papan Catur Modulasi Digital, Rahasia Gray Coding, & Simulasi Kanal AWGN
*Track: LEVEL 1 — Modulasi Digital & Kanal Nirkabel (Radio 101)*  
*Status: IN PROGRESS (Lab Code & Checkpoint Quiz Available)*  
*Squad BMAD: Dr. Aris (📡 Lead Architect), Amelia (💻 Dev), Quinn (🧪 QA), Paige (📝 Docs)*

---

## 🎯 Tujuan Pembelajaran
1. Memahami bagaimana deretan bit biner `0` dan `1` diubah menjadi koordinat titik konstelasi $(I, Q)$ pada modulasi **BPSK**, **QPSK**, dan **16-QAM**.
2. Memahami peran penting **Faktor Normalisasi Energi Simbol** ($\sqrt{E_s}$) agar perbandingan performa antar modulasi bersifat adil (*fair comparison*).
3. Membongkar trik rahasia **Gray Coding**: Mengapa urutan biner sekolah (`00, 01, 10, 11`) haram digunakan pada diagram konstelasi radio.
4. Memahami model matematis **Kanal AWGN (Additive White Gaussian Noise)** dan penurunan desah kompleks per sumbu ($\sigma = \sqrt{N_0/2}$).
5. Mengeksekusi simulasi Monte Carlo pertama di Python (`src/level-1/lab01_modulation_awgn.py`) dan memverifikasi kurva **BER vs. $E_b/N_0$** terhadap formula analitis $Q$-function.

---

## ♟️ 1. Papan Catur Modulasi: Dari Bit ke Koordinat $(I, Q)$

Di Level 0, kita sudah membuktikan bahwa sumbu **In-phase ($I$)** dan **Quadrature ($Q$)** adalah dua senter ortogonal yang tidak saling mengganggu pada frekuensi pembawa yang sama. 

Sekarang, tugas pemancar (*transmitter*) adalah mengubah aliran bit biner komputer menjadi titik koordinat tegangan pada bidang $(I, Q)$.

```
   BPSK (1 bit/simbol)           QPSK (2 bit/simbol)               16-QAM (4 bit/simbol)
        Sumbu Q                       Sumbu Q                           Sumbu Q
           ▲                             ▲                                 ▲
           │                    (01) •   │   • (00)               •   •    │    •   •
           │                             │                        •   •    │    •   •
   (1)     │     (0)                     │                                 │
 ───•──────┼──────•───► I        ────────┼────────► I        ──────────────┼──────────────► I
   -1      │     +1                      │                                 │
           │                    (11) •   │   • (10)               •   •    │    •   •
           ▼                             ▼                        •   •    │    •   •
                                                                           ▼
```

### Taksonomi Pemetaan:
1. **BPSK (Binary Phase Shift Keying) — 1 bit/simbol ($k = 1$):**
   * Bit `0` dipetakan ke koordinat $+1$.
   * Bit `1` dipetakan ke koordinat $-1$.
   * Sumbu $Q$ bernilai $0$ (hanya memanfaatkan sumbu riil).
2. **QPSK (Quadrature Phase Shift Keying) — 2 bit/simbol ($k = 2$):**
   * Mengirim 2 bit sekaligus dalam 1 pulsa simbol.
   * Memanfaatkan kedua sumbu: $I$ membawa 1 bit, $Q$ membawa 1 bit.
   * Terdapat 4 titik kuadran: $(\pm 1, \pm 1)$.
3. **16-QAM (Quadrature Amplitude Modulation) — 4 bit/simbol ($k = 4$):**
   * Mengirim 4 bit per simbol.
   * Kisi matriks $4 \times 4 = 16$ titik koordinat: amplitudo diskrit $\{-3, -1, +1, +3\}$ pada sumbu $I$ dan sumbu $Q$.

---

## ⚖️ 2. Mengapa Perlu Normalisasi Energi Simbol ($\sqrt{E_s}$)?

Di dunia nyata, Power Amplifier (PA) ponsel memiliki batas daya rata-rata maksimal $\mathbb{E}[|s|^2] = 1$. Kita tidak boleh membandingkan modulasi jika salah satunya "berbuat curang" dengan memancarkan daya lebih besar.

* **Pada QPSK:** Koordinatnya $(\pm 1, \pm 1)$.  
  Energi per titik: $1^2 + 1^2 = 2$.  
  Maka, seluruh titik harus dibagi dengan faktor normalisasi **$\sqrt{2}$**:
```math
s_{\text{QPSK}} \in \left\{ \frac{\pm 1 \pm 1j}{\sqrt{2}} \right\} \implies \mathbb{E}[|s|^2] = 1.0
```

* **Pada 16-QAM:** Koordinatnya $(\pm 1, \pm 3)$.  
  Rata-rata energi kuadrat titik:
```math
\text{Rata-rata } I^2 = \frac{(-3)^2 + (-1)^2 + 1^2 + 3^2}{4} = \frac{9 + 1 + 1 + 9}{4} = 5
```
  Karena ada sumbu $I$ dan $Q$, total energi rata-rata = $5 + 5 = 10$.  
  Maka, seluruh titik 16-QAM harus diskalakan dengan faktor normalisasi **$\sqrt{10}$**:
```math
s_{\text{16-QAM}} \in \left\{ \frac{I + jQ}{\sqrt{10}} \right\} \implies \mathbb{E}[|s|^2] = 1.0
```

---

## 🧠 3. Trik Rahasia Gray Coding: Meminimalkan Kerusakan Bit

Bayangkan sebuah titik konstelasi QPSK di kuadran pertama (`00`). Ketika badai noise menghembus sinyal, posisi titik itu sedikit bergeser dan penerima salah menebaknya ke kuadran tetangga terdekat.

```
       Biner Biasa (BAHAYA!)                      Gray Coding (STANDAR 3GPP!)
              Q                                                Q
              ▲                                                ▲
       (01) • │ • (00)                                  (01) • │ • (00)
       ───────┼───────► I                               ───────┼───────► I
       (10) • │ • (11)                                  (11) • │ • (10)
              ▼                                                ▼
```

### Mengapa Biner Biasa Berbahaya?
* Perhatikan kuadran kiri-atas (`01`) dan kanan-bawah (`10`) pada biner biasa:
  Jarak Hamming-nya = 2 bit (keduanya berubah: bit pertama `0` jadi `1`, bit kedua `1` jadi `0`).
* Jika ada sedikit derau yang mendorong titik melintasi batas sumbu, penerima akan menghasilkan **2 bit eror sekaligus** dari 1 kesalahan simbol!

### Aturan Emas Gray Coding:
> **Setiap titik konstelasi yang bertetangga langsung HANYA BOLEH BERBEDA TEPAT 1 BIT (Hamming Distance = 1).**
* Pada Gray Code, jika desah menyebabkan kesalahan tebak simbol ke tetangga terdekat, **kesalahan bit yang terjadi dijamin hanya 1 bit**. Ini menekan angka Bit Error Rate (BER) hingga 50%!

---

## 🌊 4. Model Kanal AWGN: Sinyal Bertemu Desah Semesta

Sinyal baseband kompleks yang dikirimkan ($x$) merambat melintasi udara dan terkena desah termal Johnson-Nyquist yang dimodelkan sebagai **AWGN (Additive White Gaussian Noise)**:

```math
y = x + n
```

Di mana $n = n_I + j n_Q$ adalah bilangan kompleks acak Gaussian berdistribusi normal:
* Daya total noise: $N_0$.
* Karena desah terbagi rata ke sumbu $I$ dan sumbu $Q$, variansi masing-masing sumbu adalah separuhnya:
```math
\sigma_I^2 = \sigma_Q^2 = \frac{N_0}{2} \implies \sigma = \sqrt{\frac{N_0}{2}}
```

### Hubungan Energi Bit ($E_b$) dan Energi Simbol ($E_s$):
Dalam modulasi dengan $k$ bit per simbol:
```math
E_s = k \cdot E_b \implies \frac{E_s}{N_0} = k \cdot \frac{E_b}{N_0}
```
Untuk sinyal ternormalisasi ($E_s = 1$), nilai desah $N_0$ dihitung sebagai:
```math
N_0 = \frac{1}{k \cdot (E_b/N_0)_{\text{linier}}}
```

---

## 💻 5. Eksekusi Script Python Monte Carlo (`lab01_modulation_awgn.py`)

Insinyur **Amelia (💻)** telah membangun skrip simulasi modular berstandar produksi di:  
📄 [`src/level-1/lab01_modulation_awgn.py`](file:///C:/Users/jouzu/Documents/Development/zero-to-6g-sepuh/src/level-1/lab01_modulation_awgn.py)

Skrip ini memetakan 200.000 bit biner acak, menambahkan desah AWGN, melakukan demodulasi *Minimum Euclidean Distance*, dan menghitung BER empiris untuk BPSK, QPSK, dan 16-QAM.

### 📊 Hasil Simulasi Empiris vs. Batas Analitis Teori:

| $E_b/N_0$ (dB) | BPSK (Simulasi) | QPSK (Simulasi) | 16-QAM (Simulasi) | Teori Analitis $Q(\sqrt{2 E_b/N_0})$ |
| :---: | :---: | :---: | :---: | :---: |
| **0.0 dB** | $7.83 \times 10^{-2}$ | $7.89 \times 10^{-2}$ | $1.40 \times 10^{-1}$ | **$7.86 \times 10^{-2}$** |
| **2.0 dB** | $3.75 \times 10^{-2}$ | $3.72 \times 10^{-2}$ | $9.71 \times 10^{-2}$ | **$3.75 \times 10^{-2}$** |
| **4.0 dB** | $1.29 \times 10^{-2}$ | $1.27 \times 10^{-2}$ | $5.83 \times 10^{-2}$ | **$1.25 \times 10^{-2}$** |
| **6.0 dB** | $2.41 \times 10^{-3}$ | $2.44 \times 10^{-3}$ | $2.80 \times 10^{-2}$ | **$2.39 \times 10^{-3}$** |
| **8.0 dB** | $1.85 \times 10^{-4}$ | $2.45 \times 10^{-4}$ | $9.18 \times 10^{-3}$ | **$1.91 \times 10^{-4}$** |
| **10.0 dB** | $5.00 \times 10^{-6}$ | $0.00$ | $1.58 \times 10^{-3}$ | **$3.87 \times 10^{-6}$** |
| **12.0 dB** | $0.00$ | $0.00$ | $1.05 \times 10^{-4}$ | **$9.01 \times 10^{-9}$** |

---

### 🧪 6. Catatan Audit QA (Quinn): Temuan Kritis di Balik Angka

1. **Kenapa Kurva BER BPSK dan QPSK Berimpit Sempurna?**  
   Perhatikan kolom BPSK dan QPSK pada tabel di atas. Nilai BER-nya **identik secara matematis**!  
   *Penjelasan Ilmiah:* Pada QPSK, sumbu $I$ dan sumbu $Q$ saling ortogonal. Komponen desah pada sumbu $I$ tidak bocor ke sumbu $Q$. Jadi, QPSK sebenarnya adalah **dua transmisi BPSK independen yang berjalan bersamaan**! QPSK mampu melipatgandakan data rate $2\times$ lipat tanpa membayar penalti daya per bit sepeser pun.
2. **Penalti Daya pada 16-QAM:**  
   Untuk mencapai target keandalan $\text{BER} \approx 10^{-3}$, QPSK hanya butuh $E_b/N_0 \approx 7\text{ dB}$, sedangkan 16-QAM butuh $E_b/N_0 \approx 10.5\text{ dB}$ (selisih $\approx 3.5\text{ dB}$ hingga $4\text{ dB}$).
   *Trade-off Nyata:* Jika smartphone Anda berada jauh dari BTS dengan sinyal lemah, modem akan otomatis menurunkan modulasi (*adaptive modulation and coding*) dari 256-QAM/16-QAM ke QPSK agar koneksi tidak putus.

---

## 🧪 7. Checkpoint Kuis Kuliah 3

Jawab 2 pertanyaan investigatif ini untuk mengunci pemahaman koding dan konstelasi modulasi digital:

### Soal 1:
> Mengapa pada diagram konstelasi 16-QAM berenergi rata-rata ternormalisasi ($\mathbb{E}[|s|^2] = 1$), faktor pembaginya harus berupa angka $\sqrt{10}$, bukan $\sqrt{16}$ (padahal jumlah titiknya ada 16 buah)? Tunjukkan logika hitungan rata-rata energinya!

### Soal 2:
> Jika seorang developer pemula membuat konstelasi 4-titik QPSK tetapi secara keliru menggunakan penomoran biner urut biasa (`00` di kuadran I, `01` di kuadran II, `10` di kuadran III, dan `11` di kuadran IV), jelaskan apa yang terjadi pada Bit Error Rate (BER) saat sebuah titik di kuadran II (`01`) terdorong noise melintasi sumbu horizontal ke kuadran III (`10`)! Berapa bit yang salah, dan kenapa Gray Coding menyelesaikan masalah ini?

---
*Catatan kuliah dan kode praktikum ini disusun bersama Dr. Aris (📡), Amelia (💻), Quinn (🧪), dan Paige (📝) untuk repositori [jouzu1/road-to-6g-fellow](https://github.com/jouzu1/road-to-6g-fellow).*
