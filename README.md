# Tech Trove

Asyer Samuel Marpaung
2306165925

PWS : http://asyer-samuel-techtrove.pbp.cs.ui.ac.id/

<details>
  <summary>TUGAS 2</summary>

  **1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

  - Membuat Sebuah Proyek Django Baru

  Saya memulai dengan mengatur lingkungan kerja menggunakan virtual environment. Ini dilakukan dengan membuat lingkungan virtual menggunakan perintah python -m venv env, kemudian saya mengaktifkan environment tersebut. Setelah itu, saya menginstal Django dengan perintah pip install django. Langkah selanjutnya adalah membuat proyek baru dengan menjalankan perintah django-admin startproject tech_trove. Ini membuat struktur dasar proyek Django yang berisi direktori dan file utama seperti settings.py, urls.py, dan wsgi.py.

  - Membuat Aplikasi dengan Nama main

  Saya membuat aplikasi baru di dalam proyek dengan menjalankan perintah python manage.py startapp main. Setelah aplikasi main dibuat, saya menambahkannya ke dalam daftar INSTALLED_APPS di file settings.py proyek. Hal ini penting untuk memastikan aplikasi dapat dikenali oleh Django saat aplikasi berjalan.

  - Melakukan Routing pada Proyek

  Setelah aplikasi main dibuat, saya perlu memastikan bahwa aplikasi tersebut dapat diakses melalui URL tertentu. Untuk itu, saya menambahkan routing pada urls.py proyek utama. Saya menggunakan fungsi include() untuk menghubungkan routing dari proyek utama ke aplikasi main. Routing ini memastikan bahwa semua URL yang ditujukan ke aplikasi main akan diarahkan ke file urls.py dari aplikasi tersebut.

  - Membuat Model Product pada Aplikasi main

  Pada tahap ini, saya membuat model Product di dalam file models.py di aplikasi main. Model ini memiliki tiga atribut wajib yaitu name, price, dan description. Saya menggunakan CharField untuk atribut name, IntegerField untuk atribut price, dan TextField untuk atribut description. Saya juga menambahkan fungsi **str**() untuk mengembalikan representasi string dari nama produk. Setelah model dibuat, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate untuk membuat dan menerapkan perubahan database yang sesuai dengan model tersebut.

  - Membuat Fungsi di views.py

  Selanjutnya, saya membuat fungsi di file views.py yang mengembalikan template HTML dengan informasi yang diminta. Fungsi ini mengembalikan nama e-commerce, nama, dan kelas, lalu mengirimkannya sebagai konteks ke template HTML. Saya membuat file template di dalam direktori templates untuk memastikan struktur aplikasi mengikuti standar Django, dan template tersebut menerima data dari konteks yang dikirimkan oleh views.

  - Membuat Routing di urls.py Aplikasi main

  Saya membuat file urls.py di dalam aplikasi main (jika belum ada) dan mendefinisikan URL pattern untuk memetakan fungsi yang ada di views.py. Ini memungkinkan fungsi yang telah dibuat untuk diakses melalui URL yang ditentukan. Dengan menghubungkan URL pattern ke fungsi di views, saya memastikan web dapat merespons request dari user dengan benar.

  - Melakukan Deployment ke PWS

  Kemudian saya melakukan deployment dengan menjalankan perintah yang diperlukan untuk mengunggah webi ke platform PWS. Setelah berhasil di deploy, saya memastikan web dapat diakses melalui Internet.

  **2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

  ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeu3wxVVPU0wNGwzHX8vKMYVagRodpvsWi5udVQd_GAwbWX_OSN0EDQQigupujdeHjzrULQ_QcWiHyHwK4cujuKGsyaDt7I6PY18SXtrmk40nc6xevK9WautVE2pikiaKgzRSuFc4BHWVXR8QUTkCzTnNKN?key=IwMkdT6jNJPeEorK-Zf95A)

  1. urls.py - Pemetaan URL ke View

  Peran: urls.py bertanggung jawab untuk memetakan URL yang diminta oleh client (misalnya /produk/) ke fungsi view yang sesuai di views.py.

  Kaitan: Setiap kali client mengirimkan request ke server, urls.py akan mencocokkan URL yang diminta dengan pola-pola yang sudah didefinisikan. Jika ada pola yang sesuai, request tersebut akan diarahkan ke fungsi view tertentu.

  2. views.py - Pemrosesan Logika Bisnis dan Pengambilan Data

  Peran: views.py bertugas memproses logika bisnis aplikasi. Pada fungsi view, data dari model (database) akan diambil atau diolah, kemudian dikirimkan ke template untuk ditampilkan.

  Kaitan: Fungsi view akan memanggil model (models.py) jika dibutuhkan untuk mengambil data dari database. Setelah data diambil, view akan mengirimkan data tersebut ke HTML template untuk ditampilkan.

  3. models.py - Interaksi dengan Database

  Peran: models.py mendefinisikan struktur data dan berinteraksi dengan database. Django menggunakan ORM (Object-Relational Mapping) untuk memudahkan akses dan manipulasi data di database menggunakan kode Python.

  Kaitan: Model di models.py digunakan oleh views.py untuk mengambil atau menyimpan data dari/ke database. Setiap kali views.py membutuhkan data, model akan bertanggung jawab untuk mengakses database.

  4. HTML Template - Menampilkan Data ke Client

  Peran: Template HTML bertanggung jawab untuk menampilkan data yang diambil dari view. Template ini merupakan representasi visual dari halaman web yang akan ditampilkan ke client.

  Kaitan: Setelah views.py mengolah data dari model, data tersebut akan diteruskan ke template untuk di render menjadi HTML yang akan dikirim kembali ke client sebagai response.

  **3. Jelaskan fungsi git dalam pengembangan perangkat lunak!**

  Git dalam pengembangan perangkat lunak berfungsi sebagai sistem kontrol versi yang memungkinkan pengembang untuk melacak setiap perubahan kode yang dilakukan dalam proyek, memastikan bahwa mereka dapat kembali ke versi sebelumnya jika terjadi kesalahan. Selain itu, Git memfasilitasi kolaborasi dengan memungkinkan banyak pengembang untuk bekerja pada kode yang sama secara bersamaan melalui fitur branching dan merging, yang memungkinkan pengembangan paralel tanpa mengganggu kode utama. Git juga menyediakan repositori terpusat seperti GitHub dan GitLab, yang memungkinkan pengembang untuk menyimpan kode mereka secara online, berkolaborasi, mengelola proyek, serta menerapkan praktik Continuous Integration/Continuous Deployment (CI/CD).

  **4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

  Django adalah framework yang cocok untuk pemula dalam pengembangan perangkat lunak karena menyediakan banyak fitur bawaan yang memudahkan pembelajaran. Misalnya, autentikasi pengguna, manajemen URL, dan akses database semuanya sudah terintegrasi, sehingga tidak perlu mencari solusi dari awal lagi. Struktur proyek Django yang terorganisir juga membantu memahami bagaimana aplikasi web bekerja secara menyeluruh, dari menerima permintaan pengguna hingga menampilkan halaman. Selain itu, dokumentasinya yang sangat lengkap dan komunitasnya yang aktif memudahkan ketika menghadapi kesulitan atau tantangan dalam pengembangannya.

  **5. Mengapa model pada Django disebut sebagai ORM?**

  Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara kode Python dan database relasional. Dengan ORM, pengembang dapat mengelola database menggunakan objek Python tanpa perlu menulis query SQL secara langsung. ORM secara otomatis menerjemahkan operasi pada objek Python menjadi perintah SQL yang sesuai, memungkinkan pengembang untuk berfokus pada logika aplikasi daripada sintaks SQL yang kompleks. Ini tidak hanya meningkatkan produktivitas, tetapi juga memastikan integritas data dan keamanan aplikasi karena ORM menangani banyak detail teknis terkait interaksi dengan database.

