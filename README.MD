Link Deploying App : https://cupcat-shop.adaptable.app/

Saya membuat jenis inventori berupa toko kue cupcake yang memiliki beberapa atribut, yaitu name, price, amount, description, dan sweetness.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

Bagan

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.