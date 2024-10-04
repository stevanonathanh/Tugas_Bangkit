import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat dataset Aotizhongxin
@st.cache_data
def load_aotizhongxin():
    return pd.read_csv("C:/Users/hp/Downloads/BANGKIT 2024/Data Air quality/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv")

# Memuat dataset Changping
@st.cache_data
def load_changping():
    return pd.read_csv("C:/Users/hp/Downloads/BANGKIT 2024/Data Air quality/PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv")

# Judul aplikasi
st.title("Analisis Polusi Udara: Aotizhongxin & Changping")

# Memuat kedua dataset
data_aotizhongxin = load_aotizhongxin()
data_changping = load_changping()

# Menampilkan data mentah
st.subheader("Data Mentah")
if st.checkbox("Tampilkan data mentah Aotizhongxin"):
    st.write(data_aotizhongxin)

if st.checkbox("Tampilkan data mentah Changping"):
    st.write(data_changping)

# Bagian Analisis O3 untuk kedua kota
st.subheader("Analisis O3")

# Menghitung rata-rata kadar O3 per tahun untuk Aotizhongxin
o3_avg_per_year_aotizhongxin = data_aotizhongxin.groupby(['year', 'station'])['O3'].mean().reset_index()

# Membuat pivot table untuk heatmap Aotizhongxin
pivot_aotizhongxin = o3_avg_per_year_aotizhongxin.pivot(index='year', columns='station', values='O3')

# Menghitung rata-rata kadar O3 per tahun untuk Changping
o3_avg_per_year_changping = data_changping.groupby(['year', 'station'])['O3'].mean().reset_index()

# Membuat pivot table untuk heatmap Changping
pivot_changping = o3_avg_per_year_changping.pivot(index='year', columns='station', values='O3')

# Menyiapkan gambar untuk plot heatmap
fig_o3, axes_o3 = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plot heatmap untuk Aotizhongxin
sns.heatmap(pivot_aotizhongxin, ax=axes_o3[0], cmap='coolwarm', annot=True, fmt=".1f")
axes_o3[0].set_title('Rata-rata Kadar O3 per Tahun - Aotizhongxin')
axes_o3[0].set_xlabel('Stasiun')
axes_o3[0].set_ylabel('Tahun')

# Plot heatmap untuk Changping
sns.heatmap(pivot_changping, ax=axes_o3[1], cmap='coolwarm', annot=True, fmt=".1f")
axes_o3[1].set_title('Rata-rata Kadar O3 per Tahun - Changping')
axes_o3[1].set_xlabel('Stasiun')
axes_o3[1].set_ylabel('Tahun')

# Menampilkan plot O3 di Streamlit
plt.tight_layout()
st.pyplot(fig_o3)

# Kesimpulan untuk O3
st.subheader("Kesimpulan Analisis O3")
st.write("""
- Untuk kesimpulan pertanyaan pertama berdasarkan data yang tersedia dan analisis yang sudah dilakukan, kota yang memiliki tingkat polusi udara tertinggi berdasarkan rata-rata indikator O3 tiap tahunnya adalah kota Aotizhongxin. Untuk tahun yang memiliki kadar O3 paling baik yaitu untuk kota Aotizhongxin dan Changping berada di tahun 2017.
""")

# Bagian Analisis SO2 untuk kedua kota
st.subheader("Analisis SO2")

# Hitung rata-rata SO2 per tahun dan stasiun untuk Aotizhongxin
average_so2_per_year_station_aotizhongxin = data_aotizhongxin.groupby(['year', 'station'])['SO2'].mean().reset_index()

# Menambahkan kategori kualitas udara berdasarkan SO2 untuk Aotizhongxin
average_so2_per_year_station_aotizhongxin['Kualitas_Udara'] = average_so2_per_year_station_aotizhongxin['SO2'].apply(
    lambda x: 'Baik' if x <= 20 else 'Sedang' if x <= 40 else 'Tidak Baik')

# Hitung rata-rata SO2 per tahun dan stasiun untuk Changping
average_so2_per_year_station_changping = data_changping.groupby(['year', 'station'])['SO2'].mean().reset_index()

# Menambahkan kategori kualitas udara berdasarkan SO2 untuk Changping
average_so2_per_year_station_changping['Kualitas_Udara'] = average_so2_per_year_station_changping['SO2'].apply(
    lambda x: 'Baik' if x <= 20 else 'Sedang' if x <= 40 else 'Tidak Baik')

# Menyiapkan gambar untuk plot SO2
fig_so2, axes_so2 = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Warna untuk setiap kategori
color_mapping = {
    'Baik': 'green',
    'Sedang': 'yellow',
    'Tidak Baik': 'red'
}

# Plot SO2 untuk Aotizhongxin
sns.barplot(data=average_so2_per_year_station_aotizhongxin, x='year', y='SO2', hue='Kualitas_Udara', palette=color_mapping, ax=axes_so2[0])
axes_so2[0].set_title('Rata-rata SO2 per Tahun - Aotizhongxin')
axes_so2[0].set_xlabel('Tahun')
axes_so2[0].set_ylabel('Rata-rata SO2')
axes_so2[0].legend(title='Kualitas Udara')

# Plot SO2 untuk Changping
sns.barplot(data=average_so2_per_year_station_changping, x='year', y='SO2', hue='Kualitas_Udara', palette=color_mapping, ax=axes_so2[1])
axes_so2[1].set_title('Rata-rata SO2 per Tahun - Changping')
axes_so2[1].set_xlabel('Tahun')
axes_so2[1].set_ylabel('Rata-rata SO2')
axes_so2[1].legend(title='Kualitas Udara')

# Menampilkan plot SO2 di Streamlit
plt.tight_layout()
st.pyplot(fig_so2)

# Kesimpulan untuk SO2
st.subheader("Kesimpulan Analisis SO2")
st.write("""
- Untuk kesimpulan kedua, rata-rata kadar SO2 di setiap kota merupakan bukan yang kadar rata-rata terbaik. Rata-rata terbaik untuk kota Aotizhongxin dan Changping berada di tahun 2016
""")