</details>

<details>
  <summary>TUGAS 3</summary>

1. **Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?**  
   Data delivery diperlukan dalam pengimplementasian platform karena memungkinkan pertukaran informasi antar sistem secara efisien dan terstruktur. Dengan data delivery, platform dapat mengirim dan menerima data dalam berbagai format (seperti JSON atau XML), memungkinkan integrasi antara aplikasi, aksesibilitas API, dan pemrosesan data secara real-time. Ini mendukung komunikasi yang mulus antara frontend dan backend serta aplikasi lain, memastikan data yang diterima sesuai dan valid untuk keperluan platform.

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**  
   JSON umumnya dianggap lebih baik daripada XML untuk banyak kasus karena lebih sederhana, ringan, dan mudah dibaca oleh manusia maupun mesin. JSON memiliki format yang lebih ringkas dan langsung digunakan dalam JavaScript, menjadikannya lebih populer dalam pengembangan web modern. Selain itu, parsing JSON lebih cepat dan efisien dibandingkan XML. Sementara XML lebih kuat dalam struktur dan dapat digunakan untuk data yang lebih kompleks, JSON lebih disukai karena kemudahan penggunaannya dan kompatibilitasnya dengan API dan aplikasi web.  

3. **Jelaskan secara sederhana fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**  
   Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang telah ditentukan di model atau form terkait. Secara umum, file forms berperan dalam memetakan data dari input pengguna ke dalam model dengan mudah, serta mengotomatisasi validasi sesuai dengan aturan yang ada pada model. Dengan menggunakan `is_valid()`, Django memastikan bahwa data yang di-input, seperti tipe data, panjang karakter, atau batasan lainnya, valid sebelum disimpan ke database. Ini sangat penting untuk mencegah kesalahan penyimpanan data yang tidak sesuai, menjaga integritas data, dan memastikan sistem berjalan dengan benar tanpa memerlukan pengembang untuk menulis kode validasi secara manual.  

