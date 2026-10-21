# Arsitektur, Sistem, dan Implementasi Jaringan 6G: Dari Kerangka Kerja Regulatoris hingga Simulasi Lapisan Fisik Berbasis Kecerdasan Buatan

## 1. Visi High-Level dan Kerangka Kerja Standardisasi Global (ITU-R IMT-2030 & 3GPP)

Evolusi jaringan seluler generasi keenam (6G) menandai pergeseran paradigma mendasar dari sekadar penyedia saluran konektivitas data pita lebar menjadi sistem terintegrasi yang menyatukan komunikasi nirkabel, penginderaan spasial, komputasi terdistribusi, dan kecerdasan buatan (*Artificial Intelligence* / AI) [cite: 1, 2]. Secara formal, badan pengatur spektrum dan standar telekomunikasi global di bawah naungan Perserikatan Bangsa-Bangsa, yaitu *International Telecommunication Union Radiocommunication Sector* (ITU-R), meratifikasi sebutan resmi bagi teknologi 6G sebagai **IMT-2030** melalui penerbitan *Recommendation ITU-R M.2160* pada akhir tahun 2023 [cite: 1, 3, 4]. Dokumen ini menjadi pilar utama yang menetapkan kerangka kerja, skenario penggunaan, serta persyaratan kinerja teknis minimum yang wajib dipenuhi oleh konsorsium pengembang teknologi nirkabel di seluruh dunia [cite: 1, 4].

Proses standardisasi 6G berjalan melalui mekanisme bertahap yang terstruktur ketat antara ITU-R dan badan pembentuk spesifikasi teknis industri, yaitu *3rd Generation Partnership Project* (3GPP) [cite: 4, 5]. ITU-R bertindak menetapkan visi dan kriteria evaluasi tingkat tinggi, sedangkan 3GPP bertugas menerjemahkan kriteria tersebut ke dalam protokol radio serta arsitektur jaringan yang dapat diimplementasikan secara komersial [cite: 4]. Rekomendasi ITU-R M.2160 yang diselesaikan pada akhir 2023 menandai selesainya fase formulasi visi [cite: 1, 2]. Selanjutnya, konsorsium Working Party 5D (WP 5D) merumuskan panduan evaluasi teknis melalui laporan *Technical Performance Requirements* (TPR) dan *Evaluation Guidelines* [cite: 1, 6]. Memasuki fase pengoperasian spesifikasi, 3GPP memulai studi eksplorasi awal pada Release 20, sebelum dilanjutkan dengan penyusunan spesifikasi normatif pada Release 21 [cite: 5]. Evaluasi independen atas kandidat teknologi radio 6G akan berlangsung hingga konsensus global dicapai dan diratifikasi resmi oleh ITU-R sebagai standar IMT-2030 pada tahun 2030 [cite: 1, 4].

### Transisi Skenario Penggunaan dari 5G ke 6G

Rekomendasi ITU-R M.2160 memperluas tiga skenario penggunaan klasik pada era 5G (IMT-2020)—yakni *enhanced Mobile Broadband* (eMBB), *Ultra-Reliable and Low-Latency Communication* (URLLC), dan *massive Machine Type Communication* (mMTC)—menjadi enam skenario penggunaan utama yang mendefinisikan kemampuan 6G [cite: 1, 4, 6]. Skenario *Immersive Communication* (IC) dikembangkan sebagai evolusi langsung dari eMBB untuk mengakomodasi kebutuhan *throughput* sangat tinggi dan interaksi audio-visual real-time pada aplikasi *Extended Reality* (XR), pemetaan holografik, serta antarmuka manusia-mesin presisi [cite: 1, 2]. Skenario *Hyper-Reliable and Low-Latency Communication* (HRLLC) mengevolusikan URLLC dengan memperketat toleransi keterlambatan sinyal (*latency*) dan meningkatkan keandalan transmisi hingga tingkat kritis yang dibutuhkan oleh operasi medis jarak jauh, otomatisasi industri berat, serta sistem kendali kendaraan otonom [cite: 1, 6]. Skenario *Massive Communication* (MC) menyempurnakan mMTC guna mendukung integrasi jaringan sensor skala besar dengan kepadatan ekstrim di lingkungan kota cerdas (*smart cities*) dan pemantauan lingkungan berkelanjutan [cite: 1, 6].

