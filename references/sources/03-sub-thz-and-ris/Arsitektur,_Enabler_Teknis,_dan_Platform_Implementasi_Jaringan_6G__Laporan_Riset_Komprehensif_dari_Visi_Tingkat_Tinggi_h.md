# Arsitektur, Enabler Teknis, dan Platform Implementasi Jaringan 6G_ Laporan Riset Komprehensif dari Visi Tingkat Tinggi hingga Eksekusi Lapisan Fisik

---

### Arsitektur, Enabler Teknis, dan Platform Implementasi Jaringan 6G: Laporan Riset Komprehensif dari Visi Tingkat Tinggi hingga Eksekusi Lapisan Fisik

#### Visi Strategis, Kerangka Kerja Global, dan Konsensus Industri IMT-2030

Perkembangan jaringan seluler generasi keenam (6G) menandai pergeseran paradigma dasar dalam rekayasa telekomunikasi, dari sekadar penyedia saluran transmisi data berkecepatan tinggi menjadi tatanan kecerdasan terdistribusi terpadu [cite: 1]. Ketika generasi kelima (5G) berfokus pada perluasan konektivitas pita lebar seluler ( _Enhanced Mobile Broadband_ / eMBB), komunikasi latensi rendah yang sangat andal ( _Ultra-Reliable Low-Latency Communication_ / URLLC), dan komunikasi mesin masif ( _Massive Machine-Type Communication_ / mMTC), jaringan 6G dirancang untuk menyatukan dunia fisik, digital, dan biologis melalui infrastruktur yang otonom dan berbasis kecerdasan buatan murni ( _AI-native_ ) [cite: 1, 2, 3].

##### Kerangka Utama dan Skenario Penggunaan ITU-R

Sektor Komunikasi Radio Organisasi Telekomunikasi Internasional ( _International Telecommunication Union Radiocommunication Sector_ / ITU-R) melalui kelompok pakar Working Party 5D telah merumuskan kerangka kerja global 6G yang dikenal sebagai IMT-2030 melalui Rekomendasi ITU-R M.2160 [cite: 2, 4]. Kerangka kerja ini memperluas skenario penggunaan klasik 5G menjadi enam skenario penggunaan utama yang mendefinisikan batas kapabilitas jaringan nirkabel masa depan [cite: 2]:

  1. _Immersive Communication_ (IC): Pengembangan langsung dari eMBB yang dirancang untuk memfasilitasi interaksi manusia-mesin berskala tinggi, mencakup telepresensi holografik multi-sensori, _Augmented Reality_ (AR) dan _Virtual Reality_ (VR) beresolusi ultra-tinggi, serta representasi _Digital Twin_ secara _real-time_ [cite: 1, 2, 3].
  2. _Hyper-Reliable and Low-Latency Communication_ (HRLLC): Evolusi dari URLLC yang menjamin latensi bidang pengguna ( _user plane latency_ ) hingga tingkat sub-milidetik dengan keandalan transmisi ekstrem untuk aplikasi kritis seperti operasi bedah jarak jauh, jaringan listrik cerdas ( _smart grid_ ), dan kendali otonom industri skala besar [cite: 2, 5].
  3. _Massive Communication_ (MC): Perluasan dari mMTC yang meningkatkan kerapatan koneksi perangkat Internet of Things (IoT) hingga puluhan juta perangkat per kilometer persegi dalam ekosistem kota cerdas dan manufaktur terotomatisasi [cite: 2].
  4. _Ubiquitous Connectivity_ (UC): Skenario baru yang bertujuan mengeliminasi area tanpa sinyal ( _blank spot_ ) secara global melalui integrasi penuh antara jaringan terestrial dan jaringan non-terestrial ( _Non-Terrestrial Networks_ / NTN), seperti satelit _Low Earth Orbit_ (LEO), sistem platform ketinggian tinggi ( _High-Altitude Platform Systems_ / HAPS), dan wahana udara tanpa awak ( _Unmanned Aerial Vehicles_ / UAV) [cite: 2, 3, 6].
  5. _Artificial Intelligence and Communication_ (AIAC): Skenario khusus yang memfasilitasi pertukaran data dan model antar-agen AI otonom, pelatihan pembelajaran mesin terdistribusi ( _Federated Learning_ ), serta koordinasi mesin-ke-mesin dengan prediktabilitas kinerja yang terverifikasi [cite: 1, 2, 7].
  6. _Integrated Sensing and Communication_ (ISAC): Konvergensi di mana gelombang radio komunikasi seluler dimanfaatkan secara simultan sebagai radar spasial untuk deteksi objek, pelacakan posisi presisi tinggi, pemetaan lingkungan tiga dimensi, dan penginderaan kondisi atmosfer [cite: 2, 8, 9]. Skenario penggunaan ini menuntut peningkatan signifikan pada seluruh Parameter Kinerja Utama ( _Key Performance Indicators_ / KPI) dibandingkan dengan teknologi 5G [cite: 2]. | Parameter Kinerja Utama (KPI) | IMT-2020 (5G) | IMT-2030 (6G) Target | | ------ | ------ | ------ | | Kecepatan Data Puncak ( _Peak Data Rate_ ) | $20 \text{ Gbps}$ [cite: 5] | $100 \text{ Gbps} - 1 \text{ Tbps}$ [cite: 2, 4] | | Kecepatan Data Pengalaman Pengguna | $100 \text{ Mbps}$ | $1 \text{ Gbps} - 10 \text{ Gbps}$ | | Latensi Bidang Pengguna ( _User Plane Latency_ ) | $1 \text{ ms}$ | $0.1 \text{ ms}$ (Sub-milidetik) [cite: 2, 5] | | Efisiensi Spektral ( _Spectral Efficiency_ ) | $1\times \text{ Baseline 5G}$ | $1.5\times - 3\times \text{ Efisiensi 5G}$ | | Keandalan Transmisi ( _Reliability_ ) | $99.999\%$ | $99.99999\%$ [cite: 5] | | Kerapatan Koneksi ( _Connection Density_ ) | $10^6 \text{ perangkat/km}^2$ | $10^7 \text{ perangkat/km}^2$ [cite: 2] | | Akurasi Posisi dan Penginderaan | $1 \text{ meter}$ | Akurasi Sentimeter hingga Milimeter [cite: 5] | | Efisiensi Energi Sistem | Baseline 2020 | $10\times - 100\times \text{ Lebih Efisien}$ [cite: 1, 5] |



