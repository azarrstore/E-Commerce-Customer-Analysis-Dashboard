# 📊 E-Commerce Customer Analysis Dashboard

Dashboard ini menyajikan hasil analisis data transaksi e-commerce menggunakan pendekatan **RFM Analysis** dan **Cohort Retention Analysis**. Proyek ini dibuat sebagai bagian dari submission kelas **Proyek Analisis Data (Dicoding)**.

---

## 🔍 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis perilaku pelanggan pada platform e-commerce berdasarkan data transaksi. Analisis dilakukan untuk:
- Mengelompokkan pelanggan berdasarkan nilai bisnisnya (RFM).
- Mengidentifikasi segmen pelanggan dengan kontribusi pendapatan terbesar.
- Menganalisis tingkat retensi pelanggan dari waktu ke waktu menggunakan cohort analysis.

Hasil analisis disajikan dalam bentuk **dashboard interaktif** menggunakan **Streamlit**, sehingga insight dapat dipahami dengan lebih mudah.

---

## 📁 Struktur Proyek
```

submission/
├── data/
│   ├── customers_dataset.csv
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   └── order_payments_dataset.csv
├── dashboard/
│   ├── rfm_data.csv
│   ├── revenue_by_segment.csv
│   ├── retention.csv
│   └── dashboard.py
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt

````

---

## 🧠 Metodologi Analisis
1. **Gathering & Assessing Data**  
   Menggunakan dataset e-commerce mentah (asli) yang disediakan oleh Dicoding.

2. **Data Cleaning & Wrangling**  
   Penghapusan duplikasi, penanganan missing value, konversi tipe data, serta penggabungan tabel.

3. **Exploratory Data Analysis (EDA)**  
   Analisis tren transaksi dan distribusi nilai pembelian.

4. **RFM Analysis (Non-Machine Learning)**  
   Segmentasi pelanggan berdasarkan Recency, Frequency, dan Monetary.

5. **Cohort & Retention Analysis**  
   Analisis tingkat retensi pelanggan dari waktu ke waktu.

---

## ▶️ Menjalankan Dashboard Secara Lokal
1. Clone repository ini:
   ```bash
   git clone https://github.com/username/nama-repo.git
   cd submission
````

2. Install dependency:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan dashboard:

   ```bash
   python -m streamlit run dashboard/dashboard.py
   ```

Dashboard akan terbuka otomatis di browser.

---

## ☁️ Deploy ke Streamlit Community Cloud

Dashboard ini dapat dideploy menggunakan **Streamlit Community Cloud** dengan langkah berikut:

1. Pastikan proyek sudah di-push ke GitHub.
2. Masuk ke [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Hubungkan akun GitHub dan pilih repository ini.
4. Set **Main file path** ke:

   ```
   dashboard/dashboard.py
   ```
5. Klik **Deploy**.

---

## 📌 Catatan Penting

* Dataset yang digunakan adalah **dataset mentah** (belum dimodifikasi).
* Tidak menggunakan algoritma machine learning.
* Analisis lanjutan dilakukan menggunakan pendekatan non-ML sesuai ketentuan Dicoding.

---

## ✍️ Author

Disusun Erlangga Azhar sebagai bagian dari submission kelas **Proyek Analisis Data – Dicoding**.