Di samping tiga skenario evolusioner tersebut, ITU-R menetapkan tiga skenario penggunaan baru yang tidak dimiliki oleh generasi sebelumnya [cite: 4, 6]. *Ubiquitous Connectivity* (UC) dirancang untuk mengatasi jurang digital dengan menjamin akses konektivitas pita lebar dasar di kawasan terisolasi, lautan, dan ruang udara melalui integrasi harmonis antara jaringan terestrial dan *Non-Terrestrial Networks* (NTN) berbasis satelit *Low Earth Orbit* (LEO) [cite: 1, 2, 7]. *Artificial Intelligence and Communication* (AIAC) menyediakan fondasi bagi komputasi AI terdistribusi, memfasilitasi pertukaran parameter *federated learning*, inferensi di batas jaringan (*edge AI*), serta optimalisasi lalu lintas data antar node cerdas secara otonom [cite: 1, 6]. Skenario *Integrated Sensing and Communication* (ISAC) memanfaatkan pemancaran gelombang radio untuk menjalankan fungsi ganda, yaitu sebagai media transmisi informasi sekaligus sebagai radar pencitraan spasial untuk pelacakan posisi, rekonstruksi peta 3D, dan deteksi pergerakan objek [cite: 1, 6].

### Persyaratan Kinerja Teknis Minimum (Technical Performance Requirements)

Guna merealisasikan skenario penggunaan di atas, ITU-R menyusun 15 kapabilitas kunci yang terdiri dari sembilan kapabilitas peningkat kinerja dari era 5G dan enam kapabilitas baru yang spesifik dirancang untuk era 6G [cite: 4, 6].

| No | Kapabilitas Kunci | Status vs IMT-2020 | Target Indikatif IMT-2030 (ITU-R M.2160) |
| :--- | :--- | :--- | :--- |
| 1 | Peak Data Rate | Ditingkatkan | $50 \text{ hingga } 200 \text{ Gbit/s}$ [cite: 4] |
| 2 | User-Experienced Data Rate | Ditingkatkan | $300 \text{ hingga } 500 \text{ Mbit/s}$ [cite: 4] |
| 3 | Spectrum Efficiency | Ditingkatkan | $1.5\times \text{ hingga } 3\times \text{ dibanding IMT-2020}$ [cite: 4] |
| 4 | Area Traffic Capacity | Ditingkatkan | $30 \text{ hingga } 50 \text{ Mbit/s/m}^2$ [cite: 4] |
| 5 | Connection Density | Ditingkatkan | $10^6 \text{ hingga } 10^8 \text{ perangkat/km}^2$ [cite: 4] |
| 6 | Mobility | Ditingkatkan | $500 \text{ hingga } 1000 \text{ km/h}$ [cite: 4] |
| 7 | Latency (User Plane) | Ditingkatkan | $0.1 \text{ hingga } 1 \text{ ms}$ [cite: 4] |
| 8 | Reliability | Ditingkatkan | $1 - 10^{-5} \text{ hingga } 1 - 10^{-7} \text{ probabilitas sukses}$ [cite: 4] |
| 9 | Security & Resilience | Ditingkatkan | Aman sejak desain (*Secure by Design*) [cite: 2, 4] |
| 10 | Coverage | Baru | Cakupan terintegrasi terestrial dan non-terestrial [cite: 4, 7] |
| 11 | Positioning | Baru | Akurasi posisi $1 \text{ hingga } 10 \text{ cm}$ [cite: 4] |
| 12 | Sensing-Related Capabilities | Baru | Presisi tinggi deteksi lokasi, kecepatan, dan pemetaan [cite: 4] |
| 13 | AI-Related Capabilities | Baru | Dukungan integrasi AI native dan komputasi terdistribusi [cite: 4] |
| 14 | Sustainability | Baru | Peningkatan efisiensi energi dan rasio jejak karbon [cite: 2, 4] |
| 15 | Interoperability | Baru | Antarmuka terbuka multi-vendor (*Open RAN*) [cite: 4] |

Terdapat perbedaan mendasar antara target aspiratif yang ditetapkan oleh ITU-R M.2160 dan *Key Performance Indicators* (KPI) operasional yang disusun dalam dokumen teknis internal 3GPP seperti TR 38.914 [cite: 4]. Kerangka kerja ITU-R memberikan rentang nilai ideal sebagai panduan arah riset jangka panjang bagi komunitas ilmiah [cite: 4]. Sebaliknya, 3GPP menetapkan ambang batas evaluasi terikat yang didasarkan pada pemodelan parameter sistem yang realistis [cite: 4]. Sebagai gambaran, target *peak data rate* sebesar $36 \text{ Gbit/s}$ yang dihitung oleh 3GPP diturunkan secara terikat dari asumsi efisiensi spektral puncak sebesar $60 \text{ bit/s/Hz}$ yang dioperasikan pada agregasi spektrum sebesar $600 \text{ MHz}$, sementara ITU-R mencantumkan rentang aspiratif hingga $200 \text{ Gbit/s}$ untuk kondisi operasional spektrum yang lebih ekstrem [cite: 4].

---

## 2. Fondasi Teknologi Low-Level dan Enabler Lapisan Fisik (Physical Layer & Radio)