##### Garis Waktu Standarisasi 3GPP dan Inisiatif Riset Global

Pengembangan standar teknis 6G berjalan melintasi tahapan terstruktur yang dikoordinasikan oleh organisasi Third Generation Partnership Project (3GPP) bersama badan standar internasional lainnya [cite: 10, 11]. Transisi ini dibangun secara gradual dari komersialisasi 5G Standalone (5G SA) dan 5G-Advanced menuju arsitektur 6G murni [cite: 1]:

  * Fase 5G-Advanced (2024–2027): 3GPP Release 18 dan Release 19 meletakkan fondasi awal untuk kecerdasan buatan pada lapisan akses radio, penginderaan gelombang radio, dan penyempurnaan jaringan non-terestrial [cite: 11, 12].
  * Spesifikasi Awal 6G (2027–2028): 3GPP Release 20 berfokus pada studi kelayakan arsitektur, yang dilanjutkan oleh Release 21 pada tahun 2028 untuk merumuskan spesifikasi teknis resmi pertama antarmuka udara ( _air interface_ ) 6G [cite: 10].
  * Uji Coba Lapangan dan Komersialisasi Awal (2029–2030): Uji coba lapangan luar ruang ( _outdoor field trials_ ) dan adopsi komersial awal oleh operator perintis di wilayah dengan kesiapan spektrum tinggi [cite: 10, 13].
  * Peluncuran Global Berskala Masif (2030 dan seterusnya): Peluncuran komersial penuh sistem 6G terstandarisasi secara global [cite: 10, 11, 13]. Konsensus teknis dan arah riset 6G dibentuk oleh berbagai konsorsium regional utama [cite: 10, 14]. Di Eropa, proyek flagship Hexa-X dan Hexa-X II yang dipimpin oleh Nokia dan Ericsson memelopori pengembangan arsitektur dasar dan enabler lapisan fisik [cite: 10, 13, 14]. Di Amerika Utara, Next G Alliance memimpin integrasi pasar dan kesiapan teknologi [cite: 10, 14, 15]. Sementara itu, IMT-2030 Promotion Group di Tiongkok, Bharat 6G Alliance di India, XG Mobile Promotion Forum (XGMF) di Jepang, serta strategi K-Network 2030 di Korea Selatan secara aktif melakukan riset alokasi spektrum dan pengujian prototipe [cite: 10, 13, 14].



* * *

#### Arsitektur Jaringan Inti dan Prinsip Desain Terdistribusi

##### AI-Native Fabric dan Otonomi Berbasis Intensi

Berbeda dari generasi sebelumnya yang menambahkan fungsi kecerdasan buatan secara terpisah di atas infrastruktur eksisting ( _AI-applied_ ), arsitektur 6G dirancang sejak awal berbasis AI murni ( _AI-Native_ ) [cite: 1, 13]. Dalam arsitektur ini, seluruh komponen jaringan bertindak sebagai elemen kognitif otonom yang secara kontinu mengamati kondisi lingkungan radio, mempelajari pola lalu lintas data, dan mengoptimalkan fungsi internalnya secara _real-time_ [cite: 1]. Pengelolaan dan pengoperasian jaringan mengadopsi mekanisme otonomi berbasis intensi ( _Intent-Based Autonomy_ ) [cite: 10]. Pengelola jaringan cukup mendefinisikan sasaran tingkat tinggi—seperti jaminan latensi untuk kendaraan otonom atau efisiensi energi maksimum di area pemukiman—dan arsitektur berbasis _RAN Intelligent Controller_ (RIC) serta agen AI terdistribusi akan menerjemahkan sasaran tersebut menjadi konfigurasi lapisan fisik, jadwal alokasi sumber daya, dan rute lalu lintas secara otomatis tanpa intervensi manual [cite: 1, 10, 16].

##### Integrasi Kontinuum Komputasi, Cloud, dan Konektivitas

Arsitektur inti jaringan 6G ( _Core Network_ ) berevolusi menuju platform _hybrid core_ yang menyatukan kapabilitas komputasi seluler, komputasi awan ( _cloud_ ), dan komputasi tepi ( _edge compute_ ) ke dalam satu tatanan terintegrasi ( _Compute-Cloud-Connectivity Continuum_ ) [cite: 1, 10]. Pemrosesan data, inferensi model ML, dan penyimpanan sementara tidak lagi terpusat di server utama, melainkan didistribusikan secara dinamis ke titik komputasi terdekat dari perangkat guna meminimalkan latensi pemrosesan dan menghemat bandwidth jaringan inti [cite: 1, 17]. Eksposur kapabilitas jaringan diwujudkan melalui _Network Application Programming Interfaces_ (APIs) yang terbuka dan terstandarisasi [cite: 1]. Melalui API ini, aplikasi pihak ketiga dapat meminta kustomisasi jaringan secara presisi, seperti pemesanan jaminan tingkat layanan ( _Service-Level Agreement_ / SLA) untuk bandwidth, sinkronisasi waktu akurasi mikrodetik, atau layanan penginderaan lokasi presisi tinggi [cite: 1].

