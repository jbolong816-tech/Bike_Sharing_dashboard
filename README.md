# 🚲 Bike Sharing Dashboard

Proyek ini bertujuan untuk menganalisis **Bike Sharing Dataset** dan menyajikan hasil analisis dalam bentuk **dashboard interaktif** menggunakan **Streamlit**. Dashboard membantu pengguna memahami pola penyewaan sepeda berdasarkan waktu, musim, dan tahun.

---

## 📌 Tujuan Proyek

1. Melakukan proses analisis data secara menyeluruh (data gathering, cleaning, exploratory data analysis).
2. Menjawab pertanyaan bisnis terkait pola penyewaan sepeda.
3. Menyajikan insight dalam bentuk visualisasi interaktif melalui dashboard.

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

Pastikan file `main_data.csv` berada dalam satu folder dengan `dashboard.py`, lalu jalankan perintah berikut:

```bash
streamlit run dashboard.py
```

Dashboard akan terbuka secara otomatis di browser.

---

## 📊 Fitur Dashboard

- **Filter interaktif** berdasarkan tahun dan musim
- **Key Performance Indicator (KPI)**:
  - Total penyewaan sepeda
  - Rata-rata penyewaan harian
  - Jumlah penyewaan tertinggi
- **Visualisasi data**:
  - Bar chart jumlah penyewaan per musim
  - Line chart tren penyewaan harian
- **Tabel data mentah** yang dapat dilihat langsung

---

## 📈 Insight Utama

- Musim tertentu memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda.
- Terlihat pola fluktuasi penyewaan sepeda dari waktu ke waktu, dengan puncak pada hari-hari tertentu.

---

## 🛠️ Teknologi yang Digunakan

- Python
- Pandas
- Matplotlib & Seaborn
- Streamlit

---

## ✍️ Penulis

Proyek ini dibuat sebagai bagian dari **Proyek Analisis Data**.

