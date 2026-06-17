Test Scenario sederhana untuk Proses booking
1. TC001 Validasi Harga Booking Sesuai Jadwal
    - Memastikan harga yang tersimpan pada booking sesuai dengan harga jadwal yang dipilih.
    - Precondition : 
        Venue 15 available pada tanggal 2022-12-10 jam 09:00 - 11:00
        Price : 1.000.000
    - Test Step :
        1. Login sebagai user
        2. Pilih venue 15
        3. Pilih tanggal 2022-12-10
        4. Pilih jam 09:00-11:00
        5. Klik Book
        6. Simpan booking
    - Expected Result :
        Booking berhasil dibuat.
        Harga yang tersimpan pada tabel booking = 1.000.000.
        Harga yang ditampilkan di UI = 1.000.000.

2. TC002 Cegah Double Booking
    - Memastikan slot yang sudah dibooking tidak dapat dibooking kembali.
    - Precondition :
        Sudah ada booking untuk 
            Venue : 15
            Date : 2022-12-10
            Time : 09:00-11:00
    - Test Step :
        1. Login user A
        2. Booking venue 15 pada 09:00-11:00
        3. Booking berhasil
        4. Login user B
        5. Coba booking venue 15 pada slot yang sama
    - Expected Result :
        Sistem menolak booking kedua.
        Muncul pesan validasi "Selected time is not available"

3. TC003 Validasi Slot Bersebelahan
    - Memastikan user dapat booking pada waktu yang bersebelahan dengan jadwal sesudah/sebelumnya
    - Precondition :
        Ada 2 jadwal yang bersebelahan untuk venue 15 07:00 - 09:00, 09:00 - 11:00 dan 11:00 - 13:00 yang available
    - Test Step :
        1. Login user A
        2. Booking venue 15 pada 09:00-11:00
        3. Booking berhasil
        4. Login user B
        5. Coba booking venue 15 pada 11:00-13:00
    - Expected Result :
        Booking ke dua user A dan B success
        Data pada table  sesuai dengan User id A dan B
        