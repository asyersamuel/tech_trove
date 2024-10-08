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

<details>
  <summary>TUGAS 4</summary>
  
**1\. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?**

Django UserCreationForm adalah formulir bawaan dari Django yang digunakan untuk membuat pengguna baru dalam aplikasi web. Formulir ini menyediakan tiga bidang utama: username, password, dan konfirmasi password

### Kelebihan:

1. **Mudah Digunakan:** UserCreationForm sudah siap pakai dan memudahkan pengembang untuk membuat formulir pendaftaran pengguna tanpa perlu menulis kode dari awal.
2. **Keamanan:** Formulir ini sudah dilengkapi dengan validasi kata sandi dan konfirmasi kata sandi, sehingga membantu mencegah kesalahan umum seperti kata sandi yang tidak cocok.
3. **Integrasi dengan Django Admin:** Mudah diintegrasikan dengan sistem autentikasi dan administrasi Django, sehingga mempermudah pengelolaan pengguna.

### Kekurangan:

1. **Keterbatasan Kustomisasi:** Meskipun mudah digunakan, UserCreationForm mungkin memerlukan penyesuaian tambahan jika Anda membutuhkan fitur khusus atau tampilan yang berbeda.
2. **Tidak Ada Tampilan Bawaan:** Django tidak menyediakan tampilan (view) bawaan untuk menangani pembuatan pengguna, sehingga Anda harus membuat tampilan sendiri untuk menggunakannya

**2\. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

Autentikasi adalah proses untuk memverifikasi identitas pengguna. Dalam konteks Django, ini biasanya dilakukan melalui nama pengguna dan kata sandi. Ketika pengguna mencoba masuk ke aplikasi, sistem autentikasi akan memeriksa apakah kredensial yang diberikan cocok dengan yang ada di database. Jika cocok, pengguna diizinkan untuk masuk. Autentikasi penting karena memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sehingga mencegah akses oleh pihak yang tidak berwenang.

Otorisasi, di sisi lain, adalah proses untuk menentukan hak akses pengguna setelah mereka terautentikasi. Ini berarti setelah pengguna berhasil masuk, sistem akan menentukan apa yang bisa dan tidak bisa dilakukan oleh pengguna tersebut berdasarkan peran atau izin yang mereka miliki. Misalnya, seorang pengguna biasa mungkin hanya bisa melihat dan mengedit profil mereka sendiri, sementara seorang admin bisa mengelola semua profil pengguna. Otorisasi penting karena memastikan bahwa pengguna hanya bisa mengakses data dan fungsi yang sesuai dengan peran mereka, menjaga keamanan dan integritas data.

Kedua konsep ini sangat penting dalam pengembangan aplikasi web karena mereka bekerja bersama untuk memastikan keamanan dan kontrol akses yang tepat. Autentikasi memastikan bahwa hanya pengguna yang sah yang bisa masuk, sementara otorisasi memastikan bahwa mereka hanya bisa melakukan tindakan yang diizinkan. Dengan kombinasi ini, pengembang dapat mengontrol akses ke berbagai bagian aplikasi berdasarkan peran pengguna, memberikan pengalaman pengguna yang aman dan terkontrol.

**3\. Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?**

Cookies dalam konteks aplikasi web adalah file kecil yang disimpan di browser pengguna untuk menyimpan data seperti preferensi atau informasi sesi. Cookies memungkinkan situs web mengenali pengguna saat mereka kembali, misalnya untuk tetap login atau mengingat pengaturan tertentu.

Dalam Django, cookies digunakan untuk mengelola **data sesi pengguna**. Ketika pengguna login atau melakukan interaksi yang membutuhkan sesi, Django membuat sesi unik untuk pengguna tersebut dan menyimpan **ID sesi** dalam cookie di browser mereka. ID ini digunakan untuk melacak aktivitas pengguna selama mereka menggunakan situs web, sementara data sesi yang sebenarnya (misalnya, informasi login) disimpan di server Django. Django menggunakan cookies ini untuk memeriksa apakah pengguna sudah login atau untuk menyimpan informasi lain yang berkaitan dengan sesi, tanpa harus menyimpan data sensitif di cookie itu sendiri.

**4\.Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

Penggunaan cookies dalam pengembangan web secara default dapat aman, namun ada risiko potensial yang harus diperhatikan. Cookies adalah file kecil yang disimpan di browser pengguna untuk menyimpan informasi seperti preferensi, data login, atau sesi. Secara umum, cookies membantu meningkatkan pengalaman pengguna, tetapi jika tidak dikelola dengan benar, mereka dapat menjadi celah keamanan.

Salah satu risiko utama adalah **pencurian cookies** melalui serangan **Cross-Site Scripting (XSS)**, di mana penyerang dapat menyuntikkan skrip berbahaya ke dalam situs web untuk mencuri cookies yang berisi informasi sensitif. Untuk mengurangi risiko ini, pengembang dapat mengaktifkan atribut **HttpOnly** pada cookies, sehingga cookie tersebut tidak dapat diakses melalui JavaScript.

Risiko lainnya adalah **Cross-Site Request Forgery (CSRF)**, di mana penyerang menggunakan cookies yang valid untuk menjalankan permintaan berbahaya di situs web atas nama pengguna. Atribut **SameSite** dapat digunakan untuk membatasi pengiriman cookies hanya dalam konteks yang sama, sehingga mencegah serangan ini.