##### Ketahanan Siber Kuantum dan Desain Keberlanjutan

Keamanan dalam arsitektur 6G dibangun atas prinsip _Security-by-Design_ [cite: 13]. Mengingat ancaman dekripsi masa depan yang dipicu oleh hadirnya komputer kuantum skala praktis, 6G mengintegrasikan kriptografi tahan kuantum ( _Post-Quantum Cryptography_ ) pada protokol pertukaran kunci dan enkripsi data [cite: 13, 18, 19]. Sistem otentikasi jaringan mengadopsi pendekatan _Zero Trust Architecture_ di mana setiap permintaan akses dari perangkat, fungsi jaringan, atau agen AI diperiksa secara berkelanjutan berdasarkan kredensial dinamis dan konteks keamanan [cite: 18, 19]. Dari sudut pandang keberlanjutan ( _Sustainability-by-Design_ ), sistem 6G menetapkan efisiensi energi sebagai batasan desain utama [cite: 2, 5, 13]. Operasi modulasi dan pemrosesan sinyal dirancang dengan konsep _lean design_ , yang memungkinkan elemen pemancar radio memasuki mode tidur ( _deep sleep mode_ ) mikrodetik saat tidak ada beban transmisi [cite: 1]. Penggunaan AI mendistribusikan konsumsi daya secara dinamis sesuai dengan permintaan trafik aktual sehingga mampu menekan jejak karbon total jaringan secara signifikan [cite: 1, 5].

* * *

#### Enabler Lapisan Fisik dan Radio Akses (Low-Level PHY)

##### Alokasi Spektrum: FR3 Centimeter-Wave dan Sub-THz

Pengoperasian radio akses 6G mengombinasikan tiga tingkatan pita spektrum elektromagnetik untuk menyeimbangkan kebutuhan cakupan area luas dan kapasitas bandwidth masif [cite: 1, 20]:

  1. Pita Frekuensi Rendah dan Menengah Eksisting (< 7 GHz): Spektrum 4G dan 5G yang dialokasikan ulang ( _spectrum refarming_ ) untuk mempertahankan cakupan dasar ( _coverage layer_ ) dan mendukung komunikasi mobilitas tinggi [cite: 1, 20].
  2. Pita Frekuensi Menengah Tinggi / FR3 (7 GHz – 24 GHz): Sering disebut sebagai pita _Centimeter-Wave_ (cm-Wave) atau _Upper Mid-Band_ . Pita spektrum FR3 menjadi wilayah krusial ( _sweet spot_ ) bagi 6G karena menawarkan keseimbangan optimal antara kapasitas bandwidth yang jauh lebih lebar dibandingkan pita sub-6 GHz dan karakteristik propagasi gelombang yang masih dapat menjangkau area makro seluler [cite: 1, 9, 14].
  3. Pita Sub-Terahertz dan Terahertz (100 GHz – 3 THz): Spektrum frekuensi sangat tinggi untuk menyediakan bandwidth berkelanjutan hingga belasan Gigahertz [cite: 3, 5, 21]. Gelombang Sub-THz sangat rentan terhadap rugi-rugi jalur ( _path loss_ ) akibat penyerapan atmosferik dan penghalangan fisik, sehingga ditargetkan untuk komunikasi jarak dekat ( _short-range ultra-high data rate links_ ), _wireless backhaul/fronthaul_ , serta aplikasi penginderaan presisi ekstrem [cite: 4, 8, 21].



##### Rekayasa Bentuk Gelombang, SCS Ekstrem, dan Modulasi 4096-QAM

Guna mengatasi tantangan propagasi pada frekuensi tinggi, antarmuka udara lapisan fisik ( _Physical Layer_ / PHY) 6G mengadaptasi rekayasa bentuk gelombang ( _waveform_ ) berkinerja tinggi [cite: 4, 8, 21]. Pada transmisi OFDM konvensional, penambahan frekuensi pembawa ( _carrier frequency_ ) meningkatkan efek _phase noise_ dan _Doppler shift_ secara eksponensial. 6G mengatasi masalah ini dengan memperluas Spasi Subpembawa ( _Subcarrier Spacing_ / SCS) melampaui batas maksimum 5G NR ( $960 \text{ kHz}$ ) [cite: 4]. Spasi subpembawa dalam sistem berbasis OFDM dihitung dengan persamaan numerologi: $$SCS = 15 \times 2^\mu \text{ kHz}$$ Pada 6G, indeks numerologi $\mu$ ditingkatkan hingga nilai $\mu = 7$ atau $\mu = 8$ , yang menghasilkan spasi subpembawa $SCS = 1920 \text{ kHz}$ dan $SCS = 3840 \text{ kHz}$ [cite: 4]. Peningkatan SCS membuat durasi simbol OFDM menjadi sangat pendek, yang secara langsung memangkas latensi transmisi fisik sekaligus meningkatkan ketahanan sistem terhadap _phase noise_ pada pita Sub-THz [cite: 4]. Di sisi modulasi, untuk kondisi saluran dengan rasio sinyal terhadap derau ( _Signal-to-Noise Ratio_ / SNR) yang tinggi, 6G memperkenalkan skema modulasi tingkat tinggi hingga 4096-QAM ( _Quadrature Amplitude Modulation_ ) [cite: 4]. Modulasi 4096-QAM mampu memetakan 12 bit informasi ke dalam satu simbol konstelasi ( $2^{12} = 4096$ ), yang meningkatkan efisiensi spektral secara drastis dibandingkan 256-QAM ( $8 \text{ bit/simbol}$ ) pada 5G [cite: 4]. Selain variasi OFDM, skema modulasi _Orthogonal Time Frequency Space_ (OTFS) dievaluasi sebagai kandidat kuat bentuk gelombang 6G untuk skenario mobilitas sangat tinggi karena kemampuannya memetakan simbol informasi pada domain _Delay-Doppler_ alih-alih domain _Time-Frequency_ konvensional [cite: 8].