4. **Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**  
    Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan **Cross-Site Request Forgery (CSRF)**. Serangan CSRF adalah jenis serangan di mana penyerang memanfaatkan sesi yang sudah ada untuk mengirimkan permintaan jahat tanpa sepengetahuan atau izin pengguna. Penyerang dapat menyisipkan kode berbahaya di situs lain yang ketika dikunjungi oleh pengguna yang sudah login, secara otomatis mengirimkan permintaan yang tidak sah ke aplikasi web target.  
    Token `csrf_token` adalah kunci unik yang dikirim bersama form untuk memastikan bahwa data yang dikirim berasal dari sumber yang sah (yaitu aplikasi web itu sendiri), bukan dari situs eksternal yang mencoba melakukan serangan. Tanpa menambahkan `csrf_token`, form kita menjadi rentan terhadap serangan ini, yang memungkinkan penyerang membuat pengguna mengirimkan permintaan yang tidak diinginkan ke server.  
    Jika `csrf_token` tidak ditambahkan, penyerang dapat:  
   **Eksploitasi Sesi Pengguna**: Menggunakan situs jahat untuk mengirimkan permintaan yang meniru tindakan sah dari pengguna yang sudah login.  
   **Manipulasi Data**: Mengubah data atau pengaturan pengguna, seperti memperbarui profil atau menghapus data penting tanpa sepengetahuan pengguna.  
   **Akses Tidak Sah**: Mengirimkan permintaan yang memanfaatkan hak akses pengguna untuk melakukan tindakan yang tidak diinginkan atau berbahaya.  
   **Phishing dan Penipuan**: Mengarahkan korban ke situs jahat untuk meretas akun atau mengakses fitur sensitif.  
    Dengan `csrf_token`, kita memastikan bahwa setiap permintaan yang mengubah data atau melakukan tindakan penting berasal dari pengguna yang sah dan bukan dari sumber yang tidak diinginkan.  

5. **Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial)**