Selain itu, cookies yang tidak dienkripsi dapat disadap oleh pihak ketiga jika transmisi data tidak menggunakan protokol **HTTPS**. Oleh karena itu, mengaktifkan atribut **Secure** untuk memastikan cookie hanya dikirim melalui koneksi terenkripsi sangat penting.

Dengan menjaga praktik keamanan seperti menggunakan atribut HttpOnly, SameSite, dan Secure, serta memastikan data dikirim melalui HTTPS, risiko penggunaan cookies dapat diminimalkan. Namun, pengembang harus tetap waspada terhadap potensi serangan yang memanfaatkan kelemahan dalam pengelolaan cookies.

**5\. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).**

- **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**

  Tahap pertama yang saya lakukan adalah membuat halaman registrasi bagi pengguna baru dengan memanfaatkan formulir bawaan Django, yaitu **UserCreationForm**. Saya menambahkan fungsi `register()` pada _views.py_ sehingga pengguna bisa membuat akun baru dan menyimpan informasi mereka ke dalam database. Setelah registrasi berhasil, saya menambahkan pesan konfirmasi dengan modul **messages**, dan pengguna akan diarahkan ke halaman login.

  Setelah menyelesaikan tahap registrasi, saya beralih ke penambahan fungsi login. Di sini, saya menggunakan **AuthenticationForm** untuk memvalidasi kredensial pengguna. Jika kredensial tersebut valid, saya menggunakan fungsi `login()` untuk mengautentikasi pengguna dan membuat sesi baru. Saya juga menghubungkan halaman login dengan HTML yang sederhana, yang berisi formulir login dan hyperlink ke halaman registrasi jika pengguna belum memiliki akun.

  Setelah berhasil mengimplementasikan login, saya menambahkan mekanisme logout. Pada bagian ini, saya membuat fungsi `logout_user()` untuk mengakhiri sesi pengguna dengan memanfaatkan fungsi **logout** bawaan Django. Setelah logout, pengguna akan diarahkan kembali ke halaman login, dan semua data sesi akan dihapus.

  Untuk meningkatkan keamanan, saya menggunakan **login_required** decorator untuk membatasi akses ke halaman utama hanya bagi pengguna yang sudah login. Ini memastikan bahwa hanya pengguna terautentikasi yang bisa mengakses konten tersebut. Terakhir, saya juga mempelajari bagaimana menggunakan cookies, seperti menyimpan informasi _last login_ di halaman utama. Saya menambahkan _cookie_ bernama **last_login** ketika pengguna berhasil login, yang kemudian dihapus saat mereka logout. Dengan demikian, saya dapat membangun sistem autentikasi yang aman dan fungsional untuk aplikasi Django saya.

- **Membuat dua akun pengguna dengan masing-masing tiga _dummy data_ menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**
  Saya membuat dua akun pengguna pada aplikasi yang saya bangun secara lokal. Saya memanfaatkan fitur _UserCreationForm_ dari Django untuk memudahkan pembuatan akun tersebut. Setelah itu, saya menjalankan aplikasi pada _local server_ dan melakukan registrasi untuk dua akun pengguna dengan informasi berbeda.

  Setelah akun pengguna selesai dibuat, saya login ke masing-masing akun dan memasukkan tiga data _dummy_ sesuai dengan model yang telah saya buat sebelumnya. Data ini meliputi atribut seperti nama, harga, kuantitas, dan deskripsi yang saya isi secara acak untuk setiap akun. Setelah itu, saya memastikan bahwa semua data _dummy_ yang dimasukkan berhasil disimpan ke dalam database lokal melalui ORM Django.

- **Menghubungkan model `Product` dengan `User`.**  
  Untuk menghubungkan model **Product** dengan **User** dalam aplikasi Django, saya mulai dengan menambahkan relasi yang sesuai pada model **Product**. Dalam file **models.py**, saya memperbarui model **Product** untuk mencakup field baru yang merujuk ke model **User**. Saya menggunakan `ForeignKey` untuk mendefinisikan hubungan satu-ke-banyak antara **User** dan **Product**, di mana satu pengguna bisa memiliki banyak produk. Field ini dinamai **user** dan dikonfigurasi sebagai opsional dengan parameter `null=True` dan `blank=True`. Dengan menambahkan field ini, setiap produk yang dibuat dalam aplikasi dapat dikaitkan dengan pengguna tertentu.  
  Setelah memperbarui model, saya melanjutkan dengan melakukan migrasi database untuk menerapkan perubahan tersebut. Proses ini melibatkan menjalankan perintah `python manage.py makemigrations` diikuti oleh `python manage.py migrate`, yang memastikan bahwa field **user** baru diterapkan ke skema database dan dapat digunakan dalam aplikasi.  
  Selanjutnya, saya perlu memperbarui formulir dan tampilan aplikasi untuk menghubungkan produk dengan pengguna yang sedang login. Dalam **views.py**, saya menambahkan logika untuk mengaitkan produk yang baru dibuat dengan pengguna saat ini. Ketika formulir produk dikirimkan, field **user** diisi secara otomatis dengan informasi pengguna yang sedang login, memastikan bahwa setiap produk yang ditambahkan oleh pengguna terkait dengan akun mereka.  
  Terakhir, untuk menampilkan produk yang sesuai dengan pengguna yang sedang login, saya memperbarui tampilan produk dengan memfilter query berdasarkan pengguna saat ini. Dalam **views.py**, saya menambahkan logika untuk hanya menampilkan produk yang dimiliki oleh pengguna yang sedang login.