##### Topologi Multi-Antena Advanced: Cell-Free Massive MIMO dan RIS

Untuk memaksimalkan efisiensi spektral dan mengatasi pelemahan sinyal pada frekuensi cm-Wave/Sub-THz, 6G mentransformasikan arsitektur antena pemancar melalui dua teknologi utama [cite: 3, 22]:

  1. _Cell-Free Massive MIMO_ : Konsep seluler tradisional berbasis batas wilayah sel ( _cell-centric_ ) dihilangkan dan digantikan oleh pendekatan yang berpusat pada pengguna ( _user-centric_ ) [cite: 9, 22]. Ratusan _Access Points_ (AP) berukuran kecil disebar di suatu kawasan dan dihubungkan secara kooperatif melalui jaringan _backhaul_ . Seluruh AP melayani setiap perangkat pengguna secara bersamaan tanpa batasan _handover_ , yang menghasilkan pemrosesan sinyal koheren dan menghilangkan interfersi antar-sel pada area batas sel [cite: 9, 22].
  2. _Reconfigurable Intelligent Surfaces_ (RIS / IRS): RIS adalah permukaan planar metamaterial buatan yang terdiri dari ribuan elemen reflektif pasif yang fase dan amplitudonya dapat dikontrol secara elektronik melalui sinyal kendali digital [cite: 3, 8, 21]. Ketika sinyal gelombang millimeter atau Sub-THz terhalang oleh gedung atau dinding, RIS secara dinamis mengarahkan refleksigelombang radio menuju perangkat penerima, sehingga menciptakan jalur propagasi baru ( _Line-of-Sight_ buatan) dan menyelesaikan masalah _blockage_ pada frekuensi tinggi [cite: 8, 21].



##### Integrated Sensing and Communication (ISAC)

Dalam sistem ISAC, bentuk gelombang radio dirancang secara terpadu ( _Dual-Function Radar-Communication_ / DFRC) untuk menjalankan dua fungsi secara bersamaan menggunakan spektrum dan perangkat keras yang sama [cite: 2, 8, 9]. Fungsi komunikasi bertugas mengirimkan bit data terenkripsi ke penerima target melalui teknik demodulasi data standar, sementara fungsi penginderaan memanfaatkan pantulan gelombang ( _echo signal_ ) yang memantul dari objek di sekitarnya untuk mengekstrak informasi fisik lingkungan [cite: 8]. Dengan memproses sinyal pantulan menggunakan algoritma pemrosesan radar terdistribusi, jaringan 6G dapat menghitung jarak objek ( $R$ ) dan kecepatan radial ( $v$ ) berdasarkan estimasi penundaan waktu ( _time delay_ $\tau$ ) dan pergeseran Doppler ( $f_d$ ): $$R = \frac{c \tau}{2}, \quad v = \frac{\lambda f_d}{2}$$ Di mana $c$ adalah kecepatan cahaya dan $\lambda$ adalah panjang gelombang sinyal. Kemampuan ISAC memfasilitasi pelacakan posisi presisi tinggi hingga tingkat sentimeter dan milimeter tanpa membutuhkan modul GPS eksternal [cite: 2, 5].

##### Arsitektur AI-Native Air Interface dan Neural Receiver

Salah satu terobosan fundamental pada lapisan fisik 6G adalah penggantian blok pemrosesan sinyal tradisional di sisi penerima ( _receiver chain_ ) dengan jaringan saraf tiruan terkomputasi ( _Neural Receiver_ ) [cite: 16, 23, 24]. Pada penerima klasik, proses penerimaan sinyal dibagi menjadi modul-modul independen yang terpisah: estimasi saluran ( _channel estimation_ ), ekualisasi ( _equalization_ ), dan demapping simbol ( _symbol demapping_ ). Pendekatan terpisah ini berpotensi menimbulkan akumulasi eror antar-blok. _Neural Receiver_ mengintegrasikan seluruh fungsi tersebut ke dalam satu arsitektur _Deep Learning_ tunggal (seperti arsitektur Residual Network / ResNet atau Fully Convolutional Network) [cite: 16, 24]. Penerima menerima masukan berupa kisi-kisi sumber daya ( _resource grid_ ) pasca-DFT dan secara langsung menghasilkan nilai _Log-Likelihood Ratios_ (LLRs) untuk bit-bit terkode yang kemudian diteruskan ke blok _decoder_ LDPC [cite: 24]. Proses pelatihan _Neural Receiver_ dilakukan secara _end-to-end_ menggunakan kerangka kerja diferensiasi otomatis ( _differentiable system_ ) [cite: 24, 25]. Kerugian pelatihan ( _loss function_ ) dihitung berdasarkan fungsi _Binary Cross-Entropy_ (BCE) antara bit yang ditransmisikan $c$ dan nilai LLR $\hat{L}$ yang dihasilkan penerima [cite: 24]: $$\mathcal{L}_{BCE} = -\frac{1}{N} \sum_{i=1}^{N} \left[ c_i \log \sigma(\hat{L}_i) + (1 - c_i) \log (1 - \sigma(\hat{L}_i)) \right]$$ Penggunaan _Neural Receiver_ terbukti secara eksperimental mampu memberikan perbaikan rasio kesalahan bit ( _Bit Error Rate_ / BER) yang signifikan pada saluran nirkabel non-linear yang kompleks di mana model matematis konvensional gagal memetakan kerugian sinyal secara akurat [cite: 23, 24].

