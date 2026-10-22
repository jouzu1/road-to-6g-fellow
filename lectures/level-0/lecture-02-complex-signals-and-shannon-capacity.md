# 📡 KULIAH 2: Bilangan Kompleks ($I + jQ$), Senter Ortogonal, & Batas Absolut Kapasitas Shannon
*Track: Level 0 — Kalibrasi Gelombang & Intuisi Sinyal*  
*Status: COMPLETED (Verified via Checkpoint Quiz)*

---

## 🎯 Tujuan Pembelajaran
1. Memahami intuisi fisik **In-phase ($I$)** dan **Quadrature ($Q$)** sebagai dua gelombang pembawa yang saling ortogonal (tidak saling mengganggu pada frekuensi yang sama).
2. Membongkar mitos bilangan imajiner $j$: $j = \sqrt{-1}$ bukan angka khayalan, melainkan **operator rotasi $90^\circ$** pada bidang 2D.
3. Memahami bagaimana persamaan gelombang passband RF diubah menjadi representasi **baseband kompleks (sinyal analitik)** untuk pemrosesan software di Sionna/PyTorch/NumPy.
4. Memahami hukum mutlak alam semesta nirkabel: **Teorema Kapasitas Shannon-Hartley** ($C = B \log_2(1 + \text{SNR})$).
5. Memahami asal-usul **Desah Termal Johnson-Nyquist** ($N_0 \approx -174\text{ dBm/Hz}$) dan mengapa 6G mengejar spektrum frekuensi raksasa (Sub-THz).

---

## 🔦 1. Misteri I/Q: Trik Menggandakan Data di Frekuensi yang Sama

Bayangkan Anda memiliki satu kabel tembaga atau satu antena radio yang memancarkan sinyal pada frekuensi pembawa tertentu, misalnya $f_c = 3.5\text{ GHz}$. Secara awam, kita berpikir satu frekuensi hanya bisa membawa satu aliran data. Namun, para insinyur telekomunikasi menemukan cara cerdas untuk **mengirim dua aliran data sekaligus tanpa saling tabrak**.

Trik ini disebut **Modulasi I/Q (In-phase & Quadrature)**.

```
                  ┌──────────────┐
  Bit Data I ───► │  Amplitudo I │ ───► [ x cos(2π f_c t) ] ───┐
                  └──────────────┘                               │  (+) Sinyal RF Gabungan
                                                                 ├───► Antena Pemancar
                  ┌──────────────┐                               │     s(t) = I cos - Q sin
  Bit Data Q ───► │  Amplitudo Q │ ───► [ x -sin(2π f_c t) ] ──┘
                  └──────────────┘
```

### Analogi Dua Senter Silang (Ortogonalitas)
* Bayangkan Anda berada di panggung teater yang gelap. Anda memegang dua senter dengan polarisasi cahaya yang disilangkan tepat $90^\circ$ (vertikal dan horizontal).
* Kedua sinar senter itu diarahkan ke titik layar yang sama persis.
* Penonton di depan layar yang memakai kacamata polarisasi vertikal **hanya akan melihat kedipan senter pertama**, sama sekali tidak terganggu oleh senter kedua. Begitu juga penonton berkacamata horizontal.
* Dalam matematika gelombang radio:
  * Gelombang Cosinus: $\cos(2\pi f_c t)$ disebut komponen **In-phase ($I$)**.
  * Gelombang Sinus: $-\sin(2\pi f_c t)$ disebut komponen **Quadrature ($Q$)** (karena fasenya digeser $90^\circ$ atau $\pi/2$ radian).
* Karena integral hasil kali $\cos$ dan $\sin$ pada satu periode adalah **nol**:
```math
\int_0^T \cos(\omega t) \sin(\omega t) \, dt = 0
```
Mereka disebut **ORTOGONAL**. Mereka berbagi udara yang sama tanpa saling merusak!

---