- **Menampilkan detail informasi pengguna yang sedang _logged in_ seperti _username_ dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.**  
  Langkah pertama yang saya ambil adalah memperbarui tampilan halaman utama aplikasi untuk menampilkan nama pengguna yang saat ini sedang login. Dengan memanfaatkan **request.user** di dalam view, saya bisa mendapatkan informasi tentang pengguna yang sedang aktif dan meneruskannya ke template HTML. Di template, saya menampilkan nama pengguna dengan menggunakan sintaks **{{ user.username }}**, sehingga pengguna dapat melihat informasi pribadi mereka secara langsung.  
  Selanjutnya, saya fokus pada implementasi cookies untuk meningkatkan pengalaman pengguna. Saya menambahkan cookie bernama **last_login** pada halaman utama aplikasi. Untuk melakukan ini, saya memperbarui fungsi view untuk menyertakan logika yang menyimpan informasi _last login_ setiap kali pengguna berhasil login. Saya menggunakan **HttpResponse** untuk mengatur cookie dan **request.COOKIES** untuk membaca nilai cookie yang sudah ada. Pada saat login, cookie **last_login** diatur dengan nilai waktu saat login terjadi, dan informasi ini ditampilkan pada halaman utama jika cookie tersebut tersedia. Selain itu, saya memastikan bahwa cookie ini dihapus saat pengguna logout untuk menjaga keamanan data.

