Buka web https://ayo.co.id dan coba pelajari. Menurut anda bagian mana yang perlu untuk
dilakukan pengujian dan kira-kira mekanisme pengujian apa yang sesuai?

Karena AYO adalah Platform yang menghubungkan para penggiat olah raga satu dengan lainnya serta platform olahraga yang memiliki fitur booking, pembayaran, komunitas, kompetisi, dan manajemen venue
maka berdasarkan pendapat dan pengalaman saya hal yang perlu di uji adalah berdasarkan tingkat urgensi dan risk seperti bagian yang berdapak dengan pendapatan dan user experience
1. Bagian Booking Lapangan
    - Test yang di perlukan adalah FUNCTIONALITY TESTING
    - Test berdasarkan USER FLOW mulai dari Cari venue, Pilih tanggal,Pilih jam,Pilih durasi, Booking, Bayar, Booking terkonfirmasi
    - Mengecek waktu booking dengan memberikan input POSITIVE atau NEGATIVE
        - Positive contohnya memilih waktu yang available
        - Negative contohnya ketika booking mendekati waktu yang tertera atau booking ketika / bertepatan dengan jadwal yang ada
    - Test ketika ada 2 user yang booking 1 tempat jam waktu dan tanggal yang sama
    - Test ketika 1 user mencoba booking dari beberapa browser atau device berbeda menggunakan 1 akun
2. Bagian Pembayaran
    - Test yang dilakukan adalah menggunakan positive flow dan memastikan bahwa pembayaran valid dan booking diterima dan berstatus terbayar
    - Test menggunakan flow negative bisa dengan contoh user menggunakan pembayaran invalid atau jumlah currency yang di gunakan tidak sama, maka pembayaran akan gagal
    - Selain itu testing yang dilakukan bisa dengan cara EDGE SCENARIO dimana user melakukan pending pembayaran dalam kurun waktu tertentu atau merestart browser yang digunakan untuk mengakali pembayaran
3. Bagian Search atau Filter
    - Bagian ini juga salah satu yang penting dimana fitur ini mempermudah user untuk mencari tempat atau lapangan yang di kehendaki secara cepat dan efisien
    - Test bisa dilakukan secara FUNCTIONAL TEST untuk melihat bahwa fitur bisa berjalan secara normal
    - Test ketika user memberikan input yang tidak di ijinkan seperti spesial charater #%^ dll
    - Test menggunakan long character atau kalimat/kata panjang melebihi yang di ijinkan
4. Bagian Login dan Pendaftaran
    - Pada bagian ini saya akan mencoba untuk test normal/positive flow untuk memastikan fitur berjalan normal
    - Kemudian akan melakukan VALIDATION TESTING ketika user login/register dengan email invalid/valid, mengkosongkan email/password
    - Serta edge case lainya seperti halnya register mengguunakan email testing pada PRODUCTION site
    - Test untuk mengecek validasi ketika user salah memberikan input password/email secara terus menerus melebih batas
    - Test dengan beberapa device/browser menggunakan akun yang sama
5. API Testing
    - Test untuk validasi tiap endpoint seperti untuk register/login check apakah respon yang diberikan pass atau failed ketika menggunakan data valid/invalid
    - Test untuk melihat perubahan data ketika user mengupdate parameter pada endpoint akan tertampil pada website
6. Test dari segi Performance dan web responsive
    - Test web responsive ketika website dibuka pada device lain seperti Handphone/tablet bahkan variasi layar komputer
    - Test performance dapat dilakukan untuk melihat performa website ketika contohnya ada 100 user login/mendaftar/booking secara bersama
7. Exploratory test
    - Pada test ini tidak mengacu ke test case melainkan test secara acak, bisa berdasarkan pengalaman penguji/QA dalam mengerjakan projek sebelumnya, test ini juga bisa bertujuan mendapatkan bug diluar test case yang di buat

===============================================================================================================================================================================

Buka aplikasi AYO baik di playstore/appstore dan coba pelajari. Menurut anda bagian mana yang
perlu untuk dilakukan pengujian dan kira-kira mekanisme pengujian apa yang sesuai?

Pada dasarnya testing pada web maupun aplikasi mobile sama, namun ada sedikit tambahan khususnya ketika ada beberapa fitur yang tersedia khusus mobile
1. Background & Foreground Testing
    - Test ketika user pada halaman booking pada waktu payment mencoba membuka aplikasi lain
    - Test ketika user sedang pada halaman booking pada waktu payment user coba untuk meminimize aplikasi AYO
2. Network Interruption 
    - Test ini bertujuan menguji ketika aplikasi kehilangan koneksi baik dari mobile data atau pun wifi connection pada saat saat tertentu seperti ketika proses payment berlangsung user mencoba mematikan koneksi data
3. Testing Compatibility
    - Test bertujuan untuk melihat performa atau UI aplikasi apakah kompatible pada beragam device dan dapat berjalan lancar pada macam macam device yang ada di pasaran, biasanya ketika ada keterbatasan perangkat yang di gunakan QA bisa menggunakan aplikasi 3rd party seperti lambda test yang memiliki banyak macam device secara realtime melalui website mereka
4. Performance dan Stress testing
    - Test ketika ada banyak aplikasi yang berjalan bersamaan dengan aplikasi AYO untuk melihat apakah ada problem crash/kecepatan melambat bahkan critical issue lainya