## 🧭 2. Menghapus Phobia Bilangan Kompleks ($I + jQ$)

Di bangku sekolah, kita sering diajarkan bahwa $j = \sqrt{-1}$ adalah "bilangan khayalan/imajiner". Istilah ini sangat menyesatkan para insinyur software!

> **💡 Hakikat $j$ di Software Radio:**  
> Bilangan $j$ **bukanlah halusinasi mistis**. $j$ hanyalah **operator geometris untuk memutar sumbu sebesar $90^\circ$ berlawanan arah jarum jam** di diagram kartesius 2D!
> * Jika titik $1$ dikali $j \rightarrow j$ (berada di sumbu vertikal).
> * Jika $j$ dikali $j \rightarrow j^2 = -1$ (berputar lagi $90^\circ$, mendarat di sumbu horizontal negatif).

```
                      Sumbu Q (Imajiner / Sinus)
                                ▲
                                │
                                │     • Titik Simbol (I + jQ)
                                │    /│
                     Amplitudo  │   / │
                        A       │  /  │ Q
                                │ /   │
                                │/ θ  │
        ────────────────────────┼─────┴──────────────────► Sumbu I (Riil / Cosinus)
                                │     I
                                │
                                │
```

### Mengapa Software DSP & AI (Sionna/PyTorch) Selalu Memakai Bilangan Kompleks?
Sinyal radio fisik yang keluar dari antena ke udara selalu berbentuk gelombang riil tegangan listrik:

```math
s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)
```

Namun, melakukan simulasi modulasi, propagasi fading, dan filtering pada frekuensi pembawa $f_c = 3.5\text{ GHz}$ secara langsung di komputer membutuhkan laju sampling (*sampling rate*) super tinggi (minimal puluhan Gigasample per detik)! Komputer atau GPU akan kehabisan memori dalam hitungan milidetik.

Solusinya, insinyur telekomunikasi membuang frekuensi pembawa $f_c$ dan hanya memproses "amplop informasi"-nya saja menggunakan **Formula Euler**:

```math
e^{j\theta} = \cos(\theta) + j\sin(\theta)
```

```math
s(t) = \text{Re}\left\{ (I(t) + jQ(t)) e^{j 2\pi f_c t} \right\}
```

Bagian $(I(t) + jQ(t))$ inilah yang disebut **Sinyal Baseband Kompleks** (*Equivalent Complex Baseband*).
* Sumbu **Riil** menyimpan nilai gelombang **$I(t)$**.
* Sumbu **Imajiner** menyimpan nilai gelombang **$Q(t)$**.
* Di Python / Sionna, sinyal ini cukup direpresentasikan sebagai array tipe data `complex64` atau pasangan dua float `(real, imag)`:
  ```python
  import numpy as np

  # 1 Simbol modulasi nirkabel di software
  I_value = 0.707
  Q_value = -0.707
  simbol_baseband = np.complex64(I_value + 1j * Q_value)

  print(f"Amplitudo : {np.abs(simbol_baseband):.3f}")  # Panjang vektor
  print(f"Fase (rad): {np.angle(simbol_baseband):.3f}") # Sudut rotasi
  ```

---

## 🌌 3. Batas Mutlak Alam Semesta: Teorema Kapasitas Shannon-Hartley

Pada tahun 1948, bapak teori informasi modern, **Claude Shannon**, menerbitkan karya ilmiah yang membuktikan bahwa setiap saluran nirkabel memiliki batas kecepatan transfer data maksimum tanpa salah (*error-free channel capacity*), yang dirumuskan sebagai:

```math
C = B \log_2\left(1 + \frac{S}{N}\right) \quad [\text{bits/second}]
```

Di mana:
* **$C$**: Kapasitas kanal maksimum teoritis (bps / bit per detik).
* **$B$**: Lebar pita frekuensi / Bandwidth (Hz).
* **$S$**: Daya sinyal pemancar yang diterima (*Signal power* dalam Watt).
* **$N$**: Daya desah/noise gangguan (*Noise power* dalam Watt).
* **$S/N$**: Rasio Sinyal terhadap Derau (*Signal-to-Noise Ratio* / SNR, dalam skala linier, bukan dB).