Dua akun pengguna dengan masing-masing tiga dummy data
![image](https://github.com/user-attachments/assets/d62f5ae6-938a-4a20-a71d-dc2c49d164c7)
![image](https://github.com/user-attachments/assets/b480c8e5-7614-4808-b616-eec6646f0f8b)

</details>

<details>
  <summary>TUGAS 5</summary>
  

**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Pertama, browser akan mempertahankan gaya yang didefinisikan langsung di dalam elemen HTML menggunakan atribut style. Ini disebut sebagai gaya inline. Kemudian, browser akan mempertahankan gaya yang didefinisikan menggunakan selector ID, yaitu selector yang menggunakan simbol # untuk menargetkan elemen dengan atribut id tertentu.

Selanjutnya, browser akan mempertahankan gaya yang didefinisikan menggunakan selector kelas, atribut, dan pseudo-kelas. Selector kelas menggunakan simbol . untuk menargetkan elemen dengan atribut class tertentu, sedangkan selector atribut dan pseudo-kelas menargetkan elemen berdasarkan atribut atau pseudo-kelasnya (contohnya :hover, :active, dan lain-lain). Terakhir, browser akan mempertahankan gaya yang didefinisikan menggunakan selector elemen dan pseudo-elemen. Selector elemen menargetkan elemen berdasarkan nama tag-nya, sedangkan selector pseudo-elemen menargetkan elemen berdasarkan pseudo-elemen (contohnya :before, :after, dan lain-lain).

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

Responsive design adalah konsep yang penting dalam pengembangan aplikasi web karena memungkinkan website untuk menyesuaikan tampilan dan layoutnya berdasarkan ukuran layar dan perangkat yang digunakan. Ini sangat penting karena:

-   Saat ini, pengguna menggunakan berbagai perangkat seperti smartphone, tablet, laptop, dan desktop untuk mengakses website. Responsive design memastikan bahwa website dapat menyesuaikan diri dengan ukuran layar dan perangkat yang berbeda.
-   Dengan responsive design, pengguna dapat memiliki pengalaman yang lebih baik ketika mengakses website karena tampilan dan layoutnya dapat menyesuaikan dengan perangkat yang digunakan.
-   Responsive design memungkinkan website dapat diakses dengan mudah dan nyaman dari berbagai perangkat, sehingga meningkatkan kemudahan akses bagi pengguna.
    

Contoh Aplikasi yang Sudah Menerapkan Responsive Design
-   Instagram
-   Twitter
  
Contoh Aplikasi yang Belum Menerapkan Responsive Design
-   DJP Online
-   Craiglist
    

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Dalam CSS, margin, border, dan padding adalah tiga properti yang digunakan untuk mengatur layout dan tampilan elemen HTML.

-   Margin adalah ruang kosong di sekitar elemen HTML yang memisahkan elemen dari elemen lainnya. Margin dapat digunakan untuk mengatur jarak antara elemen dengan elemen lainnya.
-   Border adalah garis yang mengelilingi elemen HTML. Border dapat digunakan untuk mengatur ketebalan, gaya, dan warna garis yang mengelilingi elemen.
-   Padding adalah ruang kosong di dalam elemen HTML yang memisahkan konten dari border. Padding dapat digunakan untuk mengatur jarak antara konten dengan border.
    
Cara Mengimplementasikan Margin, Border, dan Padding

```bash
box  {
/*  Margin  */
margin:  20px; /*  mengatur  jarak  20px  dari  elemen  lainnya  */

/*  Border  */
border:  1px  solid  #000; /* mengatur ketebalan 1px, gaya solid, dan warna hitam */

/*  Padding  */
padding:  10px; /*  mengatur  jarak  10px  dari  konten  dengan  border  */
```
Dalam contoh di atas, saya mengatur margin 20px, border dengan ketebalan 1px, gaya solid, dan warna hitam, serta padding 10px untuk elemen dengan class .box.


**Jelaskan konsep flex box dan grid layout beserta kegunaannya**

Flexbox (Flexible Box Layout)

Flexbox adalah metode CSS yang dirancang untuk membuat tata letak yang lebih fleksibel dan responsif dalam satu dimensi, baik horizontal (baris) atau vertikal (kolom). Flexbox memungkinkan elemen-elemen dalam container (flex container) untuk disusun dan disesuaikan dengan mudah sesuai dengan ruang yang tersedia.

Cara Kerja Flexbox:
Flexbox beroperasi berdasarkan dua komponen utama:
-   Flex Container: Elemen yang mengandung elemen-elemen lain yang disebut Flex Items. Container ini diatur menggunakan display: flex;.
-   Flex Items: Elemen-elemen di dalam flex container yang disusun sesuai dengan aturan Flexbox.
    

Beberapa properti dalam Flexbox:
-   flex-direction: Mengatur arah susunan elemen. Bisa dalam arah baris (default: row) atau kolom (column).
-   justify-content: Mengatur bagaimana elemen-elemen dalam flex container diatur secara horizontal (misal: center, space-between, flex-end).
-   align-items: Mengatur perataan elemen secara vertikal (misal: stretch, center, flex-start).
-   flex-wrap: Mengatur apakah elemen akan dipaksa berada dalam satu baris atau dapat dilipat ke baris berikutnya jika ruang tidak mencukupi.
    

Kegunaan Flexbox:
-   Memudahkan dalam pengaturan elemen yang fleksibel dan responsif, terutama ketika elemen-elemen perlu menyesuaikan ruang yang tersedia.
-   Setiap elemen dalam flex container dapat memiliki ukuran yang dinamis, tergantung pada konten atau pengaturan tata letak.
-   Cocok untuk membuat elemen-elemen menyesuaikan diri di dalam container yang berubah ukurannya, seperti pada tampilan responsif.
    

Grid Layout
 
Grid Layout adalah metode CSS yang memungkinkan tata letak dalam dua dimensi (baris dan kolom). Dengan Grid Layout, elemen-elemen web dapat diatur lebih terstruktur dengan menggunakan grid, seperti tabel, tetapi dengan lebih banyak fleksibilitas.

Cara Kerja Grid Layout:
Grid Layout memungkinkan untuk membuat grid yang terdiri dari kolom dan baris, di mana setiap elemen dapat ditempatkan secara presisi.

Beberapa properti penting dalam Grid Layout:
-   display: grid: Mengaktifkan mode Grid pada container.
-   grid-template-columns dan grid-template-rows: Mengatur berapa banyak kolom dan baris yang akan dimiliki grid, serta ukuran masing-masing kolom dan baris.
-   grid-column dan grid-row: Mengatur posisi elemen dalam grid, misalnya elemen mana yang menempati kolom pertama atau baris kedua.
-   grid-gap atau gap: Memberikan jarak antara baris dan kolom dalam grid.
    

Kegunaan Grid Layout:
-   Mempermudah pembuatan tata letak yang lebih terstruktur, di mana elemen-elemen bisa ditempatkan dalam beberapa baris dan kolom.
-   Fleksibilitas tinggi dalam mengatur ukuran dan penempatan elemen sesuai dengan grid yang telah ditentukan.
-   Grid sangat ideal untuk membuat halaman web yang memiliki banyak bagian dengan susunan yang simetris dan teratur.
    

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**


**Implementasikan fungsi untuk menghapus dan mengedit product.**

Implementasi Fitur Edit Product
Untuk menambahkan fitur edit produk pada aplikasi, saya memulai dengan membuka berkas views.py yang terletak di subdirektori main. Di sini, saya membuat fungsi baru bernama edit_product yang menerima dua parameter: request dan id. Fungsi ini bertujuan untuk mengambil entri product berdasarkan ID yang diberikan. Saya menggunakan Product.objects.get(pk=id) untuk mendapatkan entri tersebut. Setelah itu, saya membuat instance dari ProductEntryForm, dengan mengisi data yang telah diambil sebelumnya. Ini memungkinkan form untuk menampilkan data yang sudah ada sehingga pengguna dapat mengeditnya.

Selanjutnya, saya menambahkan logika untuk memproses pengiriman form. Jika form valid dan metode yang digunakan adalah POST, saya menyimpan perubahan dengan memanggil form.save(), dan mengarahkan kembali pengguna ke halaman utama dengan menggunakan HttpResponseRedirect(reverse('main:show_main')). Jika form tidak valid atau metode bukan POST, saya menyiapkan konteks yang berisi form untuk ditampilkan pada template edit_product.html. Akhirnya, saya merender template dengan mengirimkan konteks yang telah disiapkan.

Setelah itu, saya perlu menambahkan import yang diperlukan di bagian atas berkas views.py, yaitu from django.shortcuts import render, reverse dan from django.http import HttpResponseRedirect. Ini penting agar fungsi yang saya buat dapat bekerja dengan baik dan dapat mengakses fitur-fitur yang diperlukan dari Django.

Implementasi Template Edit Product
Langkah selanjutnya adalah membuat berkas template baru bernama edit_product.html di subdirektori main/templates. Dalam berkas ini, saya menggunakan sintaks templating Django untuk memperluas base.html. Di dalam blok konten, saya membuat form yang menggunakan metode POST. Form ini dilengkapi dengan token CSRF untuk keamanan. Saya memanfaatkan {{ form.as_table }} untuk menampilkan field dari form dalam format tabel, dan menambahkan tombol submit untuk mengedit product.

Penambahan URL untuk Edit Product
Selanjutnya, saya membuka berkas urls.py yang terletak di direktori main untuk menambahkan rute yang akan mengarahkan pengguna ke fungsi edit_product yang baru saja saya buat. Saya mengimpor fungsi tersebut menggunakan from main.views import edit_product. Kemudian, saya menambahkan path baru ke dalam urlpatterns, yang memungkinkan akses ke fungsi edit_product dengan URL yang sesuai, misalnya path('edit-product/<uuid:id>', edit_product, name='edit_product'). 

Penambahan Tombol Edit di Box Product
Setelah menyiapkan fitur edit, saya melanjutkan dengan membuka berkas card_product.html. Di sini, saya menambahkan tombol Edit pada box product yang menampilkan terkait informasi product tertentu. Dengan menambahkan potongan kode yang sesuai, saya memastikan bahwa tombol tersebut mengarahkan pengguna ke halaman edit product dengan menyertakan primary key dari entri yang bersangkutan dalam URL. Saya menggunakan sintaks {% url 'main:edit_product' product.pk %} untuk membangun URL yang dinamis.

Implementasi Fitur Hapus Product
Pertama, saya membuat fungsi baru bernama delete_product di views.py. Fungsi ini juga menerima parameter request dan id, dan berfungsi untuk menghapus entri product berdasarkan ID yang diberikan. Dalam fungsi ini, saya memanggil ProductEntry.objects.get(pk=id) untuk mengambil entri product yang akan dihapus, dan kemudian memanggil metode delete() pada objek tersebut untuk menghapusnya dari database. Setelah penghapusan berhasil, saya mengarahkan pengguna kembali ke halaman utama.

Penambahan URL untuk Hapus Product
Saya kemudian membuka kembali berkas urls.py untuk mengimpor fungsi delete_product yang telah saya buat, dan menambahkan path baru untuk mengakses fungsi ini, mirip dengan proses yang saya lakukan untuk fungsi edit_product.

Penambahan Tombol Hapus di Box Product
Untuk melengkapi implementasi ini, saya membuka kembali berkas card_product.html dan menambahkan tombol Hapus pada box product yang menampilkan terkait informasi product tertentu. Saya menggunakan sintaks {% url 'main:delete_product' product.pk %} untuk membangun URL untuk fungsi hapus, sehingga pengguna dapat menghapus entri product yang diinginkan dengan mudah.

  
**Kustomisasi halaman login, register, dan tambah product semenarik mungkin.**
Pada halaman login, saya menggunakan Tailwind untuk mengatur warna latar belakang halaman dan elemen form gray-100, serta memastikan responsivitasnya dengan kelas seperti flex, justify-center, dan items-center. Saya menambahkan margin dan padding yang tepat menggunakan utilitas py, px, dan mt untuk mengatur jarak antar elemen sehingga tampilannya lebih rapi dan terstruktur. Pada bagian input form seperti username dan password, saya menggunakan Tailwind untuk memberi warna placeholder dan efek hover yang memperjelas interaksi pengguna, dan pada tombol Sign-in saya juga memberikan background dan efek hover.

Pada halaman register, elemen-elemen form ditempatkan secara terpusat dengan memanfaatkan fitur flex, items-center, dan justify-center, yang membuat tampilan lebih rapi dan seimbang. Latar belakang halaman menggunakan warna (bg-gray-100) untuk membuat elemen form yang dibatasi oleh border abu-abu (border-gray-300) dan latar belakang putih (bg-white). Saya juga menambahkan judul form dengan ukuran teks yang besar (text-3xl font-extrabold) serta jarak antar field input yang rapi menggunakan mt-4, sehingga pengguna dapat dengan mudah memahami dan mengisi setiap bagian form.

Selain itu, saya menampilkan pesan error menggunakan teks merah (text-red-600) dan ikon peringatan berbentuk svg di sebelah kanan input yang memiliki error. Tombol submit (Register) didesain dengan warna bg-cyan-400 yang berubah menjadi lebih gelap saat di-hover. Terakhir, saya menyertakan link ke halaman login bagi pengguna yang sudah memiliki akun, dengan gaya teks biru yang lebih terang saat di-hover (hover:text-blue-500), untuk memudahkan navigasi.

Pada halaman tambah produk,  saya membuat judul dengan ukuran teks besar (text-3xl font-bold) agar pengguna segera mengetahui fungsi halaman. Bagian utama dari form ditempatkan di dalam container yang memiliki padding dan jarak yang cukup besar untuk memastikan setiap elemen mudah diakses dan terlihat rapi. Elemen input dari form masing-masing diberi label yang jelas dengan teks font-semibold, memastikan bahwa pengguna bisa mengerti fungsi dari setiap field. Selain itu, form diatur menggunakan sistem kolom (flex flex-col), sehingga setiap input diletakkan vertikal satu per satu untuk memudahkan pengisian.

Saya juga menambahkan pesan kesalahan (jika ada) yang ditampilkan dalam warna merah (text-red-600) dibawah input yang salah, serta teks bantuan (help_text) yang muncul dengan warna abu-abu terang (text-gray-500). Tombol submit pada halaman ini menggunakan warna bg-cyan-400 yang akan berubah menjadi lebih gelap saat pengguna meng-hover tombol tersebut.

**Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:**

**Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.**

Pertama, dalam menangani situasi ketika tidak ada produk yang tersimpan, saya menggunakan struktur kondisi yang mengandalkan Django template tags. Dengan menggunakan {% if not products %}, saya memastikan bahwa jika belum ada produk yang terdaftar, halaman akan menampilkan gambar sedih yang diambil dari folder static/image dan pesan yang sesuai. Di bagian ini, saya menciptakan elemen dengan class flex, flex-col, items-center, dan justify-center, yang membantu menyusun konten secara vertikal di tengah halaman. Gambar dan teks diletakkan dalam div dengan padding yang cukup (p-6) agar tampak lebih rapi dan terpusat.

Ketika produk tersedia, saya menggunakan grid untuk menampilkan detail setiap produk dengan cara yang menarik. Saya menggunakan {% for product in products %} untuk mengulangi setiap produk dan menyertakan template card_product.html, yang mendefinisikan bagaimana setiap produk harus ditampilkan. Saya menggunakan grid Tailwind dengan pengaturan grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 yang memungkinkan tampilan produk beradaptasi dengan ukuran layar. Dengan cara ini, pada layar kecil, setiap produk akan ditampilkan satu per satu, sedangkan pada layar yang lebih besar, produk dapat ditampilkan dalam dua atau tiga kolom. Saya juga menggunakan kelas gap-6 untuk memberikan ruang antar card.  

**Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!**  

Pada template card_product.html, dua tombol utama untuk fungsi "Edit" dan "Delete" disusun dengan elemen a, yang berfungsi sebagai tautan dengan tampilan seperti tombol. Tombol "Edit" memiliki kelas bg-cyan-500 text-white rounded-lg py-2 px-4, yang menetapkan latar belakang berwarna cyan, teks putih, dan sudut membulat, serta memberikan padding vertikal (py-2) dan horizontal (px-4) untuk ukuran tombol yang sesuai. Lalu saya menambahkan hover:bg-cyan-600 yang mengubah warna latar belakang saat dihover, sementara hover:shadow-lg dan hover:-translate-y-1 menambahkan bayangan dan sedikit pergerakan vertikal. Tautan mengarah ke halaman edit produk melalui {% url 'main:edit_product' product.pk %} yang menghasilkan URL dinamis berdasarkan primary key produk.

Tombol "Delete" memiliki struktur yang serupa dengan tombol "Edit", namun menggunakan warna merah dengan kelas bg-red-600. Saat dihover, kelas hover:bg-red-700 mengganti warna latar belakang menjadi lebih gelap. Kelas-kelas yang digunakan seperti rounded-lg, py-2 px-4, dan shadow-md memastikan bahwa kedua tombol memiliki ukuran dan gaya yang konsisten, namun dengan skema warna yang berbeda. Selain itu, setiap tombol dilengkapi dengan aria-label, misalnya aria-label="Edit {{ product.name }}", yang menambah elemen aksesibilitas untuk pengguna pembaca layar, memberikan penjelasan yang lebih informatif mengenai tombol dan fungsinya.

Kedua tombol ini diletakkan dalam div dengan kelas flex justify-around items-center mt-4, yang memberikan penataan yang rapi dan memastikan bahwa kedua tombol terpisah dengan jarak yang cukup untuk meningkatkan keterbacaan dan aksesibilitas. 

**Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.**

Navbar saya implementasikan pada navbar.html. navbar.html saya buat pada direktori templates yang global, agar navbar dapat diakses oleh seluruh halaman yang ada (bukan hanya pada app main). Pada bagian atas, kelas bg-gradient-to-r from-cyan-500 to-purple-500 memberikan efek gradient dari warna cyan ke ungu, sementara shadow-lg menambahkan bayangan. Dengan pengaturan fixed top-0 left-0 z-40 w-screen, navbar tetap terlihat di bagian atas layar saat pengguna menggulir (scroll) halaman, memberikan akses cepat ke menu navigasi.

Lalu saya menggunakan kelas flex, items-center, dan justify-between untuk menyusun elemen dalam navbar. Kelas max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 membatasi lebar maksimum navbar dan memusatkan kontennya. Untuk menjadikan navbar responsif, saya menerapkan kelas hidden md:flex pada bagian tautan navigasi desktop. Ini berarti tautan tersebut hanya akan ditampilkan pada perangkat dengan ukuran medium (md) dan lebih besar, sementara pada perangkat kecil, tautan tersebut disembunyikan. Sebagai gantinya, menu mobile yang lebih sederhana ditampilkan dengan mobile-menu, yang juga menggunakan kelas hidden md:hidden agar tidak terlihat pada layar lebih besar.

Pada bagian autentikasi pengguna, saya menggunakan conditional rendering dengan sintaks Django templating {% if user.is_authenticated %} untuk menampilkan pesan sambutan dan tombol logout jika pengguna sudah masuk. Jika tidak, tombol login dan registrasi akan ditampilkan. Tombol menu mobile, yang ditandai dengan ikon burger dalam SVG JavaScript sederhana juga ditambahkan untuk menangani toggle kelas hidden pada menu mobile saat tombol ditekan.

</details>

<details>
  <summary>TUGAS 6</summary>
  
**Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web\!**  
JavaScript memiliki peran yang sangat penting dalam pengembangan aplikasi web karena kemampuannya untuk berjalan di sisi klien (client-side), memungkinkan interaktivitas tinggi dan pengalaman pengguna yang responsif. Dengan JavaScript, elemen pada halaman web dapat diperbarui secara dinamis tanpa perlu memuat ulang seluruh halaman, berkat teknologi seperti AJAX dan Fetch API. JavaScript juga memungkinkan manipulasi DOM secara langsung, membuatnya mudah untuk mengubah struktur, konten, atau gaya halaman secara real-time. Selain itu, ekosistem JavaScript yang luas dengan banyak framework dan library, seperti React, Angular, dan Vue, memfasilitasi pengembangan aplikasi web yang skalabel dan efisien. Di sisi server, dengan adanya Node.js, JavaScript juga memungkinkan pengembang untuk menggunakan bahasa yang sama untuk front-end dan back-end, menyederhanakan alur kerja dan kolaborasi tim. Fleksibilitas dan kapabilitas lintas platformnya menjadikannya pilihan utama dalam pengembangan aplikasi web modern.

**Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`\! Apa yang akan terjadi jika kita tidak menggunakan `await`?**

Fungsi `await` ketika digunakan dengan `fetch()` adalah untuk menunggu hasil dari *promise* yang dikembalikan oleh `fetch()` sebelum melanjutkan ke baris kode berikutnya. `fetch()` bekerja secara asinkron, artinya akan segera mengembalikan *promise* yang menunggu respons dari server, tanpa menghentikan eksekusi kode. Dengan `await`, kita bisa menunggu hingga respons diterima dan diproses sebelum melanjutkan, sehingga kita bisa bekerja dengan data yang sudah tersedia.

Jika kita tidak menggunakan `await`, kode akan terus berjalan tanpa menunggu hasil dari `fetch()`, sehingga kita mungkin mencoba menggunakan data yang belum siap (karena *promise* belum terselesaikan). Ini dapat menyebabkan perilaku tak terduga atau *errors* karena data belum diambil ketika kode lain mencoba mengaksesnya.

**Mengapa kita perlu menggunakan *decorator* `csrf_exempt` pada *view* yang akan digunakan untuk AJAX `POST`?**

Kita perlu menggunakan decorator `@csrf_exempt` pada view yang digunakan untuk AJAX POST karena mekanisme *Cross-Site Request Forgery* (CSRF) di Django secara default mengharuskan setiap permintaan POST, termasuk AJAX, menyertakan token CSRF yang valid sebagai tindakan keamanan. Token ini digunakan untuk memastikan bahwa permintaan yang dikirim berasal dari sumber yang sah, bukan dari situs lain yang mencoba melakukan serangan CSRF.

Namun, dalam beberapa kasus, terutama saat menangani permintaan AJAX POST dari sumber eksternal atau ketika kita tidak mengirimkan token CSRF, Django akan menolak permintaan POST jika tidak ada token CSRF atau jika token tersebut tidak valid. Untuk mencegah pemeriksaan CSRF pada view tertentu, kita bisa menambahkan decorator `@csrf_exempt`, yang memberitahu Django agar tidak memverifikasi token CSRF untuk permintaan tersebut. 

**Pada tutorial PBP minggu ini, pembersihan data *input* pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?**

Pembersihan data input pengguna perlu dilakukan di backend karena backend adalah tempat yang lebih aman dan andal untuk validasi, meskipun kita bisa melakukan validasi di frontend. Validasi di frontend bisa dimanipulasi oleh pengguna yang mencoba menghindari aturan atau melakukan serangan berbahaya, seperti mengubah kode JavaScript atau mematikan validasi browser. Oleh karena itu, backend harus selalu memverifikasi dan membersihkan data untuk memastikan keamanan aplikasi, mencegah serangan seperti *SQL Injection* atau *XSS* (Cross-Site Scripting), serta menjaga integritas data. Dengan melakukan validasi di backend, kita memastikan bahwa data yang diproses oleh server selalu valid dan aman.

**Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)\!**

**Ubahlah kode `cards` data *mood* agar dapat mendukung AJAX `GET`.**

Saya mengimplementasikan AJAX GET untuk mendukung pengambilan data produk dengan mengubah beberapa bagian kode pada file `views.py`. Pertama, saya menghapus kode yang mengirimkan data produk langsung ke template, dan menggantinya dengan endpoint `show_json` yang mengembalikan data produk dalam format JSON. Dalam fungsi `show_json`, saya menggunakan `Product.objects.filter(user=request.user)` untuk mengambil produk yang dimiliki oleh pengguna yang sedang login dan mengembalikannya dalam format JSON menggunakan `HttpResponse`. Selanjutnya, di frontend, pada file `main.html`, saya menambahkan div dengan ID `product_entry_cards` untuk menampung data produk. Saya membuat fungsi `getMoodEntries()` yang menggunakan `fetch()` untuk mengambil data dari endpoint `show_json`. Fungsi ini kemudian dipanggil oleh `refreshProductEntries()`, yang memeriksa apakah ada produk yang diterima. Jika tidak ada produk, pesan "Belum ada produk" akan ditampilkan; jika ada, data produk ditampilkan dalam format kartu (card) dengan menggunakan template string untuk membangun HTML secara dinamis. 

**Lakukan pengambilan data *mood* menggunakan AJAX `GET`. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang *logged-in*.**  
Pada fungsi `show_json` di file `views.py`, pemfilteran data dilakukan dengan sintaks `data = Product.objects.filter(user=request.user)`, yang mengambil semua objek `Product` yang terasosiasi dengan pengguna yang sedang login (diwakili oleh `request.user`). Dengan cara ini, hanya entri produk yang dimiliki oleh pengguna yang terautentikasi yang akan diambil dari basis data. Dalam skrip JavaScript pada `main.html`, implementasi pengambilan data mood menggunakan AJAX GET dapat dilakukan dengan memanfaatkan fungsi `getProductEntries()`, yang menggunakan metode `fetch()` untuk mengakses URL yang ditentukan oleh Django (melalui `{% url 'main:show_json' %}`). Fungsi ini mengharuskan server untuk mengembalikan data dalam format JSON, yang kemudian diolah menjadi objek JavaScript menggunakan `.json()`. Setelah data diterima, fungsi `refreshProductEntries()` memanggil `getProductEntries()` untuk memperbarui tampilan dengan memasukkan data ke dalam elemen HTML yang sesuai, yang hanya akan menampilkan entri produk milik pengguna yang terautentikasi.

### **Buatlah fungsi *view* baru untuk menambahkan *mood* baru ke dalam basis data.**

Saya membuat fungsi `add_product_entry_ajax` dalam file `views.py`. Fungsi ini bertugas untuk menangani permintaan POST yang dikirimkan dari klien (frontend) ketika pengguna ingin menambahkan produk baru. Sintaks `@csrf_exempt` dan `@require_POST` digunakan untuk memastikan bahwa fungsi ini hanya bisa diakses melalui permintaan POST dan juga untuk menonaktifkan perlindungan CSRF untuk keperluan pengujian (meskipun sebaiknya menggunakan perlindungan CSRF dalam aplikasi nyata). Di dalam fungsi, saya menggunakan `request.POST.get()` untuk mengambil data harga, kuantitas, dan deskripsi dari form yang dikirimkan. Setelah itu, produk baru dibuat dengan menggunakan model `Product`, yang merupakan representasi dari tabel produk dalam database, dan disimpan dengan metode `save()`. Fungsi ini mengembalikan respons HTTP dengan status 201 (CREATED) sebagai tanda bahwa produk baru berhasil ditambahkan.

**Buatlah *path* `/create-ajax/` yang mengarah ke fungsi *view* yang baru kamu buat.**

Pada file `urls.py`, dalam konteks penambahan produk melalui AJAX, saya menambahkan path baru menggunakan fungsi `path()`. Sintaks `path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax')` ini menetapkan rute untuk URL `/create-product-entry-ajax`, yang akan memanggil fungsi `add_product_entry_ajax` dari `main.views` ketika URL tersebut diakses. Dengan menggunakan `name='add_product_entry_ajax'`, saya memberikan nama pada rute ini, sehingga dapat dirujuk di dalam template dan JavaScript kode saya.

### **Hubungkan form yang telah kamu buat di dalam modal kamu ke *path* `/create-ajax/`.**

Dalam `main.html`, saya menghubungkan form `#productEntryForm` ke path `/create-ajax/` dengan menggunakan `fetch` di fungsi JavaScript `addProductEntry()`. Fungsi ini memanggil endpoint yang telah saya buat dengan menggunakan method POST, mengirimkan data form yang diambil melalui `new FormData(document.querySelector('#productEntryForm'))`. Sintaks `fetch("{% url 'main:add_product_entry_ajax' %}", {...})` mengarahkan permintaan ke URL yang sesuai dengan nama yang telah ditentukan dalam `urls.py`. Setelah produk berhasil ditambahkan, form akan direset, dan modal akan ditutup.

### **Lakukan *refresh* pada halaman utama secara asinkronus untuk menampilkan daftar *mood* terbaru tanpa reload halaman utama secara keseluruhan.**

Untuk menampilkan daftar produk terbaru tanpa me-reload halaman utama, saya menggunakan fungsi `refreshProductEntries()`. Dalam fungsi ini, saya memanggil `getProductEntries()` yang mengirimkan permintaan ke endpoint `show_json`. Setelah menerima respons berupa data produk dalam format JSON, saya mengupdate elemen HTML dengan ID `product_entry_cards` untuk menampilkan daftar produk yang baru. Proses ini dilakukan dengan mengosongkan elemen HTML terlebih dahulu, kemudian membangun string HTML baru berdasarkan data yang diterima, dan akhirnya menetapkan `innerHTML` elemen tersebut. 


</details>