Pada tingkatan fisik terendah (*low-level*), realisasi kinerja 6G bersumber dari inovasi pada ranah rekayasa propagasi elektromagnetik, material canggih, dan pemrosesan sinyal digital ter-otomasi [cite: 8, 9].

### Gelombang Terahertz (THz) dan Karakteristik Kanal Propagasi

Penyediaan laju data ratusan gigabit per detik menuntut perluasan pita frekuensi operasi melampaui gelombang milimeter (*mmWave*) menuju spektrum *Terahertz* (0.1 THz hingga 10 THz), khususnya pada rentang spektrum $92 \text{ GHz}$ hingga $300 \text{ GHz}$ yang diklasifikasikan sebagai pita Sub-THz [cite: 7, 10]. Laporan ITU-R M.2541 memverifikasi kelayakan teknis pemanfaatan spektrum di atas $92 \text{ GHz}$ untuk komunikasi seluler [cite: 7]. Pemodelan matematis sinyal transmisi pada spektrum THz dengan konfigurasi sistem *Multiple-Input Multiple-Output* (MIMO) merumuskan vektor sinyal terima $\tilde{\mathbf{y}}$ sebagai berikut [cite: 9]:

$$\tilde{\mathbf{y}} = \sqrt{P} h_{pl} h_{s} \mathbf{H} \mathbf{w} x + \mathbf{n}$$

Dalam persamaan tersebut, $\tilde{\mathbf{y}} \in \mathbb{C}^{N_r \times 1}$ mewakili vektor sinyal yang diterima pada $N_r$ elemen antena penerima, di mana $P$ merepresentasikan daya transmisi total [cite: 9]. Variabel $h_{pl}$ mewakili koefisien kerugian jalur (*path loss*) THz yang secara dominan dipengaruhi oleh penyerapan molekuler uap air ($H_2O$) dan oksigen ($O_2$), sedangkan $h_{s}$ adalah variabel acak yang memodelkan penampangan bayangan (*shadowing*) [cite: 9, 10]. Matriks $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ menyatakan matriks kanal MIMO antara $N_t$ antena pemancar dan $N_r$ antena penerima, $\mathbf{w} \in \mathbb{C}^{N_t \times 1}$ adalah vektor pembentukan berkas sinyal (*beamforming*), $x$ adalah simbol data ter-modulasi, dan $\mathbf{n} \in \mathbb{C}^{N_r \times 1}$ merepresentasikan *Additive White Gaussian Noise* (AWGN) [cite: 9].

Pemanfaatan spektrum THz dihadapkan pada redaman atmosferik yang sangat tinggi dan fenomena *beam splitting*, di mana berkas gelombang elektromagnetik mengalami pembiasan sudut yang berbeda pada sub-pembawa frekuensi yang berbeda di sepanjang pita lebar [cite: 9, 10]. Guna mengatasi pelemahan sinyal yang ekstrem ini, arsitektur radio 6G mengadopsi antena holografik (*holographic MIMO*) yang memadatkan ribuan elemen antena mikro dalam ruang terbatas untuk menghasilkan berkas sinyal berdaya fokus tinggi [cite: 10, 11].

### Reconfigurable Intelligent Surfaces (RIS)

*Reconfigurable Intelligent Surfaces* (RIS) menghadirkan paradigma baru di mana lingkungan propagasi radio tidak lagi diperlakukan sebagai variabel acak yang pasif, melainkan sebagai elemen yang dapat dikendalikan [cite: 9, 12]. RIS dibangun dari permukaan planar yang terdiri dari susunan metamaterial elektronik [cite: 12]. Setiap elemen mikro pada RIS mampu mengubah fase ($\theta$) dan amplitudo ($\alpha$) gelombang elektromagnetik yang memantul melaluinya secara independen berdasarkan kontrol penggerak berbasis semikonduktor [cite: 9, 12].

Sifat pemantulan sinyal dari elemen RIS ke-$m$ dimodelkan secara matematis melalui koefisien pergeseran kompleks:

$$\phi_m = \alpha_m e^{j \theta_m}$$

Di mana $\alpha_m \in [0, 1]$ menyatakan rentang rekayasa amplitudo dan $\theta_m \in [0, 2\pi)$ menentukan pergeseran fase gelombang [cite: 9]. Arsitektur RIS diklasifikasikan ke dalam dua kategori utama [cite: 9]. RIS Pasif bekerja memantulkan dan mengarahkan fase sinyal tanpa dilengkapi komponen penguat daya aktif, sehingga bebas dari *hardware noise* tambahan namun mengalami efek kerugian jalur ganda (*double path-loss effect*) [cite: 9]. Sebaliknya, RIS Aktif dilengkapi amplifier daya skala mikro pada setiap elemennya untuk memperkuat intensitas sinyal pantulan, sehingga efektif mengatasi kerugian jalur ganda pada pita frekuensi THz [cite: 9, 12].