```
                              SHANNON CAPACITY TRADEOFF
                              
    Kapasitas C (Gbps)
        ▲
        │                                 / (Pita Lebar: Bandwidth Besar B)
        │                                /
        │                               /
        │                              /
        │    -------------------------/---- (Pita Sempit: Diminishing Return log2)
        │   /
        │  /
        └──┴────────────────────────────────► SNR (Daya Pemancar S)
```

### Analogi Pesta Disko Berisik (Trade-Off Bandwidth vs Daya)
Bayangkan Anda ingin berbicara dengan teman di dalam ruangan diskotik yang sangat bising (Noise $N$ tinggi):
1. **Strategi 1: Teriak Lebih Kencang (Naikkan S / SNR)**  
   Anda bisa berteriak sekuat tenaga. Tetapi tenggorokan Anda (baterai smartphone & regulasi batas paparan radiasi SAR) memiliki batas maksimal. Terlebih lagi, variabel SNR berada **di dalam logaritma ($\log_2$)**.  
   *Artinya: Untuk melipatgandakan kecepatan data sebesar $2\times$, Anda membutuhkan daya pancar eksponensial jauh lebih besar! Efisiensinya makin lama makin anjlok (*diminishing returns*).*
2. **Strategi 2: Buka Ruang Baru / Bahasa Gerak Tangan (Naikkan Bandwidth $B$)**  
   Perhatikan bahwa variabel Bandwidth $B$ berada **di luar logaritma (berbanding lurus / linier)**.  
   *Artinya: Jika Anda menaikkan lebar pita frekuensi $B$ sebanyak $10\times$, kapasitas data $C$ otomatis melesat $10\times$ lipat tanpa perlu menaikkan daya pemancar!*

> **🚀 Inilah Alasan Utama Mengapa 5G dan 6G Berlari ke Frekuensi Tinggi (mmWave & Sub-THz):**  
> Di frekuensi rendah (700 MHz - 2.6 GHz), spektrum sudah sangat padat dan sempit (hanya ada potongan 10 - 20 MHz). Tapi di pita Sub-THz (100 GHz - 300 GHz), terdapat lahan kosong selebar **puluhan Gigahertz ($B$)**, membuka gerbang menuju kecepatan **Terabit per detik (Tbps)**!

---

## ❄️ 4. Desah Termal Johnson-Nyquist: $-174\text{ dBm/Hz}$

Dari mana datangnya variabel Noise ($N$) pada rumus Shannon di atas? Apakah hanya gangguan sinyal tetangga?

Jawabannya: **Bukan. Noise berasal dari denyut partikel alam semesta itu sendiri.**

Semua benda di alam semesta yang suhunya berada di atas nol mutlak ($0\text{ Kelvin}$ atau $-273.15^\circ\text{C}$) mengalami agitasi termal acak pada elektron-elektron di dalam sirkuit konduktor dan antenanya. Gerakan elektron acak ini membangkitkan tegangan desah acak yang disebut **Desah Termal Johnson-Nyquist**.

Kerapatan spektrum daya desah termal dirumuskan oleh:

```math
N_0 = k_B \cdot T \quad [\text{Watt/Hz}]
```

* $k_B = 1.380649 \times 10^{-23}\text{ J/K}$ (Konstanta Boltzmann).
* $T$: Suhu absolut dalam Kelvin (standar temperatur ruang telekomunikasi adalah $T_0 = 290\text{ K} \approx 17^\circ\text{C}$).

Jika dikonversi ke satuan logaritmik daya telekomunikasi ($\text{dBm/Hz}$):

```math
N_0 = 10 \log_{10}\left( \frac{k_B \cdot 290 \cdot 1000}{1} \right) \approx -174\text{ dBm/Hz}
```

