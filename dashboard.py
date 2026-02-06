import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================
# Load Data
# =====================
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# =====================
# Filter Jan - Jun 2011
# =====================
df_2011 = df[
    (df['dteday'].dt.year == 2011) &
    (df['dteday'].dt.month <= 6)
]

# =====================
# Mapping Cuaca
# =====================
weather_map = {
    1: "Cerah",
    2: "Berkabut",
    3: "Hujan Ringan",
    4: "Hujan Lebat"
}

df_2011['weathersit'] = df_2011['weathersit'].map(weather_map)

# =====================
# Sidebar
# =====================
st.sidebar.title("🚲 Bike Sharing Dashboard")
st.sidebar.markdown("**Periode:** Jan - Jun 2011")

# =====================
# Title
# =====================
st.title("📊 Analisis Penyewaan Sepeda")
st.markdown("Periode **Januari – Juni 2011**")

# =====================
# Pertanyaan 1
# =====================
st.subheader("❓ Pertanyaan 1")
st.write("**Berapa rata-rata jumlah penyewaan sepeda Jan–Jun 2011?**")

avg_rent = df_2011['cnt'].mean()
st.metric(label="Rata-rata Penyewaan Sepeda", value=f"{avg_rent:,.0f} sepeda/hari")

# =====================
# Pertanyaan 2
# =====================
st.subheader("❓ Pertanyaan 2")
st.write("**Bagaimana pengaruh kondisi cuaca terhadap penyewaan sepeda harian?**")

weather_avg = df_2011.groupby('weathersit')['cnt'].mean().sort_values()

# Plot
fig, ax = plt.subplots()
weather_avg.plot(kind='bar', ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda")

st.pyplot(fig)

# =====================
# Insight
# =====================
st.subheader("📌 Insight")
st.markdown("""
- Penyewaan sepeda **tertinggi terjadi saat cuaca cerah**
- Semakin buruk kondisi cuaca, **jumlah penyewaan cenderung menurun**
- Cuaca menjadi faktor penting dalam permintaan layanan bike sharing
""")
