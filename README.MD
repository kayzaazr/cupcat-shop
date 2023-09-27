# CUPCAT
Link Deploying App : https://cupcat-shop.adaptable.app/
> Cupcat-shop merupakan toko kue jenis cupcake. Di dalam toko ini terdapat 5 informasi yang tersedia, yaitu name, price, description, sweetness, dan amount.

## TUGAS 4

## Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

`UserCreationForm` adalah salah satu form bawaan yang disediakan oleh Django untuk mengelola proses autentikasi dan otorisasi pengguna. Form ini digunakan untuk membuat formulir pendaftaran (sign-up) pengguna baru di aplikasi web.

### Kelebihan
- Mudah Digunakan
- Terintegrasi dengan Django Model `User`
- Dilengkapi validasi input yang sesuai

### Kekurangan
- Validasi input yang sesuai
- Kustomisasi yang terbatas

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

- **Otentikasi (Authentication):**
Otentikasi adalah proses verifikasi identitas pengguna. Ini memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah mereka yang mereka klaim. 

- **Otorisasi (Authorization):**
Otorisasi adalah proses menentukan akses atau izin yang dimiliki oleh pengguna yang telah terotentikasi. Ini mengatur apa yang dapat dan tidak dapat dilakukan oleh pengguna dalam aplikasi berdasarkan peran (role) atau izin yang mereka miliki.

Kedua tahap ini, otentikasi dan otorisasi, sangat penting dalam mengelola keamanan aplikasi. Tanpa otentikasi yang kuat, orang yang tidak sah dapat mengakses data dan fungsi yang seharusnya tidak mereka akses. Tanpa otorisasi yang baik, pengguna yang telah terotentikasi mungkin mendapatkan akses yang lebih besar dari yang seharusnya, yang dapat mengancam keamanan dan privasi data.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah file kecil yang disimpan di browser pengguna dan digunakan untuk menyimpan informasi yang dapat diakses oleh server di halaman web tersebut. 

Dalam Django, cookies sering digunakan untuk mengelola sesi pengguna (user sessions) secara server-side. Namun, untuk mencapai hal ini, Django menggunakan mekanisme cookies yang disebut "session cookies" untuk menyimpan Session ID di sisi klien (browser pengguna).

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Secara default, cookies berfungsi untuk menyimpan informasi di dalam browser dan aman untuk digunakan dalam pengembangan web. tetapi ada potensi risiko yang harus diwaspadai dan dikelola dengan baik. Beberapa risiko potensial yang terkait dengan penggunaan cookies contohnya Cookie Theft, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), dll.

## STEP
### Mengimplementasikan Autentikasi
1. Pertama, saya menambahkan import yang sesuai pada file `views.py`
```python
...
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
```
2. Kedua, saya juga menambahkan fungsi baru yang sesuai pada file `views.py`
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')
```

3. Ketiga, saya menambahkan template baru untuk tampilan login dan registrasi dengan menambahkan file `login.html` dan `register.html` berikut pada folder `templates`
- ##### login.html
```python
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
- #### register.html
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

4. Terakhir, pada file `urls.py` saya menambahkan imports dan path urls baru
- #### Imports
```python
...
from main.views import register, login_user, logout_user
...
```
- #### URL Paths
```python
...
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('register/', register, name='register'),
...
```

### Mengimplementasikan Otentikasi
1. Pertama, saya menambahkan *import* yang sesuai pada file views.py
```python
from django.contrib.auth.decorators import login_required
```
2. Kedua, saya menambahkan *code* diatas fungsi yang akan show_main() sehingga fungsi show_main() hanya dapat diakses jika user telah login
```python
...
@login_required(login_url='/login')
def show_main(request):
...
```

### Menghubungkan Model `Product` dengan `User`
1. Pertama, saya menambahkan *import* yang sesuai pada file models.py
```python
from django.contrib.auth.decorators import login_required
```
2. Kedua, di file yang sama saya menambahkan *attribute*  `user` pada Class `Product`
```python
...
user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
3. Terakhir, saya mengubah beberapa fungsi pada views.py
- context pada show_main
```python
context = {
    'name': request.user.username,  # Mengubah atribut name
    'class': 'PBP A',
    'products': products,
}
```

- create_product
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

### Menggunakan Data Dari Cookies
1. Pertama, saya menambahkan *import* yang sesuai pada file views.py
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
2. Kedua, saya mengubah fungsi-fungsi pada views.py
- login_user
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Mengubah blok if dibawah
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

- context pada show_main
```python
context = {
    'name': request.user.username,
    'class': 'PBP A',
    'products': products,
    'last_login': request.COOKIES['last_login'], # Menambahkan context baru
}
```

- logout_user
```python
# Mengubah fungsi logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
3. Terakhir, menampilkan data dari Cookies pada template dengan menambahkan kode berikut pada `main.html`
```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

<details>
<summary> ## TUGAS 3 </summary>
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
Dengan singkat, HTML adalah blok bangunan utama dalam pengembangan web dan digunakan untuk mendefinisikan struktur sebuah halaman. XML atau JSON dapat mengangkut data antara server dan sering digunakan bersamaan dengan HTML

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
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description","sweetness","amount"]
```

2. Pada views.py, tambahkan fungsi create_product
```
    def create_product(request):
        form = ProductForm(request.POST or None)
    
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_product.html", context)
```

3. Pada direktori main/templates menambahkan template baru bernama create_product.html dengan kode berikut
```
    {% extends 'base.html' %}
    {% block content %}
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
```

4. Lalu untuk XML dan JSON, pada views.py di folder main, tambahkan import HttpResponse dan serializer. Selain itu tambahkan juga fungsi show_xml dan show_json yang pada masing-masing data memiliki variable data = Product.objects.all(). Pada masing-masing fungsi meng-return HttpResponse yang sudah di-serialize sesuai format masing-masing yaitu XML dan JSON

5. Step sebelumnya diaplikasikan untuk format XML dan JSON by ID. Parameternya ditambahkan variable id. Setiap fungsinya terdapat data = Product.objects.filter(pk=id), lalu return HttpResponse yang sudah di-serialize sesuai format masing-masing yaitu XML dan JSON.

6. Terakhir, pada file urls.py tambahkan urlpatterns sesuai dengan format yang telah ditambahkan di atas.
```
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
```

### Screenshot Postman
##### HTML
![html](https://github.com/kayzaazr/cupcat-shop/assets/125040193/840b2ef6-0c8b-4b6b-b77c-09b0807ce83f)

##### XML
![xml](https://github.com/kayzaazr/cupcat-shop/assets/125040193/2db26d5a-d83b-4c7a-81dd-5f7a3949ecc1)

##### JSON
![json](https://github.com/kayzaazr/cupcat-shop/assets/125040193/992a499c-b36d-46a6-838b-f56147f31729)

##### XML by ID
![xml_by_id](https://github.com/kayzaazr/cupcat-shop/assets/125040193/c76f4c84-47df-42a1-b01d-b1f2948babd3)

##### JSON by ID
![json_by_id](https://github.com/kayzaazr/cupcat-shop/assets/125040193/9987d6cc-b8d7-4fd4-83d3-36fce99949d2)

</details>

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