> **📌 Angka Suci Telekomunikasi:**  
> Angka **$-174\text{ dBm/Hz}$** adalah konstanta alamiah paling fundamental di dunia telekomunikasi.  
> Bahkan jika seluruh menara BTS, satelit, dan stasiun radio di muka bumi ini dimatikan, antena receiver smartphone Anda pada suhu kamar akan selalu mendengarkan desah latar belakang termal sebesar **$-174\text{ dBm}$ pada setiap 1 Hz lebar pita**!

---

## 🧪 5. Checkpoint Review & Verifikasi Konsep

### Soal 1:
Mengapa di software radio modern (seperti NVIDIA Sionna, PyTorch, atau GNU Radio), sinyal yang diproses pada lapisan fisik (PHY) selalu berupa array bilangan kompleks `[real, imag]` berdimensi baseband, padahal gelombang tegangan listrik yang memancar nyata di udara dari antena pemancar selalu berupa bilangan riil murni?

#### ✅ Jawaban Terverifikasi (Evaluasi Mentor Dr. Aris 📡):
* **Beban Komputasi & Sampling Nyquist:**  
  Sinyal passband RF di udara merambat pada frekuensi pembawa $f_c$ (misal $3.5\text{ GHz}$ atau $140\text{ GHz}$). Berdasarkan teorema sampling Nyquist-Shannon, memproses sinyal passband secara digital membutuhkan laju sampling minimal $f_s \ge 2 f_c$ (puluhan hingga ratusan Gigasamples per detik!). Tidak ada GPU atau memori RAM modern yang sanggup menampung komputasi floating-point sebesar itu secara real-time.
* **Equivalent Complex Baseband:**  
  Dengan memisahkan sinyal menjadi amplop informasi kompleks $I(t) + jQ(t)$ via Formula Euler dan membuang frekuensi pembawa $f_c$, sampling rate software hanya perlu sebanding dengan lebar pita informasi (**Bandwidth $B$**), bukan frekuensi pembawa.
  * Pada bandwidth $20\text{ MHz}$, laju sampling turun drastis menjadi $20 - 40\text{ MSPS}$ (ribuan kali lebih ringan dan muat di tensor PyTorch).

---

### Soal 2:
Sebuah kanal 4G LTE memiliki bandwidth $B = 20\text{ MHz}$ dengan rasio daya $\text{SNR} = 15$ (skala linier, bukan dB).

1. Berapakah kapasitas maksimum Shannon teoritis kanal tersebut dalam satuan **Megabit per detik (Mbps)**?
```math
\text{Perhitungan: } \log_2(1 + 15) = \log_2(16) = 4
```
2. Jika regulator mengizinkan operator menggandakan lebar bandwidth menjadi $B = 40\text{ MHz}$ tanpa mengubah daya pancar, berapakah kapasitas barunya? Manakah yang lebih hemat energi: menaikkan bandwidth atau menaikkan daya pemancar?

#### ✅ Jawaban Terverifikasi (Evaluasi Mentor Dr. Aris 📡):
1. **Kapasitas Awal ($B = 20\text{ MHz}$):**
```math
C_1 = 20\text{ MHz} \times \log_2(1 + 15) = 20 \times 4 = \mathbf{80\text{ Mbps}}
```
2. **Kapasitas Baru ($B = 40\text{ MHz}$):**
```math
C_2 = 40\text{ MHz} \times \log_2(1 + 15) = 40 \times 4 = \mathbf{160\text{ Mbps}}
```
3. **Efisiensi Energi (Bandwidth vs Daya):**
   * Menaikkan bandwidth jauh lebih hemat energi karena variabel $B$ berada **di luar logaritma (linier)**: menduplikasi $B$ langsung menduplikasi kapasitas ($2\times$).
   * Sebaliknya, daya sinyal $S$ berada **di dalam kurung logaritma $\log_2$**. Untuk menaikkan kapasitas dari $80\text{ Mbps}$ ke $160\text{ Mbps}$ hanya dengan menaikkan daya (tanpa menambah bandwidth), operator harus menaikkan SNR menjadi:
