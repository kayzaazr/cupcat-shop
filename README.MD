Link Deploying App : https://cupcat-shop.adaptable.app/

Saya membuat jenis inventori berupa toko kue cupcake yang memiliki beberapa atribut, yaitu name, price, amount, description, dan sweetness.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

# Step-by-step
Step-by-step saya mengerjakan tugas 2 ini dimulai dari
1. Membuat repository baru di github dan folder baru di direktori lokal dengan nama aplikasi saya, yaitu cupcat-shop.
2. Membuka folder cupcat-shop di terminal Command dan menginstall Virtual Environment, lalu saya mengaktifkannya.
3. Menambahkan file requirements.txt dan diisi sesuai dengan yang ada di Tutorial 1 untuk menginstall Django dan menambahkan beberapa modul.
4. Membuat aplikasi baru bernama main dengan perintah python manage.py startapp main.
5. Setelah itu, daftarkan main ke dalam folder dengan menambahkan 'main' pada variabel INSTALLED_APPS yang ada di berkas settings.py
6. Melakukan migrasi model dengan perintah pyhton manage.py makemigrations.
7. Menambahkan import render dan fungsi show_main pada file views.py untuk menampilkan halaman main.html di mana terdapat variabel name, price, amount, description, dan sweetness yang telah didefinisikan di file models.py
8. Membuat berkas urls.py pada aplikasi main yang berisikan kode
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/', include('main.urls')),
]

dengan perintah python manage.py runserver pada terminal, saya dapat melihat tampilan browser di http://localhost:8000/main.
9. Terakhir, saya melakukan deploy di Adaptable dengan memilih Python App Template dan PostgreSQL yang akan digunakan.

# Bagan
![Frame 1](https://github.com/kayzaazr/cupcat-shop/assets/125040193/d2f5af7c-c908-438b-8efb-e42c3921e056)

Ketika user mengirim HTTP request pada web browser, request HTTP akan diteruskan ke urls.py dan dilakukan mapping. Setelah itu, dari urls.py akan diteruskan ke views.py. Views.py akan mengakses data yang dibutuhkan melalui models.py dan ditampilkan menggunakan template main. yang di return oleh views.py menghasilkan HTTP responseberupa HTML page.

# Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual Environment digunakan untuk mengisolasi paket dan dependensi yang berbeda di antara proyek-proyek yang berjalan pada satu perangkat yang sama. Meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun tanpa isolasi ini, ada risiko terjadinya konflik antara dependensi dari satu proyek dengan proyek lainnya, yang dapat mengakibatkan proyek-proyek tersebut menjadi tidak stabil atau tidak dapat berjalan dengan baik. Oleh karena itu, penggunaan virtual environment sangat disarankan untuk menjaga kerapian dan kestabilan suatu kode.

# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
1. MVC (Model-View-Controller) memiliki fokus pada pengendali (Controller) untuk mengatur interaksi antara Model (data dan logika) dan View (tampilan) dalam aplikasi. Controller bertanggung jawab untuk menerima input dari pengguna, memprosesnya, dan mengubah Model atau View sesuai dengan permintaan user.
2. MVT (Model-View-Template) memiliki fokus pada penggunaan Template (pola tampilan) dalam kerangka kerja Django. Dalam MVT, Template adalah komponen yang digunakan untuk mengatur tampilan HTML dari suatu aplikasi web. Template memungkinkan pemisahan yang jelas antara tampilan dan data.
3.MVVM (Model-View-ViewModel) adalah pola desain yang memiliki fokus pada ViewModel. ViewModel adalah komponen yang bertindak sebagai penghubung antara Model (data) dan View (tampilan) dalam pengembangan aplikasi berbasis antarmuka pengguna (UI). ViewModel bertanggung jawab untuk menyediakan data dan metode yang diperlukan oleh tampilan sehingga memungkinkan binding dua arah antara tampilan dan data.

Perbedaan utama di antara ketiganya terletak pada cara penggunaannya dan rincian implementasi yang spesifik. Namun, inti tujuan dari ketiga pola desain ini adalah untuk mencapai pemisahan yang jelas antara tampilan dan data dalam pengembangan aplikasi. Hal ini dilakukan untuk meningkatkan pemahaman kode dan kemampuan perluasan (scalability). Dengan kata lain, meskipun metode dan konsepnya berbeda, tetapi akhirnya semua tiga pola ini bertujuan untuk mencapai struktur kode yang efektif, lebih terstruktur, dan mudah dikelola.
