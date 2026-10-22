# 🏆 LEVEL 0 COMPREHENSIVE EXAM & SYSTEM AUDIT
*Track: Level 0 — Kalibrasi Gelombang & Intuisi Sinyal*  
*Status: PASSED WITH DISTINCTION (Nilai Akhir: 98/100)*  
*Examiner: Dr. Aris (Principal Telecom Architect & 6G Systems Fellow)*

---

## 🎯 Gambaran Ujian
Ujian komprehensif ini menguji sintesis pemahaman lintas modul dari **Kuliah 1** (Waktu vs Frekuensi, Fisika Antena, Propagasi) dan **Kuliah 2** (Representasi I/Q, Formula Euler, Batas Shannon, Desah Johnson-Nyquist) dalam bentuk studi kasus audit tautan radio 5G/6G dunia nyata.

---

## 🏢 Studi Kasus Rekayasa Lapangan

Sebuah konsorsium telekomunikasi mengaudit dua sistem nirkabel:
* **Use Case 1 (Sub-1GHz IoT):** Frekuensi $f_c = 700\text{ MHz}$, Bandwidth $B = 10\text{ MHz}$, untuk pembacaan meteran cerdas (*smart metering*) di basement bawah tanah.
* **Use Case 2 (6G Sub-THz Kiosk):** Frekuensi $f_c = 140\text{ GHz}$, Bandwidth $B = 2\text{ GHz}$, untuk stasiun unduh data ultra-cepat (*instant movie download kiosk*) di bandara.

---

## 📝 Evaluasi Jawaban Mahasiswa & Bedah Konsep

### Bagian A: Fisika Gelombang, Antena, & Propagasi

#### Soal 1: Dimensi Antena $\lambda/4$ Monopole ($c = 3 \times 10^8\text{ m/s}$)
* **Use Case 1 (700 MHz):**
```math
\lambda = \frac{3 \times 10^8\text{ m/s}}{700 \times 10^6\text{ Hz}} \approx 0.428\text{ m} = 42.8\text{ cm}
```
Panjang antena $\lambda/4 \approx \mathbf{10.7\text{ cm}}$ (seukuran antena handheld atau bentangan antena pita di bodi ponsel).

* **Use Case 2 (140 GHz):**
```math
\lambda = \frac{3 \times 10^8\text{ m/s}}{140 \times 10^9\text{ Hz}} \approx 0.00214\text{ m} = 2.14\text{ mm}
```
Panjang antena $\lambda/4 \approx \mathbf{0.535\text{ mm}}$ ($0.0005\text{ meter}$).

* **Verifikasi Jawaban:**  
  Mahasiswa menjawab tepat **$0.0005\text{ m}$ ($0.5\text{ mm}$)** dan mengidentifikasi bahwa antena $140\text{ GHz}$ inilah yang muat dicetak langsung sebagai *Antenna-on-Chip (AoC)* di dalam kemasan IC silikon.

#### Soal 2: Penetrasi Beton vs Hambatan Line-of-Sight (LOS)
* **Verifikasi & Pelurusan Terminologi:**  
  * **Gelombang Panjang ($700\text{ MHz}$, $\lambda = 42.8\text{ cm}$):** Memiliki **kemampuan difraksi yang BESAR/KUAT**. Sinyal mampu meliuk dan membelok melewati sudut celah pintu, ventilasi, dan tangga basement karena ukuran celah fisik sebanding dengan panjang gelombangnya. Atenuasi material beton pada frekuensi rendah juga relatif kecil.
  * **Gelombang Pendek ($140\text{ GHz}$, $\lambda = 2.14\text{ mm}$):** Memiliki **kemampuan difraksi yang SANGAT KECIL/LEMAH**. Gelombang merambat lurus seperti sorot lampu laser (*quasi-optical*). Sedikit saja terhalang kertas HVS atau telapak tangan, sinyal langsung mengalami pemblokiran total (*deep shadowing blockage*) serta serapan molekuler tinggi.

---

### Bagian B: Representasi I/Q & Software Radio

#### Soal 3: Ortogonalitas Fase 90° & Pemrosesan Baseband di Software
* **Kenapa $I(t)$ dan $Q(t)$ tidak bertabrakan di udara?**  
  Mahasiswa menjawab tepat: Karena keduanya memiliki **perbedaan fase tepat $90^\circ$ ($\pi/2$ radian)** sehingga fungsi $\cos(2\pi f_c t)$ dan $-\sin(2\pi f_c t)$ bersifat **ORTOGONAL**. Hasil kali integral keduanya pada satu periode adalah nol:
```math
\int_0^T \cos(2\pi f_c t) \sin(2\pi f_c t) \, dt = 0
```
* **Kenapa Software (Sionna/PyTorch) hanya memproses baseband `I + 1j*Q`?**  
  Mahasiswa menjawab tepat: Jika software harus mensimulasikan gelombang pembawa $f_c = 3.5\text{ GHz}$ atau $140\text{ GHz}$, GPU harus mencuplik data dengan laju sampling raksasa (Gigasamples per detik), yang seketika menyebabkan **Out-of-Memory (OOM)**. Dengan representasi baseband kompleks, laju sampling cukup sebanding dengan bandwidth informasi ($B$), menghemat komputasi dan memori ribuan kali lipat.

---

### Bagian C: Batas Alam Semesta Shannon & Desah Termal

#### Soal 4: Menghitung Noise Floor Semesta ($B = 10\text{ MHz}$, $T = 290\text{ K}$)
```math
N = N_0 + 10\log_{10}(B) = -174\text{ dBm/Hz} + 70\text{ dB} = \mathbf{-104\text{ dBm}}
```
* **Verifikasi Jawaban:** Mahasiswa menjawab tepat **$-104\text{ dBm}$**.

#### Soal 5: SNR & Kapasitas Shannon Kanal
* **Perhitungan SNR:**
```math
\text{SNR}_{\text{dB}} = S_{\text{dBm}} - N_{\text{dBm}} = -74\text{ dBm} - (-104\text{ dBm}) = \mathbf{30\text{ dB}}
```
Rasio linier: $30\text{ dB} = 10^{30/10} = \mathbf{1000}$.
* **Kapasitas Kanal Shannon:**
```math
C = B \log_2(1 + \text{SNR}) = 10\text{ MHz} \times \log_2(1 + 1000) \approx 10\text{ MHz} \times 10 = \mathbf{100\text{ Mbps}}
```
* **Verifikasi Jawaban:** Mahasiswa menjawab **$100$** (tepat secara numerik, dengan catatan satuannya adalah **$100\text{ Mbps}$ / Megabit per detik**, bukan bps).

---

## 🎖️ Keputusan Dewan Penguji

Mahasiswa dinyatakan **LULUS LEVEL 0 DENGAN PREDIKAT SANGAT MEMUASKAN**. Seluruh intuisi fisika sinyal, kalkulasi dimensi antena, ortogonalitas modulasi I/Q, hingga batas matematis kapasitas Shannon telah dikuasai dengan kokoh.

**Rekomendasi:** Membuka gerbang kurikulum menuju **LEVEL 1: Modulasi Digital (BPSK, QPSK, 16-QAM), Gray Coding, & Simulasi Kanal AWGN**.

---
*Catatan ujian komprehensif ini diarsipkan oleh Paige (📝) dan diverifikasi oleh Amelia (💻) di repositori [jouzu1/road-to-6g-fellow](https://github.com/jouzu1/road-to-6g-fellow).*
