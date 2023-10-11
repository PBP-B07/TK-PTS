# UlasBuku 📖

## Kelompok B-07 
- Alifa Hanania Ardha - 2206024392<br>
- Hanan Adipratama - 2206081824<br>
- Muhammad Azmi Falah - 2206082285<br>
- Muhammad Farrel Altaf - 2206829332<br>
- Monica Gloria Damanik - 2206082442<br>
- Rahida Syafa Nurdya - 2206829023

## Cerita Aplikasi
Dalam dunia yang terus bergerak cepat dalam inovasi teknologi dan ilmu komputer, mencari sumber referensi berkualitas menjadi tantangan tersendiri. Sebagian besar mahasiswa, terutama mereka yang baru memulai perjalanan akademik di bidang ini, sering kali merasa terjebak dalam belantara informasi. Ditambah lagi, pemasaran buku yang menarik sering kali mengecoh, memancing mereka untuk membeli buku dengan harapan tinggi namun kemudian merasa kecewa dengan isi halamannya.

Sekelompok mahasiswa dari Fakultas Ilmu Komputer UI, yang telah menghabiskan banyak waktu dalam pencarian buku yang tepat, memutuskan untuk mengambil langkah proaktif. Mereka mendirikan "UlasBuku", sebuah platform online di mana mereka dan orang-orang lain yang berkecimpung di dunia Computer Science dapat meninggalkan ulasan jujur tentang buku-buku yang mereka baca. Tujuannya sederhana: membantu orang lain menghindari kesalahan yang sama dan memastikan bahwa setiap pembelian buku memang bernilai.

Namun, UlasBuku bukan sekadar tempat untuk ulasan. Seiring dengan pertumbuhan penggunanya, fitur-fitur baru diperkenalkan. Forum diskusi diluncurkan, memberikan ruang bagi anggota untuk mendiskusikan konsep-konsep yang mereka temukan dalam buku-buku tersebut, membagikan perspektif, atau bahkan meminta bantuan dalam topik yang sulit.



## Manfaat Aplikasi
1. Peningkatan Keputusan Pembelian Buku: Dengan adanya ulasan dan rekomendasi dari komunitas, pengguna dapat menghemat waktu dan uang dengan memilih buku yang benar-benar sesuai dengan kebutuhan dan kualitas yang diharapkan.

2. Mengurangi Kesulitan dalam Menemukan Materi Berkualitas: Banyaknya buku di pasaran seringkali membingungkan. UlasBuku menjadi penyaring informasi, memudahkan pengguna menemukan buku berkualitas tinggi berdasarkan ulasan komunitas.

3. Menambah Pengetahuan: Melalui diskusi dengan komunitas yang aktif, pengguna mendapat wawasan tambahan tentang topik-topik dalam buku, yang mungkin tidak mereka peroleh hanya dengan membaca buku tersebut.

## Daftar Modul
1. Homepage (main) 
    - Menampilkan rekomendasi buku berupa forum yang sedang ramai diperbincangkan dan juga forum yang kurang peminatnya (READ)
    - Menampilkan buku dengan ulasan terbaru dan terbaik dari user (READ)
    - Menampilkan buku dengan forum yang di dalamnya ada kontribusi user (READ)
    - Tentang UlasBuku (READ)
    - Menampilkan event/iklan yang berhubungan dengan buku pada database (READ)
    - `Admin` Menambahkan event/iklan yang berhubungan dengan buku pada database (CREATE)

2. Profile (ditaruh di navbar)
    - Riwayat ulasan buku yang pernah di ulas oleh user (READ)
    - Riwayat forum yang pernah user kontribusi (READ)
    - Deskripsi diri (READ)
    - Hapus ulasan (DELETE)
    - Edit ulasan (UPDATE)

3. Katalog buku (ditaruh di navbar)
    - Berisi apa saja buku yang ada di UlasBuku yang terurut sesuai abjad (READ)
    - Didalam page ini ada fitur ‘search’ buku (READ)
    - Didalam page ini ada fitur filter (berdasarkan tag)  (READ)
        1. Kategori buku
        2. Bintang (hasil ulasan)
    - `Admin` dapat menambahkan detail buku (CREATE)

4. Deskripsi per buku (ada di setiap buku)
    - Details buku (Judul, Deskripsi, Penulis, ISBN-10, ISBN-13, Tanggal Rilis, Edisi, Best Seller, Estimasi Harga, tag buku) (READ)
    - Melihat review dan rate user jika ada (READ)
    - Lihat ringkasan review dan rate yang ada di buku yang berkaitan (READ)
    - Lihat ringkasan forum diskusi yang ada di buku yang berkaitan (READ)
    - `Admin` dapat mengedit deskripsi buku (UPDATE)

5. Review + Rate (ada di setiap buku)
    - User dapat memberikan satu review/ulasan dan rating terhadap satu buku (CREATE)
    - User dapat melihat review dan rating secara lengkap (READ)
    - User dapat memfilter review dan rating yang diinginkan berdasarkan: (READ)
        1. Jumlah Bintang (1-5) 
        2. Terbaru-Terlama

6. Forum (ada di setiap buku)
    - User dapat memposting pembicaraannya pada forum (CREATE)
    - User dapat mengirimkan foto pada forum (CREATE)
    - User dapat melihat perbincangan di forum tersebut (READ)

7. Login dan Register
    - User dapat masuk menggunakan login (CREATE)
    - User dapat mendaftarkan menggunakan register (CREATE)


## Sumber Dataset
Pada projek kali ini kami menggunakan dataset dari `Kaggle`, Dataset tersebut berisi lebih dari 300 buku Ilmu Komputer yang tersedia di Amazon:

[Amazon Books Details for Computer Science](https://www.kaggle.com/datasets/uzair01/amazon-books)

## Role
1. Role dari pengunjung terdaftar: 
    - Dapat mendaftarkan akun dan melakukan login
    - Dapat menambahkan review buku yang ada di UlasBuku 
    - Dapat melihat detail dan review dari tiap buku yang ada di UlasBuku
    - Dapat menambahkan diskusi di forum diskusi UlasBuku
    - Dapat melakukan pencarian buku dengan filter yang diterapkan
2. Role dari admin:
    - Dapat mendaftarkan akun dan melakukan login
    - Dapat mengelola katalog buku yang ada di UlasBuku

## Referensi
1. [Ulas Kelas](https://www.ulaskelas.id/en)
			      
