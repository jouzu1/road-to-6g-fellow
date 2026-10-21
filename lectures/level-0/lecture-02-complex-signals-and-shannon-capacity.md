# 📡 KULIAH 2: Bilangan Kompleks ($I + jQ$), Senter Ortogonal, & Batas Absolut Kapasitas Shannon
*Track: Level 0 — Kalibrasi Gelombang & Intuisi Sinyal*  
*Status: IN PROGRESS (Checkpoint Quiz Available)*

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
* Karena integral hasil kali $\cos$ dan $\sin$ pada satu periode adalah **nol** ($\int_0^T \cos(\omega t) \sin(\omega t) dt = 0$), mereka disebut **ORTOGONAL**. Mereka berbagi udara yang sama tanpa saling merusak!

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

$$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

Namun, melakukan simulasi modulasi, propagasi fading, dan filtering pada frekuensi pembawa $f_c = 3.5\text{ GHz}$ secara langsung di komputer membutuhkan laju sampling (*sampling rate*) super tinggi (minimal puluhan Gigasample per detik)! Komputer atau GPU akan kehabisan memori dalam hitungan milidetik.

Solusinya, insinyur telekomunikasi membuang frekuensi pembawa $f_c$ dan hanya memproses "amplop informasi"-nya saja menggunakan **Formula Euler**:

$$e^{j\theta} = \cos(\theta) + j\sin(\theta)$$

$$s(t) = \text{Re}\left\{ (I(t) + jQ(t)) \, e^{j 2\pi f_c t} \right\}$$

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

$$C = B \log_2\left(1 + \frac{S}{N}\right) \quad [\text{bits/second}]$$

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
> Di frekuensi rendah (700 MHz – 2.6 GHz), spektrum sudah sangat padat dan sempit (hanya ada potongan 10–20 MHz). Tapi di pita Sub-THz (100 GHz – 300 GHz), terdapat lahan kosong selebar **puluhan Gigahertz ($B$)**, membuka gerbang menuju kecepatan **Terabit per detik (Tbps)**!

---

## ❄️ 4. Desah Termal Johnson-Nyquist: $-174\text{ dBm/Hz}$

Dari mana datangnya variabel Noise ($N$) pada rumus Shannon di atas? Apakah hanya gangguan sinyal tetangga?

Jawabannya: **Bukan. Noise berasal dari denyut partikel alam semesta itu sendiri.**

Semua benda di alam semesta yang suhunya berada di atas nol mutlak ($0\text{ Kelvin}$ atau $-273.15^\circ\text{C}$) mengalami agitasi termal acak pada elektron-elektron di dalam sirkuit konduktor dan antenanya. Gerakan elektron acak ini membangkitkan tegangan desah acak yang disebut **Desah Termal Johnson-Nyquist**.

Kerapatan spektrum daya desah termal dirumuskan oleh:

$$N_0 = k_B \cdot T \quad [\text{Watt/Hz}]$$

* $k_B = 1.380649 \times 10^{-23}\text{ J/K}$ (Konstanta Boltzmann).
* $T$: Suhu absolut dalam Kelvin (standar temperatur ruang telekomunikasi adalah $T_0 = 290\text{ K} \approx 17^\circ\text{C}$).

Jika dikonversi ke satuan logaritmik daya telekomunikasi ($\text{dBm/Hz}$):

$$N_0 = 10 \log_{10}\left( \frac{k_B \cdot 290 \cdot 1000}{1} \right) \approx \mathbf{-174\text{ dBm/Hz}}$$

> **📌 Angka Suci Telekomunikasi:**  
> Angka **$-174\text{ dBm/Hz}$** adalah konstanta alamiah paling fundamental di dunia telekomunikasi.  
> Bahkan jika seluruh menara BTS, satelit, dan stasiun radio di muka bumi ini dimatikan, antena receiver smartphone Anda pada suhu kamar akan selalu mendengarkan desah latar belakang termal sebesar **$-174\text{ dBm}$ pada setiap 1 Hz lebar pita**!

---

## 🧪 5. Checkpoint Kuis Kuliah 2

Untuk memverifikasi pemahaman Anda sebelum kita melangkah ke modul modulasi digital di Level 1, jawab 2 pertanyaan konseptual berikut:

### Soal 1:
> Mengapa di software radio modern (seperti NVIDIA Sionna, PyTorch, atau GNU Radio), sinyal yang diproses pada lapisan fisik (PHY) selalu berupa array bilangan kompleks `[real, imag]` berdimensi baseband, padahal gelombang tegangan listrik yang memancar nyata di udara dari antena pemancar selalu berupa bilangan riil murni?

### Soal 2:
> Sebuah kanal 4G LTE memiliki bandwidth $B = 20\text{ MHz}$ dengan rasio daya $\text{SNR} = 15$ (skala linier, bukan dB).  
> 1. Berapakah kapasitas maksimum Shannon teoritis kanal tersebut dalam satuan **Megabit per detik (Mbps)**? *(Petunjuk: $\log_2(1 + 15) = \log_2(16)$)*.  
> 2. Jika regulator mengizinkan operator menggandakan lebar bandwidth menjadi $B = 40\text{ MHz}$ tanpa mengubah daya pancar, berapakah kapasitas barunya? Manakah yang lebih hemat energi: menaikkan bandwidth atau menaikkan daya pemancar?

---
*Catatan kuliah ini disusun bersama Mentor Dr. Aris (📡) & Amelia (💻) untuk repositori [jouzu1/road-to-6g-fellow](https://github.com/jouzu1/road-to-6g-fellow).*