- **Membuat input `form` untuk menambahkan objek model pada app sebelumnya.**

  Sebelum melanjutkan ke pembuatan formulir input, saya terlebih dahulu membuat file `base.html` yang berfungsi sebagai template dasar untuk aplikasi saya. File ini berisi struktur HTML umum yang akan digunakan oleh semua template lainnya. Dengan menggunakan file ini, saya dapat memastikan konsistensi tampilan dan struktur di seluruh aplikasi.

  Di dalam `base.html`, saya menyertakan elemen-elemen dasar seperti tag `<html>`, `<head>`, dan `<body>`. Saya juga menambahkan blok konten `{% block content %}` yang memungkinkan template lain untuk menambahkan konten khusus mereka di lokasi yang tepat dalam struktur HTML. Dengan cara ini, saya hanya perlu mengubah `base.html` jika saya ingin memperbarui elemen-elemen umum di seluruh aplikasi, tanpa perlu memodifikasi setiap template secara individu.

  Setelah menyiapkan `base.html`, saya melanjutkan dengan mengimplementasikan formulir input untuk model `Product`. Untuk itu, saya mengikuti langkah-langkah berikut:

  Pertama, saya mendefinisikan formulir di file `forms.py`. Saya membuat kelas `ProductEntryForm` yang mewarisi dari `ModelForm`. Di dalam kelas ini, saya menentukan model `Product` dan atribut-atribut yang akan diinputkan, yaitu `name`, `price`, `quantity`, dan `description`. Kelas ini akan menghasilkan formulir yang sesuai dengan model tersebut.

  Selanjutnya, saya mengatur tampilan (view) di file `views.py`. Saya menambahkan fungsi `product_entry` yang menangani pengiriman dan penampilan formulir. Fungsi ini memeriksa apakah metode permintaan adalah POST dan jika data formulir valid, data akan disimpan ke dalam basis data. Setelah penyimpanan berhasil, saya mengalihkan pengguna ke tampilan utama (`show_main`). Jika metode permintaan adalah GET, formulir kosong akan ditampilkan kepada pengguna. Fungsi ini juga memanfaatkan `ProductEntryForm` untuk menangani formulir.

  Kemudian, saya membuat template HTML `product_entry.html` untuk menampilkan formulir. Template ini memperluas dari `base.html` dan memblokir konten untuk menampilkan formulir dengan elemen-elemen HTML dasar. Saya menggunakan metode POST untuk mengirimkan data dan memastikan token CSRF disertakan untuk keamanan. Formulir ditampilkan dalam format tabel menggunakan `{{ form.as_table }}`.

  Terakhir, saya menambahkan URL yang sesuai di file `urls.py`. Saya menambahkan entri dengan path `product-entry` yang mengarahkan ke fungsi `product_entry`. Dengan langkah-langkah ini, saya telah berhasil membuat input form yang fungsional untuk menambahkan objek model `Product` ke dalam aplikasi Django saya.

- Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML _by ID_, dan JSON _by ID_.

  Untuk menambahkan fungsi-fungsi yang memungkinkan tampilan objek dalam format XML, JSON, XML berdasarkan ID, dan JSON berdasarkan ID, saya menambahkan empat fungsi baru ke file `views.py`. Fungsi-fungsi ini bertanggung jawab untuk menghasilkan data dalam format yang berbeda dan mengirimkan respons HTTP dengan tipe konten yang sesuai.

1. **Fungsi `show_xml`**: Fungsi ini mengambil semua objek `Product` dari basis data dan menggunakan `serializers.serialize` untuk mengkonversinya ke format XML. Saya mengembalikan data tersebut dalam respons HTTP dengan tipe konten `"application/xml"`.
2. **Fungsi `show_json`**: Mirip dengan fungsi `show_xml`, fungsi ini mengkonversi semua objek `Product` menjadi format JSON. Data JSON tersebut dikirimkan dalam respons HTTP dengan tipe konten `"application/json"`.
3. **Fungsi `show_xml_by_id`**: Fungsi ini mengambil objek `Product` berdasarkan ID yang diberikan. Menggunakan `serializers.serialize`, data objek tersebut dikonversi ke format XML dan dikirimkan dalam respons HTTP dengan tipe konten `"application/xml"`.
4. **Fungsi `show_json_by_id`**: Fungsi ini berfungsi serupa dengan `show_xml_by_id`, tetapi mengonversi data objek menjadi format JSON. Respons dikirimkan dengan tipe konten `"application/json"`.

   Dengan cara ini, saya dapat menyediakan data produk dalam berbagai format sesuai dengan kebutuhan pengguna aplikasi saya. Setiap fungsi mengakses basis data, mengkonversi data ke format yang diinginkan, dan mengembalikan hasilnya dalam bentuk respons HTTP yang sesuai.

- Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2\.

  Untuk menambahkan routing URL untuk fungsi-fungsi view baru yang telah saya buat, saya memodifikasi file `urls.py` pada proyek Django saya. Proses ini melibatkan penambahan entri baru dalam `urlpatterns`, yang merupakan daftar URL patterns yang menghubungkan URL tertentu dengan fungsi view yang sesuai.

  Pertama, saya menambahkan entri untuk menampilkan produk dalam format XML dengan menambahkan path `xml/` ke dalam `urlpatterns`. Path ini akan mengarahkan permintaan ke fungsi `show_xml`, yang mengembalikan data produk dalam format XML. Dengan menambahkan path ini, saya memastikan bahwa pengguna dapat mengakses daftar semua produk dalam format XML melalui URL yang telah ditentukan.

  Selanjutnya, saya menambahkan entri serupa untuk format JSON dengan path `json/`. Ini akan mengarahkan permintaan ke fungsi `show_json`, yang mengembalikan data produk dalam format JSON. Dengan menambahkan path ini, pengguna dapat melihat daftar semua produk dalam format JSON dengan mengunjungi URL yang sesuai.

  Untuk menampilkan data produk berdasarkan ID dalam format XML, saya menambahkan path dengan pola `xml/<str:id>/`. Path ini memungkinkan pengguna untuk menyertakan ID produk sebagai bagian dari URL, dan akan mengarahkan permintaan ke fungsi `show_xml_by_id`, yang mengembalikan data produk tertentu dalam format XML berdasarkan ID yang diberikan.

  Terakhir, saya menambahkan path `json/<str:id>/` untuk menampilkan data produk berdasarkan ID dalam format JSON. Path ini mengarahkan permintaan ke fungsi `show_json_by_id`, yang mengembalikan data produk tertentu dalam format JSON berdasarkan ID yang diberikan. Dengan menambahkan path-path ini, saya memastikan bahwa aplikasi saya dapat menyediakan data produk dalam berbagai format dan berdasarkan ID produk tertentu sesuai dengan kebutuhan pengguna.

  **Hasil akses URL pada POSTMAN**

  Postman \- GET XML

  **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXczN3D8IKhMYlDUTibQ702bOMqeuLLahaqte2EFMrETs0PbQ3ree8AE1bSjzYPZ6LoibMuJHYSKF_ZYMt71PH6q1V5lEv0g9PC5FcZoL0xeJVGo4PNSO11XJA1O2DUp-2D8TZ6l6_BCIPsqxk13xIyUr8jV?key=O0F5_SMRpCcRy4zmxo2sIg)**

  Postman \- GET XML by Id

  **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcWJ6IK_nVvfMa0kS4swr1Er8v47DULb0LaPRyIug9Ghkl6BkkdBEv-U91Pyxr5WH_XxOCn_tpOR8yT08TQY0HFywMi4YQ_qRv23MNCxwrXBTce1H6s83_JJYGJ9m-a5Bj-eZmddlzsPzWtkXU_BIDRwiwT?key=O0F5_SMRpCcRy4zmxo2sIg)**

  Postman \- GET JSON

  **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeH0wlRm452Ah2xvxU85MqSvEC4pIUadz1nIETz4H7CEgbJVv0HAJgzTRRfWMTtzcdL0ai48FCWEyfMxDtyt0UgPhg3UDzOdv-oDe4ssQ3v9IWLP4kRMqArUlv5q5IpbA5FYsUmdf2k-eAZGo1oP7lxveFJ?key=O0F5_SMRpCcRy4zmxo2sIg)**

  Postman \- GET JSON by Id

  **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfXq8y1Hhi5wh9llRvF6rXxeOe3rvNGh1sGWEMUfza4cmHMH6X-FwFsi3EIMYf9-Hxyc4gQKiL2Q0hOdldAkCAGiVbfzq2XpMZYe7O_61-HHUSJKZ5YuWn8T0CydSrK8ywZOAZlBPjL67T0eUUEfZcetQY?key=O0F5_SMRpCcRy4zmxo2sIg)**

</details>