```math
\log_2(1 + \text{SNR}) = 8 \implies 1 + \text{SNR} = 2^8 = 256 \implies \text{SNR} = 255
```
   Daya pemancar harus dinaikkan sebesar **$255 / 15 = 17\text{ kali lipat}$ (+12.3 dB)!** Hal ini akan membakar Power Amplifier (PA), melanggar batas regulasi keselamatan radiasi manusia (SAR), dan menguras baterai ponsel seketika.

---

### 💡 Diskusi Arsitektur Lanjutan: Trade-off Memperlebar Bandwidth

> *"Tapi kalau memperlebar bandwidth, harusnya ada trade-off fisika dan komersialnya kan, Prof?"*

Pertanyaan kritis yang sangat tajam! Di industri telekomunikasi riil, tidak ada makan siang gratis (*no free lunch*). Memperlebar bandwidth memicu 4 tantangan arsitektural utama:

1. **Noise Total Ikut Membengkak ($N = N_0 \cdot B$):**  
   Berdasarkan desah termal Johnson-Nyquist, daya noise total sebanding dengan bandwidth:
```math
N = k_B \cdot T \cdot B
```
   Jika $B$ digandakan dari $20\text{ MHz}$ ke $40\text{ MHz}$, daya derau total yang masuk ke receiver otomatis naik $2\times$ (+3 dB). Jika daya pancar pemancar tidak ikut disesuaikan di area tepi sel (*cell edge*), SNR efektif riil dapat terdegradasi.

2. **Frequency-Selective Fading & Dispersi Waktu (Delay Spread):**  
   Semakin lebar bandwidth ($B$), durasi waktu per simbol menjadi semakin sempit ($T_s \approx 1/B$).  
   Gelombang radio yang terpantul dari gedung-gedung dan pegunungan tiba dengan jeda waktu beberapa mikrodetik (*multipath delay spread*), memicu tumpang tindih sinyal yang disebut **Inter-Symbol Interference (ISI)**. Kanal radio tidak lagi datar (*flat*), melainkan bergelombang (*frequency-selective*).
   * **Solusi Industri:** Inilah alasan utama mengapa 4G LTE, 5G NR, dan 6G wajib menggunakan teknik **OFDM (Orthogonal Frequency Division Multiplexing)**—yaitu memecah bandwidth lebar menjadi ribuan sub-saluran sempit yang masing-masing mengalami *flat fading*.

3. **Biaya Regulasi Spektrum Selangit (BHP Frekuensi Komdigi / IPFR):**  
   Spektrum elektromagnetik adalah sumber daya alam terbatas milik negara. Di Indonesia, lelang spektrum pita $2.1\text{ GHz}$ atau $2.6\text{ GHz}$ oleh Kementerian Komunikasi dan Digital (Komdigi) mematok Biaya Hak Penggunaan (BHP) Frekuensi mencapai ratusan miliar hingga triliunan rupiah per blok $10\text{ MHz}$ setiap tahunnya.

4. **Konsumsi Daya Sirkuit ADC/DAC (*Analog-to-Digital Converter*):**  
   Semakin lebar bandwidth $B$, sirkuit ADC pada smartphone harus mencuplik (*sample*) dengan kecepatan jauh lebih tinggi. Disipasi daya listrik sirkuit ADC berskala secara eksponensial terhadap laju sampling dan resolusi bit, menuntut arsitektur *mixed-signal* yang sangat canggih di era 6G.

---
*Catatan kuliah ini disusun bersama Mentor Dr. Aris (📡), Amelia (💻), & Paige (📝) untuk repositori [jouzu1/road-to-6g-fellow](https://github.com/jouzu1/road-to-6g-fellow).*
