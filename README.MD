## TUGAS 3
> Cupcat-shop merupakan toko kue jenis cupcake. Di dalam toko ini terdapat 5 informasi yang tersedia, yaitu name, price, description, sweetness, dan amount.

### Apa perbedaan antara form POST dan form GET dalam Django?
##### FORM POST 
1. POST digunakan untuk mengirim data ke server. Data formulir dikirim dalam bentuk permintaan HTTP, sehingga tidak terlihat dalam URL.
2. Data yang dikirim dengan metode POST tidak tampil di URL atau log server, sehingga lebih aman dan sesuai untuk mengirim data sensitif seperti kata sandi.
3. POST cocok digunakan untuk permintaan yang akan mengubah status atau data pada server.

##### FORM GET
1. GET digunakan untuk mengambil data dari server. Ketika menggunakan metode GET, data formulir dikirim sebagai bagian dari URL.
2. Data yang dikirim dengan metode GET tersimpan dalam query string URL, yang dapat terlihat oleh semua orang dan tampil di log server.
3. GET cocok digunakan untuk permintaan yang bersifat idempoten, artinya permintaan ini tidak akan mengubah status atau data pada server. Contohnya adalah pencarian web atau tautan yang dapat dibookmark.

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Perbedaan mendasar antara XML, JSON, dan HTML adalah bahwa XML dan JSON digunakan untuk penyimpanan dan pengiriman data, sedangkan HTML digunakan untuk menggambarkan cara data tersebut ditampilkan.
Dengan singkat, HTML adalah blok bangunan utama dalam pengembangan web dan digunakan untuk mendefinisikan struktur sebuah halaman. XML atau JSON dapat mengangkut data antara server dan sering digunakan bersamaan dengan HTML.
##### HTML

##### XML
1. XML memiliki struktur yang kuat dan dapat digunakan untuk merepresentasikan dan mengirimkan data dengan hierarki yang kompleks. 
2. XML menggunakan tag khusus untuk mengidentifikasi elemen data. 
3. Proses parsing XML memerlukan lebih banyak waktu dan sumber daya dibandingkan dengan format lain seperti JSON, sehingga dapat menjadi kurang efisien dalam situasi tertentu.

##### JSON
1. JSON adalah format data yang ringkas, mudah dibaca dan mudah dipahami.
2. JSON mewakili data dalam bentuk objek dan larik yang memungkinkan representasi yang lebih dinamis dan terstruktur daripada XML.
3. Proses parsing JSON lebih efisien daripada XML, membuatnya lebih cocok untuk aplikasi berkinerja tinggi.

##### HTML
1. HTML adalah bahasa khusus untuk membuat tampilan halaman web. Meskipun dapat mengirimkan data, tetapi itu bukan tujuan utamanya.
2. HTML digunakan untuk mendefinisikan struktur dan tampilan halaman web dengan tag-tag yang menggambarkan elemen-elemen seperti teks, gambar, tautan, dll.
3. Meskipun HTML dapat mengandung data, itu lebih fokus pada bagaimana data tersebut ditampilkan di browser web dan kurang cocok untuk pengiriman data.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON menggunakan format yang sederhana dan mirip dengan struktur data dalam bahasa pemrograman seperti JavaScript. Ini membuatnya mudah dipahami oleh pengembang. JSON memungkinkan data untuk disusun dalam bentuk objek dan larik, yang sesuai untuk berbagai jenis data. Karena format datanya ringkas dan berukuran kecil, Ini memungkinkan untuk transfer data yang besar dengan cepat melalui jaringan. Kemampuannya untuk mengatasi data berukuran besar membuatnya cocok untuk aplikasi modern yang menghadapi volume data besar. Selain itu parsing data pada JSON meningkatkan responsivitas aplikasi web, terutama ketika aplikasi harus berkomunikasi dengan server secara real-time.

### STEP
1. Pertama, membuat file baru forms.py pada direktori main. FIle forms.py ini diisi dengan kode
'''
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description","sweetness","amount"]
'''
2. Pada views.py, tambahkan fungsi create_product
'''
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
'''
3. Pada direktori main/templates menambahkan template baru bernama create_product.html dengan kode berikut
'''
{% extends 'base.html' %}

{% block content %}
...
<body>
    <div class="container1">
        <h1>Add New Product</h1>

        <div class="container">
            <form method="POST" class="form-table">
                {% csrf_token %}
                <table>
                    {{ form.as_table }}
                    <tr>
                        <td></td>
                        <td>
                            <input type="submit" value="Add Product"/>
                        </td>
                    </tr>
                </table>
            </form>
        </div>
</div>
</body>
{% endblock content %}
'''
4. Lalu untuk XML dan JSON, pada views.py di folder main, tambahkan import HttpResponse dan serializer. Selain itu tambahkan juga fungsi show_xml dan show_json yang pada masing-masing data memiliki variable data = Product.objects.all(). Pada masing-masing fungsi meng-return HttpResponse yang sudah di-serialize sesuai format masing-masing yaitu XML dan JSON
5. Step sebelumnya diaplikasikan untuk format XML dan JSON by ID. Parameternya ditambahkan variable id. Setiap fungsinya terdapat data = Product.objects.filter(pk=id), lalu return HttpResponse yang sudah di-serialize sesuai format masing-masing yaitu XML dan JSON.
6. Terakhir, pada file urls.py tambahkan urlpatterns sesuai dengan format yang telah ditambahkan di atas.
'''
from django.urls import path
from main.views import show_main
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
'''

### Screenshot Postman
##### HTML


<details>
<summary> Tugas 2 </summary>
Link Deploying App : https://cupcat-shop.adaptable.app/

Saya membuat jenis inventori berupa toko kue cupcake yang memiliki beberapa atribut, yaitu name, price, amount, description, dan sweetness.

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
3. MVVM (Model-View-ViewModel) adalah pola desain yang memiliki fokus pada ViewModel. ViewModel adalah komponen yang bertindak sebagai penghubung antara Model (data) dan View (tampilan) dalam pengembangan aplikasi berbasis antarmuka pengguna (UI). ViewModel bertanggung jawab untuk menyediakan data dan metode yang diperlukan oleh tampilan sehingga memungkinkan binding dua arah antara tampilan dan data.

Perbedaan utama di antara ketiganya terletak pada cara penggunaannya dan rincian implementasi yang spesifik. Namun, inti tujuan dari ketiga pola desain ini adalah untuk mencapai pemisahan yang jelas antara tampilan dan data dalam pengembangan aplikasi. Hal ini dilakukan untuk meningkatkan pemahaman kode dan kemampuan perluasan (scalability). Dengan kata lain, meskipun metode dan konsepnya berbeda, tetapi akhirnya semua tiga pola ini bertujuan untuk mencapai struktur kode yang efektif, lebih terstruktur, dan mudah dikelola.
</details>