### Formulasi Bentuk Gelombang Integrated Sensing and Communications (ISAC)

Teknologi ISAC menggabungkan fungsi komunikasi data dan fungsi radar penginderaan spasial ke dalam satu sinyal pemancar tunggal (*unified waveform*) [cite: 9, 10]. Pemanfaatan lebar pita spektrum THz yang mencapai puluhan gigahertz memberikan resolusi domain waktu yang sangat tinggi, memungkinkan jaringan nirkabel mendeteksi posisi, kontur, dan kecepatan pergerakan objek dengan presisi hingga rentang milimeter [cite: 10].

Desain sinyal ISAC menghadapi kompromi fundamental (*inherent trade-off*) dalam alokasi sumber daya [cite: 9]. Pengoptimalan bentuk gelombang untuk mengoperasionalkan kapasitas transmisi data berbasis teori informasi Shannon sering kali berlawanan dengan pengoptimalan bentuk gelombang untuk meminimalkan batas bawah variansi estimasi parameter radar yang dirumuskan oleh *Cramér-Rao Bound* (CRB) [cite: 9, 10]. Oleh karena itu, arsitektur pemrosesan sinyal ISAC mengandalkan algoritma optimasi dinamis untuk membagi daya transmisi dan ruang sub-pembawa frekuensi secara adaptif sesuai prioritas kebutuhan jaringan [cite: 9, 10].

### Antarmuka Udara Berbasis AI-Native dan Penerima Saraf (Neural Receiver)

Berbeda dengan evolusi jaringan 5G yang menempatkan algoritma pembelajaran mesin sebagai modul optimasi tambahan di luar rantai pemrosesan utama, jaringan 6G mengadopsi antarmuka udara bawaan AI (*AI-native air interface*) [cite: 13, 14, 15]. Blok pemrosesan sinyal konvensional pada sisi penerima—seperti estimasi kanal *Least Squares* (LS), estimasi *Minimum Mean Square Error* (MMSE), ekualisasi sinyal, dan *demapping* QAM—digantikan oleh arsitektur jaringan saraf tiruan mendalam (*deep neural network*) yang dikenal sebagai *Neural Receiver* [cite: 11, 14].

*Neural Receiver* menerima masukan berupa sampel sinyal domain waktu I/Q yang mengalami distorsi kanal dan secara langsung memprediksi nilai *Log-Likelihood Ratios* (LLR) yang siap diproses oleh dekoder *Low-Density Parity-Check* (LDPC) [cite: 11, 14]. Proses pelatihan arsitektur ini dilakukan secara *end-to-end* dengan mengoptimalkan fungsi kerugian *Binary Cross-Entropy* (BCE):

$$\mathcal{L}_{BCE} = -\frac{1}{N} \sum_{i=1}^{N} \left[ b_i \log(\sigma(LLR_i)) + (1 - b_i) \log(1 - \sigma(LLR_i)) \right]$$

Di mana $b_i \in \{0, 1\}$ menyatakan bit data aktual yang dikirimkan, $LLR_i$ mewakili keluaran estimasi dari jaringan saraf, dan $\sigma(\cdot)$ adalah fungsi aktivasi sigmoid [cite: 11]. Penggunaan *Neural Receiver* terbukti meningkatkan ketahanan transmisi sinyal terhadap non-linearitas komponen perangkat keras dan kerumitan fenomena *fading* pada spektrum THz [cite: 11, 14].

---

## 3. Ekosistem Hands-on, Framework Simulasi, dan Implementasi Perangkat Lunak

Eksperimentasi dan riset 6G membutuhkan platform simulasi komputasional berkinerja tinggi yang mendukung perhitungan matriks ter-akselerasi serta pemodelan propagasi berbasis fisika presisi [cite: 13, 16, 17].

### Platform Simulasi Lapisan Fisik NVIDIA Sionna

NVIDIA Sionna adalah pustaka sumber terbuka (*open-source*) berbasis Python dan PyTorch/TensorFlow yang dirancang untuk riset pemrosesan sinyal nirkabel tingkat lanjut [cite: 13, 16, 17, 18]. Keunggulan utama Sionna terletak pada arsitekturnya yang *end-to-end differentiable*, memungkinkan perhitungan turunan matematis (*backpropagation*) melintasi seluruh blok sistem komunikasi untuk melatih model pemrosesan sinyal berbasis AI [cite: 16, 17].

Arsitektur pustaka Sionna terbagi ke dalam tiga komponen modular utama [cite: 17, 18]:

*   **Sionna PHY**: Menyediakan pustaka simulasi *link-level* untuk rantai komunikasi fisik lengkap, mencakup blok pengodean LDPC/Polar, pemetaan modulasi QAM/OFDM, serta estimasi kanal [cite: 17, 18].
*   **Sionna RT**: Mesin *ray tracing* berbasis pustaka Mitsuba 3 dan Dr.Jit yang mampu memodelkan propagasi gelombang radio dalam lingkungan 3D nyata secara presisi, mencakup fenomena pemantulan, difraksi, dan pembiasan [cite: 11, 17, 18].
*   **Sionna SYS**: Framework simulasi *system-level* berbasis abstraksi lapisan fisik untuk mengevaluasi manajemen sumber daya radio pada arsitektur multi-sel [cite: 17, 18].

#### Implementasi Kode Python: Neural Demapper dan Ray Tracing Sionna RT

Struktur blok pemrosesan *Neural Demapper* yang menggantikan modul konvensional dapat dibangun menggunakan pustaka PyTorch di dalam lingkungan Sionna [cite: 11]:

```python
import torch
import torch.nn as nn

class NeuralDemapper(nn.Module):
    def __init__(self, num_bits_per_symbol):
        super(NeuralDemapper, self).__init__()
        # Input terdiri dari komponen Real(y), Imag(y), dan estimasi variansi noise (no)
        self.dense1 = nn.Linear(3, 16)
        self.relu = nn.ReLU()
        self.dense2 = nn.Linear(16, num_bits_per_symbol)

    def forward(self, y, no):
        # Menyusun komponen Real, Imag, dan Noise Variance ke dalam tensor
        real_y = torch.real(y).unsqueeze(-1)
        imag_y = torch.imag(y).unsqueeze(-1)
        noise_var = no.repeat(real_y.shape).unsqueeze(-1)
        
        input_tensor = torch.cat([real_y, imag_y, noise_var], dim=-1)
        
        # Pemrosesan linier dan aktivasi jaringan saraf
        x = self.relu(self.dense1(input_tensor))
        llr = self.dense2(x)
        return llr
```

Untuk mengeksekusi simulasi ray tracing propagasi gelombang elektromagnetik pada adegan perkotaan 3D, skrip Python menggunakan modul **Sionna RT** dijalankan melalui prosedur berikut [cite: 11]:

```python
import sionna
from sionna.rt import load_scene

# 1. Memuat model adegan 3D lingkungan perkotaan (misalnya adegan Munich)
scene = load_scene(sionna.rt.scene.munich)

# 2. Menghitung lintasan propagasi gelombang elektromagnetik dari pemancar ke penerima
paths = scene.compute_paths()

# 3. Menghitung peta cakupan sinyal (Coverage Map) pada area simulasi
cm = scene.coverage_map()

# 4. Visualisasi adegan 3D beserta lintasan sinyal dan distribusi kekuatan daya
scene.render(paths=paths, coverage_map=cm)
```

### Deployment Real-Time: Sionna Research Kit (SRK) dan OpenAirInterface (OAI)

Pengujian algoritma 6G pada lingkungan radio nyata dapat diwujudkan menggunakan *Sionna Research Kit* (SRK) [cite: 14, 15, 19]. SRK mengintegrasikan modul AI lapisan fisik ber-akselerasi GPU ke dalam tumpukan protokol radio berstandar industri berbasis *OpenAirInterface* (OAI) [cite: 14, 19]. Sistem ini beroperasi secara *real-time* menggunakan perangkat keras *Software-Defined Radio* (SDR) seperti USRP yang dihubungkan ke platform komputasi akselerasi GPU seperti NVIDIA Jetson AGX Orin atau DGX Spark [cite: 15, 17, 19].

Integrasi ini memungkinkan eksekusi fungsi pemrosesan sinyal lapisan fisik (L1) dan kontrol lapisan akses media (L2) dilakukan secara *inline acceleration* pada memori GPU terpadu, menghilangkan hambatan *latency* transfer data antara memori utama CPU dan akselerator [cite: 14, 19].

#### Instruksi Pengoperasian Lingkungan Sionna Research Kit

Prosedur konfigurasi dan eksekusi platform uji coba SRK pada sistem operasi Linux berbasis komputasi akselerasi dilakukan melalui tahapan perintah terminal berikut [cite: 15]:

```bash
# Cloning repositori resmi Sionna Research Kit dari GitHub
git clone https://github.com/NVlabs/sionna-rk.git && cd sionna-rk

# Menyiapkan dependensi sistem dan mengonfigurasi driver GPU
make prepare-system

# Menguji ulang booting sistem untuk mengaktifkan modul kernel
sudo reboot

# Melakukan kompilasi container image lingkungan Sionna Research Kit
make sionna-rk

# Memulai eksekusi alur simulasi RF real-time pada moda emulator
./scripts/start_system.sh rfsim_arm64
```