* * *

#### Panduan Implementasi Hands-On dan Platform Simulasi 6G

Untuk melakukan riset dan eksperimen praktis teknologi 6G tanpa memerlukan perangkat keras laboratorium bernilai tinggi, peneliti dan insinyur mengandalkan pustaka simulasi terdistribusi tingkat lanjut [cite: 21, 25, 26]. Dua platform utama yang paling banyak digunakan di industri dan akademisi saat ini adalah **NVIDIA Sionna** dan **MATLAB 6G Exploration Library** [cite: 8, 21, 25, 26].

##### Ekosistem NVIDIA Sionna

NVIDIA Sionna adalah pustaka sumber terbuka ( _open-source_ ) berbasis Python yang dirancang khusus untuk riset lapisan fisik nirkabel 6G [cite: 3, 25, 26]. Keunggulan utama Sionna terletak pada integrasi arsitektur diferensiasi otomatis ( _differentiable framework_ ) berbasis PyTorch dan TensorFlow yang berjalan di atas akselerasi GPU NVIDIA [cite: 23, 25, 27, 28]. Arsitektur Sionna terbagi menjadi tiga modul inti [cite: 27, 28]:

  * sionna.phy: Simulator tingkat tautan ( _link-level_ ) yang mencakup modulasi, pengkodean saluran (LDPC, Polar), pemetaan ruang-waktu, dan pemrosesan sinyal MIMO [cite: 27, 28].
  * sionna.rt: Engine _ray tracing_ berdiri sendiri yang berjalan sangat cepat menggunakan Mitsuba 3 dan Dr.Jit untuk memodelkan propagasi gelombang radio 3D yang realistis berdasarkan geometri lingkungan asli [cite: 26, 27, 28].
  * sionna.sys: Simulator tingkat sistem ( _system-level_ ) yang diabstraksikan dari lapisan fisik untuk menguji alokasi sumber daya dan penjadwalan jaringan [cite: 27, 28]. Melalui modul _Sionna Research Kit_ (SRK), algoritma AI yang dilatih dalam pustaka Sionna dapat langsung disetorkan ke dalam tumpukan protokol _Software-Defined Radio_ (SDR) bertingkat nyata seperti OpenAirInterface (OAI) menggunakan kerangka kerja NVIDIA TensorRT [cite: 16, 27, 29].



##### Kapabilitas MATLAB 6G Exploration Library

MathWorks menyediakan **6G Exploration Library** sebagai pustaka ekstensi resmi untuk _5G Toolbox_ di MATLAB [cite: 8, 9, 30]. Pustaka ini memfasilitasi eksplorasi kandidat bentuk gelombang 6G yang melampaui batasan standar 5G NR [cite: 8, 9, 21]. Fitur kunci dari pustaka ini mencakup konfigurasi carrier kustom (pre6GCarrierConfig) yang memungkinkan penetapan spasi subpembawa $SCS > 960 \text{ kHz}$ (seperti $1920 \text{ kHz}$ dan $3840 \text{ kHz}$ ) serta jumlah blok sumber daya ( _Resource Blocks_ / RB) melebihi batas 275 RB [cite: 4]. Pustaka ini juga mendukung modulasi tingkat tinggi hingga 4096-QAM, pemodelan impairment RF Sub-THz (seperti _phase noise_ dan ketidaklinearan _power amplifier_ ), serta simulasi kanal RIS dan ISAC [cite: 4, 8, 9, 30].

Fitur / Parameter| NVIDIA Sionna| MATLAB 6G Exploration Library| GNU Radio| OpenAirInterface (OAI)  
---|---|---|---|---  
**Bahasa Pemrograman**|  Python (PyTorch / TensorFlow) [cite: 23, 25, 28]| MATLAB Script / Live Script [cite: 4, 9]| C++ / Python [cite: 31]| C / C++  
**Akselerasi GPU Native**|  Sangat Tinggi (CUDA / TensorRT) [cite: 23, 25, 26]| Terbatas (Parallel Computing Toolbox) [cite: 8, 32]| Terbatas| Terbatas  
**Differentiable (Native AI)**|  Ya (Diferensiasi End-to-End) [cite: 25, 27]| Integrasi Eksternal (PyTorch Import) [cite: 9]| Tidak| Tidak  
**Fokus Utama Pemodelan**|  PHY Link-Level, Ray Tracing, AI-RAN [cite: 26, 27]| PHY Link-Level, Impairment RF, ISAC [cite: 8, 9, 21]| Pemrosesan Sinyal SDR General [cite: 31]| Tumpukan Protokol RAN & Core Lengkap [cite: 16]  
**Kemudahan Penggunaan**|  Menengah (Memerlukan pemahaman ML)| Sangat Tinggi (API & GUI Siap Pakai) [cite: 8, 25]| Menengah| Kompleks  
  
