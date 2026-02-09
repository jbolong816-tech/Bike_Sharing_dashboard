# 🚲 Bike Sharing Dashboard

Proyek ini bertujuan untuk melakukan **analisis data penyewaan sepeda** menggunakan **Bike Sharing Dataset** serta menyajikan hasil analisis dalam bentuk **dashboard interaktif** menggunakan **Streamlit**.

Dashboard ini membantu pengguna memahami pola penyewaan sepeda berdasarkan waktu, musim, dan tren harian.

---

## 📌 Tujuan Proyek

1. Melakukan seluruh proses analisis data, meliputi:
   - Data Gathering
   - Data Cleaning
   - Exploratory Data Analysis (EDA)
2. Menjawab pertanyaan bisnis berdasarkan data.
3. Menyajikan insight hasil analisis dalam bentuk dashboard interaktif.

---

## ❓ Pertanyaan Bisnis

1. Bagaimana pengaruh **musim** terhadap jumlah penyewaan sepeda?
2. Bagaimana **tren penyewaan sepeda harian** pada periode waktu tertentu?

---

## 📂 Struktur Folder

```
proyek_analisis_data/
│── dashboard.py
│── main_data.csv
│── README.md
│── requirements.txt
```

---

## ⚙️ Setup Environment

### Menggunakan Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Shell / Terminal

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Dashboard

Pastikan Anda berada pada folder yang berisi file `dashboard.py` dan `main_data.csv`.

```bash
cd proyek_analisis_data
streamlit run dashboard.py
```

Setelah perintah dijalankan, dashboard akan terbuka secara otomatis melalui browser.

---

## 📊 Fitur Dashboard

- **Filter interaktif** berdasarkan tahun dan musim
- **Key Performance Indicator (KPI)**:
  - Total penyewaan sepeda
  - Rata-rata penyewaan harian
  - Jumlah penyewaan tertinggi
- **Visualisasi data**:
  - Bar chart jumlah penyewaan sepeda berdasarkan musim
  - Line chart tren penyewaan sepeda harian
- **Tabel data** untuk melihat data mentah

---

## 📈 Insight Utama

- Musim memiliki pengaruh yang cukup signifikan terhadap jumlah penyewaan sepeda.
- Terdapat pola fluktuasi penyewaan sepeda dari waktu ke waktu, dengan kecenderungan peningkatan pada periode tertentu.

---

## 🛠️ Teknologi yang Digunakan

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

---

## ✍️ Penulis

Proyek ini dibuat sebagai bagian dari **Proyek Analisis Data** pada program pembelajaran **Dicoding**.