### Simulasi Skala Luas dan Digital Network Twins (DNT)

Untuk pengujian arsitektur jaringan skala besar yang melibatkan mobilitas tinggi, kerangka simulasi jaringan terdistribusi **ns-3** dapat diintegrasikan dengan mesin ray tracing Sionna RT guna membentuk *Digital Network Twins* (DNT) [cite: 20, 21]. Pendekatan ini memungkinkan pemodelan rekaan digital dari kota nyata secara presisi [cite: 20, 21]. Pelatihan dan validasi model AI sebelum diimplementasikan ke jaringan seluler produksi didukung oleh keberadaan dataset multimodal publik seperti **DeepSense 6G** dan **DeepVerse 6G**, yang menggabungkan data temporal sinyal RF, gambar kamera, posisi GPS, dan pemindaian LiDAR [cite: 20].

---

## 4. Peta Jalan Pembelajaran Komprehensif dan Sumber Daya Terintegrasi

Proses pemahaman teknologi jaringan 6G secara mendalam membutuhkan acuan literatur terstruktur, platform pengodean hands-on, dan modul kursus akademik yang kredibel [cite: 8, 18, 22, 23].

| Kategori Sumber Daya | Nama Sumber Daya | Fokus Riset & Deskripsi Teknis | Akses / Rujukan |
| :--- | :--- | :--- | :--- |
| **Buku Teks Akademik** | *6G-Enabled Technologies for Next Generation* (Wiley-IEEE Press) | Spektrum THz, Holographic MIMO, Komunikasi Kuantum, Hardware Hijau [cite: 8]. | ISBN: 978-1-394-25833-8 [cite: 8] |
| **Buku Teks Akademik** | *Reconfigurable Intelligent Surfaces for 6G and Beyond* (Wiley-IEEE Press) | Pemodelan Kanal RIS, Algoritma Optimasi Fase, Sistem Aktif vs Pasif [cite: 12]. | ISBN: 978-1-394-25014-1 [cite: 12] |
| **Buku Teks Akademik** | *6G Security: New Frontiers in Mobile Network Technologies* (Wiley-IEEE Press) | Keamanan Network Slicing, Blockchain, Enkripsi Tahan Kuantum [cite: 24]. | ISBN: 978-1-394-29247-9 [cite: 24] |
| **Buku Teks Akademik** | *Millimeter Wave and Terahertz Devices for 5G/6G* (Springer Nature) | Rangkaian Pasif THz, Metrologi Terahertz, Perangkat Berbasis Grafena [cite: 25]. | ISBN: 978-3-031-78804-8 [cite: 25] |
| **Seri White Paper** | *University of Oulu 6G Flagship White Paper Series* | 12 Laporan Publikasi Riset Utama 6G (Ketahanan, Vertikal, Arsitektur) [cite: 22, 26]. | `6gflagship.com/white-papers` [cite: 22] |
| **Kursus Spesialisasi** | *6G for a Connected Future Specialization* (Univ. of Glasgow) | Prinsip Konektivitas 6G, Komunikasi Nirkabel Masa Depan (Coursera) [cite: 23, 27]. | Platform Coursera [cite: 23, 27] |
| **Kurikulum Terbuka** | *MIT OpenCourseWare (OCW)* | Teori Sinyal & Sistem, Elektromagnetika Terapan, Teori Informasi [cite: 28]. | `ocw.mit.edu` [cite: 28] |
| **Software Simulator** | *NVIDIA Sionna & Sionna Research Kit* | Simulasi Link-Level / System-Level PHY Diferensial Berbasis Python [cite: 15, 16, 18]. | GitHub `NVlabs/sionna` [cite: 15, 18] |
| **Tumpukan Protokol** | *OpenAirInterface (OAI)* | Arsitektur Software RAN & Core Network 5G/6G Sumber Terbuka [cite: 14, 19]. | `openairinterface.org` [cite: 19] |

---

## 5. Kesimpulan dan Alur Langkah Pembelajaran

Penguasaan domain jaringan 6G memerlukan pemahaman terpadu yang menghubungkan regulasi internasional, prinsip fisika gelombang, serta implementasi perangkat lunak [cite: 1, 9, 16]. Rekomendasi ITU-R M.2160 dan agenda standardisasi 3GPP menyajikan batas-batas parameter teknis yang menjadi fondasi perancangan sistem [cite: 1, 4]. Pada tingkatan terendah, pemanfaatan spektrum Terahertz, elemen RIS, pemrosesan gelombang ISAC, serta penerima sinyal berbasis *Neural Receiver* mengubah fundamental cara informasi ditransmisikan dan diproses [cite: 9, 10, 12, 14].