##### Alur Kerja Praktis dan Prosedur Hands-On

Untuk memfasilitasi pembelajaran praktis secara bertahap dari tingkat pemula hingga tingkat lanjut, eksperimen simulasi dikelompokkan ke dalam tiga alur kerja utama:

###### Alur Kerja 1: Konfigurasi Numerologi Ekstrem pada MATLAB

Langkah awal dapat dimulai dengan memanfaatkan _6G Exploration Library for 5G Toolbox_ untuk mensimulasikan gelombang OFDM berkecepatan tinggi [cite: 4, 8, 30]. Pengguna pertama-tama mengunduh dan menginstal add-on pustaka 6G [cite: 30, 32]. Selanjutnya, objek pembawa pre6GCarrierConfig diinisialisasi dengan menetapkan properti SubcarrierSpacing = 1920 dan alokasi blok sumber daya yang diperluas [cite: 4]. Properti modulasi pada objek pre6GPhysicalChannelConfig dikonfigurasi ke nilai '4096QAM' [cite: 4]. Sinyal kemudian dibentuk menggunakan pre6GResourceGrid dan dimodulasi melalui pre6GOFDMModulate [cite: 4]. Efek ketidaksempurnaan perangkat keras ( _hardware impairments_ ) pada frekuensi Sub-THz—seperti derau fase ( _phase noise_ ) Hexa-X dan distorsi daya amplifier—dievaluasi dengan mengukur peningatan nilai _Error Vector Magnitude_ (EVM) dan _Adjacent Channel Power Ratio_ (ACPR) pada penganalisis spektrum [cite: 4, 8, 30].

###### Alur Kerja 2: Pelatihan Neural Receiver pada NVIDIA Sionna

Eksperimen tingkat lanjut dilakukan di lingkungan Python menggunakan pustaka Sionna untuk melatih penerima sinyal berbasis AI [cite: 24, 28]. Setelah menginstal pustaka via pip install sionna, pengguna mendefinisikan objek ResourceGrid yang menentukan jumlah simbol OFDM, spasi subpembawa, serta alokasi pola pilot [cite: 24, 28]. Modul saluran nirkabel dibangun menggunakan sionna.phy.channel untuk mensimulasikan kanal fading Rayleigh multipath [cite: 24, 27]. Arsitektur _Neural Receiver_ dibangun menggunakan modul torch.nn.Module yang mengintegrasikan lapisan Convolutional 2D dan Residual Blocks [cite: 24]. Dalam loop pelatihan ( _training loop_ ), sebuah batch data terbit diumpankan ke pemancar, dilewatkan melalui saluran nirkabel bertingkat SNR acak ( $E_b/N_0$ ), dan diproses oleh _Neural Receiver_ untuk menghasilkan perkiraan LLR [cite: 24]. Pengoptimasi torch.optim.Adam mengeksekusi propagasi balik ( _backpropagation_ ) untuk meminimalkan fungsi kerugian binary_cross_entropy_with_logits secara otomatis [cite: 24].

###### Alur Kerja 3: Pemodelan Propagasi Spasial 3D dengan Sionna Ray Tracer

Pemodelan gelombang radio pada lingkungan fisik nyata dilakukan dengan memuat file geometri 3D area perkotaan ke dalam modul sionna.rt.Scene [cite: 27]. Properti material permukaan dinding dan bangunan dikonfigurasi dengan konstanta dielektrik kompleks yang sesuai untuk frekuensi cm-Wave/Sub-THz [cite: 26, 27]. Setelah menetapkan posisi spasial koordinat 3D untuk pemancar Base Station dan penerima pengguna, fungsi scene.compute_paths() dieksekusi untuk menghitung lintasan refleksi, difraksi, dan hamburan sinyal gelombang radio secara presisi [cite: 26, 27]. Hasil pemetaan sinyal ( _coverage map_ ) dan matriks saluran ( $H$ ) diekstrak untuk menganalisis performa _beamforming_ dan potensi hambatan sinyal ( _blockage_ ) [cite: 8, 26, 27].

* * *

#### Peta Literatur Akademik, Buku Teks, dan Kurikulum Belajar Mandiri

##### Literatur Akademik Utama dan Buku Teks Standar

Untuk membangun pemahaman teknis yang kokoh, peneliti dan praktisi disarankan merujuk pada buku teks standar dan dokumen putih ( _whitepapers_ ) terverifikasi yang diterbitkan oleh penerbit internasional utama [cite: 7, 19, 22, 33]:

  * **6G-Enabled Technologies for Next Generation: Fundamentals, Applications, Analysis and Challenges** (Wiley-IEEE Press, 2025; Amit Kumar Tyagi et al.): Buku teks komprehensif yang membahas arsitektur dasar 6G, teknologi jaringan nirkabel, enkripsi tahan kuantum, pemotongan jaringan ( _network slicing_ ), dan implementasi IoT [cite: 18, 19].
  * **6G Key Technologies: A Comprehensive Guide** (Wiley-IEEE Press, 2022; Wei Jiang & Fa-Long Luo): Panduan teknis mendalam mengenai antarmuka udara baru, Cell-Free Massive MIMO, Reconfigurable Intelligent Surface (RIS), serta skema modulasi non-ortogonal [cite: 22].
  * **Artificial Intelligence in the 6G Ecosystem** (Springer Nature, 2026): Buku teks fokus yang mengulas sinergi antara teknik pembelajaran mesin (Supervised, Unsupervised, Reinforcement Learning, Deep Learning) dengan Open RAN dan desain lapisan fisik 6G [cite: 33].
  * **Information Theory, Mathematical Optimization, and Their Crossroads in 6G System Design** (Springer, 2023; Shih-Chun Lin et al.): Monograf matematis mendalam yang membahas teori informasi jaringan, penginderaan sekuensial terdistribusi, dan pemrograman matematik untuk optimasi sistem 6G [cite: 7, 34].
  * **Seri White Paper 6G Flagship Universitas Oulu & Proyek Hexa-X** : Seri dokumen putih industri terbuka yang memberikan panduan terperinci mengenai spektrum Sub-THz, lokalisasi, penginderaan, dan arsitektur otonom [cite: 4, 10, 35, 36].



