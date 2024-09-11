# Tech Trove
Asyer Samuel Marpaung
2306165925


PWS : http://asyer-samuel-techtrove.pbp.cs.ui.ac.id/

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

  

-   Membuat Sebuah Proyek Django Baru
    

Saya memulai dengan mengatur lingkungan kerja menggunakan virtual environment. Ini dilakukan dengan membuat lingkungan virtual menggunakan perintah python -m venv env, kemudian saya mengaktifkan environment tersebut. Setelah itu, saya menginstal Django dengan perintah pip install django. Langkah selanjutnya adalah membuat proyek baru dengan menjalankan perintah django-admin startproject tech_trove. Ini membuat struktur dasar proyek Django yang berisi direktori dan file utama seperti settings.py, urls.py, dan wsgi.py.

  

-   Membuat Aplikasi dengan Nama main
    

Saya membuat aplikasi baru di dalam proyek dengan menjalankan perintah python manage.py startapp main. Setelah aplikasi main dibuat, saya menambahkannya ke dalam daftar INSTALLED_APPS di file settings.py proyek. Hal ini penting untuk memastikan aplikasi dapat dikenali oleh Django saat aplikasi berjalan.

  

-   Melakukan Routing pada Proyek
    

Setelah aplikasi main dibuat, saya perlu memastikan bahwa aplikasi tersebut dapat diakses melalui URL tertentu. Untuk itu, saya menambahkan routing pada urls.py proyek utama. Saya menggunakan fungsi include() untuk menghubungkan routing dari proyek utama ke aplikasi main. Routing ini memastikan bahwa semua URL yang ditujukan ke aplikasi main akan diarahkan ke file urls.py dari aplikasi tersebut.

  

-   Membuat Model Product pada Aplikasi main
    

Pada tahap ini, saya membuat model Product di dalam file models.py di aplikasi main. Model ini memiliki tiga atribut wajib yaitu name, price, dan description. Saya menggunakan CharField untuk atribut name, IntegerField untuk atribut price, dan TextField untuk atribut description. Saya juga menambahkan fungsi **str**() untuk mengembalikan representasi string dari nama produk. Setelah model dibuat, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate untuk membuat dan menerapkan perubahan database yang sesuai dengan model tersebut.

  

-   Membuat Fungsi di views.py
    

Selanjutnya, saya membuat fungsi di file views.py yang mengembalikan template HTML dengan informasi yang diminta. Fungsi ini mengembalikan nama e-commerce, nama, dan kelas, lalu mengirimkannya sebagai konteks ke template HTML. Saya membuat file template di dalam direktori templates untuk memastikan struktur aplikasi mengikuti standar Django, dan template tersebut menerima data dari konteks yang dikirimkan oleh views.

  

-   Membuat Routing di urls.py Aplikasi main
    

Saya membuat file urls.py di dalam aplikasi main (jika belum ada) dan mendefinisikan URL pattern untuk memetakan fungsi yang ada di views.py. Ini memungkinkan fungsi yang telah dibuat untuk diakses melalui URL yang ditentukan. Dengan menghubungkan URL pattern ke fungsi di views, saya memastikan web dapat merespons request dari user dengan benar.

  

-   Melakukan Deployment ke PWS
    

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