Bagi praktisi maupun peneliti yang ingin menguasai disiplin ilmu ini secara bertahap, alur pembelajaran yang direkomendasikan dibagi ke dalam empat fase utama:

1.  **Fase Kerangka Kerja dan Regulasi**: Mengkaji dokumen awal seperti Rekomendasi ITU-R M.2160 dan laporan riset University of Oulu 6G Flagship untuk memahami visi tingkat tinggi, skenario penggunaan, dan KPI teknis [cite: 1, 2, 22].
2.  **Fase Matematika dan Fisika Lapisan Fisik**: Mempelajari pemodelan kanal THz, teori pergeseran fase RIS, formulasi ISAC, dan konsep dasar propagasi gelombang elektromagnetik melalui literatur akademik terstandar [cite: 8, 9, 10, 12].
3.  **Fase Simulasi Software Link-Level (Hands-on)**: Membangun skrip simulasi pemrosesan sinyal menggunakan pustaka Python NVIDIA Sionna untuk memahami operasi *Neural Receiver*, modulasi OFDM, dan mesin *ray tracing* Sionna RT [cite: 11, 16, 18].
4.  **Fase Prototyping Real-Time dan Sistem**: Mengintegrasikan algoritma fisik yang telah dilatih ke dalam tumpukan protokol *OpenAirInterface* menggunakan *Sionna Research Kit* dan perangkat keras SDR untuk menguji kinerja sistem pada kondisi jaringan nyata [cite: 14, 15, 19].

Dengan melintasi tahapan terstruktur ini, pemahaman komprehensif mengenai teknologi jaringan 6G dapat dibangun secara kokoh, menghubungkan teori konseptual dengan eksekusi teknis ter-akselerasi [cite: 1, 9, 15, 16].

---