##### Kurikulum Pembelajaran Mandiri Bertahap

Untuk menguasai domain 6G secara bertahap, alur pembelajaran dipetakan ke dalam empat tingkatan kurikulum:

  1. Tingkat 1 (Fondasi Telekomunikasi dan Pemrosesan Sinyal Dasar): Mempelajari Teori Informasi Shannon, Modulasi Digital (QAM, OFDM), Pemrosesan Sinyal Vektor/Matriks, dan Propagasi Radio Gelombang Mikro. Target kapabilitas adalah mampu menghitung kapasitas saluran secara teoretis dan mensimulasikan rantai transceiver OFDM dasar.
  2. Tingkat 2 (Arsitektur 5G Advanced dan Ketersediaan Alat Simulasi): Mempelajari Arsitektur 5G NR (Release 15-17), Standar O-RAN (Open RAN), Kerangka Kerja ITU IMT-2030, serta Pengenalan Pustaka Sionna/MATLAB 5G Toolbox [cite: 2, 9, 11, 33]. Target kapabilitas adalah mampu menjalankan simulasi tingkat tautan 5G NR dan mengonfigurasi kisi sumber daya [cite: 9].
  3. Tingkat 3 (Enabler Lapisan Fisik 6G): Mempelajari Spektrum Sub-THz & FR3, Rekayasa Spasi Subpembawa ( $SCS > 960 \text{ kHz}$ ), Arsitektur RIS, Cell-Free Massive MIMO, dan ISAC [cite: 3, 4, 8, 22]. Target kapabilitas adalah mampu merancang skenario simulasi RIS pada MATLAB dan menganalisis efek _phase noise_ frekuensi tinggi [cite: 4, 8].
  4. Tingkat 4 (Pemodelan Praktis dan Deep Learning Telekomunikasi): Mempelajari Desain dan Pelatihan _Neural Receiver_ , Pemodelan Propagasi 3D Ray Tracing, Otonomi Jaringan Berbasis RIC/xApps, dan Deploy Model via TensorRT [cite: 16, 24, 26]. Target kapabilitas adalah mampu melatih model _Neural Receiver_ end-to-end secara mandiri menggunakan NVIDIA Sionna serta memvalidasi performa jaringan di lingkungan nirkabel realistis [cite: 23, 24, 25].



* * *

#### Kesimpulan dan Implikasi Strategis

Jaringan 6G merepresentasikan konvergensi mendalam antara rekayasa nirkabel, kecerdasan buatan terdistribusi, pemrosesan sinyal spasial, dan komputasi awan [cite: 1]. Pergeseran arsitektur menuju _AI-Native Fabric_ menuntut perubahan mendasar pada cara sistem komunikasi dirancang, di mana fungsi pemrosesan sinyal lapisan fisik dikembangkan secara diferensial berbasis _Deep Learning_ [cite: 1, 24, 25]. Penguasaan domain 6G membutuhkan keseimbangan konseptual antara pemahaman fondasi matematis (teori informasi, propagasi Sub-THz, dan pemrosesan radar ISAC) serta pemahaman praktis dalam mengoperasikan kerangka kerja simulasi modern seperti NVIDIA Sionna dan MATLAB 6G Exploration Library [cite: 7, 8, 25]. Keberadaan alat simulasi berbasis GPU ini memberikan kesempatan bagi para peneliti dan praktisi untuk mengeksplorasi, mensimulasikan, dan mevalidasi inovasi teknologi nirkabel masa depan secara mandiri sebelum implementasi standar komersialisasi penuh terwujud pada dekade 2030-an [cite: 10, 25].

* * *

  1. 6G – connectivity and beyond for the 2030s - Ericsson, <https://www.ericsson.com/en/reports-and-papers/white-papers/6g-connectivity-and-beyond-for-the-2030s>
  2. IMT-2030: Technical requirements for the 6G future - ITU, <https://www.itu.int/hub/2026/03/imt-2030-technical-requirements-for-the-6g-future/>
  3. Sionna: An Open-Source Library for Next-Generation Physical Layer Research - arXiv, <https://arxiv.org/pdf/2203.11854>
  4. Get Started with 6G Exploration Library - MATLAB & Simulink - MathWorks, <https://www.mathworks.com/help/5g/ug/get-started-with-6g-exploration-library.html>
  5. 6G Technology - C4IR Saudi Arabia, <https://www.c4irsaudiarabia.org/docs/6G%20Technology.pdf>
  6. Explore 6G technology with MATLAB - YouTube, <https://www.youtube.com/watch?v=9aC720BLlTA>
  7. Information Theory, Mathematical Optimization, and Their Crossroads in 6G System Design, <https://www.springerprofessional.de/en/information-theory-mathematical-optimization-and-their-crossroad/23510264>
  8. 6G Exploration Library - MATLAB & Simulink - MathWorks, <https://www.mathworks.com/products/6g-exploration-library.html>
  9. 6G Exploration Library - MATLAB & Simulink - MathWorks, <https://www.mathworks.com/help/5g/6g-exploration-library.html>
  10. 6G - Follow the journey to the next generation networks - Ericsson, <https://www.ericsson.com/en/6g>
  11. 6G: The Intelligent Network of Everything - A Comprehensive Vision, Survey, and Tutorial, <https://arxiv.org/html/2407.09398v1>
  12. Exploring 6G with MATLAB - MathWorks, <https://www.mathworks.com/campaigns/offers/exploring-6g-with-matlab.html>
  13. Charting the path to 6G | Nokia.com, <https://www.nokia.com/6g/>
  14. Overview of 6G (IMT-2030) | Digital Regulation Platform, <https://digitalregulation.org/overview-of-6g-imt-2030/>
  15. 5G Americas Studies 6G Vision Outlined by ITU Framework, <https://www.5gamericas.org/5g-americas-studies-6g-vision-outlined-by-itu-framework/>
  16. Tutorials — Sionna 2.2.0 - NVlabs, <https://nvlabs.github.io/sionna/rk/tutorials.html>
  17. Edge Learning for 6G-Enabled Internet of Things - Apple Academic Press, <https://www.appleacademicpress.com/edge-learning-for-6g-enabled-internet-of-things-challenges-threats-and-opportunities/9781779644213>
  18. 6G-Enabled Technologies for Next Generation: Fundamentals, Applications, Analysis and Challenges - Google Books, <https://books.google.com/books/about/6G_Enabled_Technologies_for_Next_Generat.html?id=O1k4EQAAQBAJ>
  19. 6G-Enabled Technologies for Next Generation: Fundamentals, Applications, Analysis and Challenges | Wiley, <https://www.wiley.com/en-us/6G-Enabled+Technologies+for+Next+Generation%3A+Fundamentals%2C+Applications%2C+Analysis+and+Challenges-p-9781394258338>
  20. White Paper on The EUROPEAN VISION For The 6G NETWORK ECOSYSTEM, <https://6g-ia.eu/wp-content/uploads/2024/12/6g-ia-vision-white-paper-v2.0.pdf>
  21. MATLAB Library Simulates 6G Technology - Microwaves & RF, <https://www.mwrf.com/technologies/embedded/software/article/55088732/microwaves-rf-mathworks-matlab-gets-a-6g-library-to-help-simulate-advanced-communications>
  22. 6G Key Technologies: A Comprehensive Guide | Wiley, <https://www.wiley.com/en-us/6G+Key+Technologies%3A+A+Comprehensive+Guide-p-00361132>
  23. NVIDIA Sionna: An AI-Native 6G Wireless System Design Tool - Techplayon, <https://www.techplayon.com/nvidia-sionna-an-ai-native-6g-wireless-system-design-tool/>
  24. sionna/tutorials/phy/Neural_Receiver.ipynb at main - GitHub, <https://github.com/NVlabs/sionna/blob/main/tutorials/phy/Neural_Receiver.ipynb>
  25. Sionna - An Open-Source Library for 6G Research | NVIDIA Developer, <https://developer.nvidia.com/sionna>
  26. 2026 NVIDIA Sionna (6G) & AI Projects - Projectsatbangalore, <https://www.projectsatbangalore.com/nvidia-projects-for-students/>
  27. Sionna Documentation - NVlabs, <https://nvlabs.github.io/sionna/index.html>
  28. Sionna: An Open-Source Library for Research on Communication Systems - GitHub, <https://github.com/nvlabs/sionna>
  29. Powering AI-Native 6G Research with the NVIDIA Sionna Research Kit, <https://developer.nvidia.com/blog/powering-ai-native-6g-research-with-the-nvidia-sionna-research-kit/>
  30. 6G Exploration Library for 5G Toolbox - File Exchange - MATLAB Central - MathWorks, <https://www.mathworks.com/matlabcentral/fileexchange/157771-6g-exploration-library-for-5g-toolbox>
  31. GitHub - gnuradio/gnuradio: GNU Radio – the Free and Open Software Radio Ecosystem, <https://github.com/gnuradio/gnuradio>
  32. Get Started with 6G Exploration Library - MathWorks, <https://www.mathworks.com/help/5g/get-started-with-6g-exploration-library.html>
  33. Artificial Intelligence in the 6G Ecosystem - VTT's Research Information Portal, <https://cris.vtt.fi/en/publications/artificial-intelligence-in-the-6g-ecosystem/>
  34. Information Theory, Mathematical Optimization, and Their Crossroads in 6G System Design (Springer Series in Wireless Technology) - Kinokuniya USA, <https://usa.kinokuniya.com/products/9789811920158>
  35. 6G WHITE PAPER ON LOCALIZATION AND SENSING - Barkhausen Institut, <https://www.barkhauseninstitut.org/fileadmin/user_upload/Publikationen/2020/delima_2020_6gwhitepaper.pdf>
  36. 6G Vision, Value, Use Cases and Technologies from European 6G Flagship Project Hexa-X - research.chalmers.se, <https://research.chalmers.se/publication/527418/file/527418_Fulltext.pdf>