1. Building the Foundation for Global 6G Standardization: A Deep Dive Into ITU-R IMT-2030 Requirements and Evaluation Guidelines - Samsung Research, [https://research.samsung.com/blog/Building-the-Foundation-for-Global-6G-Standardization-A-Deep-Dive-into-ITU-R-IMT-2030-Requirements-and-Evaluation-Guidelines](https://research.samsung.com/blog/Building-the-Foundation-for-Global-6G-Standardization-A-Deep-Dive-into-ITU-R-IMT-2030-Requirements-and-Evaluation-Guidelines)
2. Recommendation ITU-R M.2160-0 (11/2023) - Framework and overall objectives of the future development of IMT for 2030 and beyond, [https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.2160-0-202311-I!!PDF-E.pdf)
3. Overview of 6G (IMT-2030) | Digital Regulation Platform, [https://digitalregulation.org/overview-of-6g-imt-2030/](https://digitalregulation.org/overview-of-6g-imt-2030/)
4. IMT-2030: the ITU-R framework — 6G: Release 20 → 21, [https://www.cafetele.com/6g-book/read/ch02.html](https://www.cafetele.com/6g-book/read/ch02.html)
5. 6G Standardization Status: IMT-2030, 3GPP Releases, Timeline and Future Roadmap, [https://www.3glteinfo.com/6g/articles/6g-standardization-status/](https://www.3glteinfo.com/6g/articles/6g-standardization-status/)
6. IMT-2030: Technical requirements for the 6G future - ITU, [https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/](https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/)
7. ITU-R Update: IMT-2030 (6G - UNIDIR, [https://unidir.org/wp-content/uploads/2024/12/241211_ITU-R-Update-on-WRC-and-IMT-2030.pdf](https://unidir.org/wp-content/uploads/2024/12/241211_ITU-R-Update-on-WRC-and-IMT-2030.pdf)
8. 6G-Enabled Technologies for Next Generation: Fundamentals, Applications, Analysis and Challenges | Wiley, [https://www.wiley.com/en-us/6G-Enabled+Technologies+for+Next+Generation%3A+Fundamentals%2C+Applications%2C+Analysis+and+Challenges-p-9781394258338](https://www.wiley.com/en-us/6G-Enabled+Technologies+for+Next+Generation%3A+Fundamentals%2C+Applications%2C+Analysis+and+Challenges-p-9781394258338)
9. RIS-Assisted Terahertz Communications for 6G Networks: A Comprehensive Overview - IEEE Xplore, [https://ieeexplore.ieee.org/iel8/6287639/10820123/11016744.pdf](https://ieeexplore.ieee.org/iel8/6287639/10820123/11016744.pdf)
10. Terahertz-Band Integrated Sensing and Communications: Challenges and Opportunities - ORBilu, [https://orbilu.uni.lu/bitstream/10993/58263/1/p098_THZ_ISAC_v3.pdf](https://orbilu.uni.lu/bitstream/10993/58263/1/p098_THZ_ISAC_v3.pdf)
11. Sionna: An Open-Source Library for Next-Generation Physical Layer Research - arXiv, [https://arxiv.org/html/2203.11854v2](https://arxiv.org/html/2203.11854v2)
12. Reconfigurable Intelligent Surfaces for 6G and Beyond Wireless Networks | Wiley, [https://www.wiley.com/en-us/Reconfigurable+Intelligent+Surfaces+for+6G+and+Beyond+Wireless+Networks-p-9781394250141](https://www.wiley.com/en-us/Reconfigurable+Intelligent+Surfaces+for+6G+and+Beyond+Wireless+Networks-p-9781394250141)
13. Hello Sionna! A Demo of The First Open Source Library for Physical Layer Research, [https://www.youtube.com/watch?v=cYUNE4i4Q4E](https://www.youtube.com/watch?v=cYUNE4i4Q4E)
14. Tutorials — Sionna 2.2.0 - NVlabs, [https://nvlabs.github.io/sionna/rk/tutorials.html](https://nvlabs.github.io/sionna/rk/tutorials.html)
15. Powering AI-Native 6G Research with the NVIDIA Sionna Research Kit, [https://developer.nvidia.com/blog/powering-ai-native-6g-research-with-the-nvidia-sionna-research-kit/](https://developer.nvidia.com/blog/powering-ai-native-6g-research-with-the-nvidia-sionna-research-kit/)
16. Sionna - An Open-Source Library for 6G Research | NVIDIA Developer, [https://developer.nvidia.com/sionna](https://developer.nvidia.com/sionna)
17. Sionna Documentation - NVlabs, [https://nvlabs.github.io/sionna/index.html](https://nvlabs.github.io/sionna/index.html)
18. Sionna: An Open-Source Library for Research on Communication Systems - GitHub, [https://github.com/nvlabs/sionna](https://github.com/nvlabs/sionna)
19. Sionna Research Kit: A GPU-Accelerated Research Platform for AI-RAN - OpenAirInterface, [https://openairinterface.org/wp-content/uploads/2025/05/OAI-Kista-Workshop-NVIDIA.pdf](https://openairinterface.org/wp-content/uploads/2025/05/OAI-Kista-Workshop-NVIDIA.pdf)
20. Integrating Sionna RT in ns-3 for 6G Multi-Radio Access Technology (RAT) Networks Simulations - arXiv, [https://arxiv.org/html/2501.00372v2](https://arxiv.org/html/2501.00372v2)
21. Toward Digital Network Twins: Integrating Sionna RT in ns-3 for 6G Multi-RAT Networks Simulations - ResearchGate, [https://www.researchgate.net/publication/387671127_Toward_Digital_Network_Twins_Integrating_Sionna_RT_in_NS3_for_6G_Multi-RAT_Networks_Simulations](https://www.researchgate.net/publication/387671127_Toward_Digital_Network_Twins_Integrating_Sionna_RT_in_NS3_for_6G_Multi-RAT_Networks_Simulations)
22. 6G White Papers - 6G Flagship, [https://www.6gflagship.com/white-papers/](https://www.6gflagship.com/white-papers/)
23. 6G for a Connected Future Specialization - Coursera, [https://www.coursera.org/specializations/6g-for-a-connected-future](https://www.coursera.org/specializations/6g-for-a-connected-future)
24. 6G Security: New Frontiers in Mobile Network Technologies and Verticals | Wiley, [https://www.wiley.com/en-us/6G+Security%3A+New+Frontiers+in+Mobile+Network+Technologies+and+Verticals-p-00426725](https://www.wiley.com/en-us/6G+Security%3A+New+Frontiers+in+Mobile+Network+Technologies+and+Verticals-p-00426725)
25. Millimeter Wave and Terahertz Devices for 5G and 6G systems: Modern Design Aspects and Optimization - Google Books, [https://books.google.com/books/about/Millimeter_Wave_and_Terahertz_Devices_fo.html?id=4b960gEACAAJ](https://books.google.com/books/about/Millimeter_Wave_and_Terahertz_Devices_fo.html?id=4b960gEACAAJ)
26. 6G White Paper on Validation and Trials for Verticals towards 2030's, [https://www.6gflagship.com/6g-white-paper-on-validation-and-trials-for-verticals-towards-2030s/](https://www.6gflagship.com/6g-white-paper-on-validation-and-trials-for-verticals-towards-2030s/)
27. 10+ 6G Online Courses for 2026 | Explore Free Courses & Certifications | Class Central, [https://www.classcentral.com/subject/6g](https://www.classcentral.com/subject/6g)
28. Free Online Courses from MIT OCW | Open Learning, [https://openlearning.mit.edu/courses-programs/mit-opencourseware](https://openlearning.mit.edu/courses-programs/mit-opencourseware)
