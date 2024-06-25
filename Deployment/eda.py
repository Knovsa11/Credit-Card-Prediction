import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    # Bikin judul title page
    page_title= 'Credit Card Default'
)
def run():
        # Membuat Judul
    st.title('Default Payment Next Month Prediction')

    # Membuat subheader
    st.subheader('EDA default_payment_next_month')

    # Tambahkan gambar
    image = Image.open('credit_card.jpg')
    st.image(image, caption='Credit Card Default Payment')

    # Bikin dekripsi
    st.write('**Made by Kelvin**')

    st.markdown('---')

    # show dataframe
    df_eda = pd.read_csv("P1G5_Set_1_kelvin_rizky.csv")

    st.dataframe(df_eda)

    # Membuat grafik jumlah default
    st.write('#### Jumlah Default dalam Dataset')
    fig = plt.figure()
    plt.pie(df_eda['default_payment_next_month'].value_counts(), explode=[0.1, 0], autopct="%1.1f%%")
    plt.title('Jumlah Default')
    # Tampilkan plot di Streamlit
    st.pyplot(fig)


    # Membuat Plot status pendidikan pada setiap default payment berdasarkan umur
    st.write('#### Plot status pendidikan pada setiap default payment berdasarkan umur')
    # Membuat mapping dari nilai lama ke nilai baru
    status_pendidikan = {1: 'Pasca Sarjana', 2: 'Universitas', 3: 'SMA'}
    # Menggunakan map untuk mengubah label pada kolom 'education_level'
    df_eda['education_level'] = df_eda['education_level'].map(status_pendidikan)
    # Membuat histogram pada default_payment_next_month
    fig = sns.set(rc={'figure.figsize': (10, 8)})
    fig = sns.FacetGrid(df_eda, row='default_payment_next_month', col='education_level')
    fig.set_titles(col_template="{col_name}", row_template="{row_name}")
    fig = fig.map(plt.hist, 'age')
    # Tampilkan plot di Streamlit
    st.pyplot(fig.figure)


    # Membuat Plot Gender pada setiap default payment berdasarkan umur
    st.write('#### Plot Gender pada setiap default payment berdasarkan umur')
    # Membuat mapping dari nilai lama ke nilai baru
    jenis_kelamin = {1: 'male', 2: 'female'}
    # Menggunakan map untuk mengubah label pada kolom 'sex'
    df_eda['sex'] = df_eda['sex'].map(jenis_kelamin)
    # Membuat histogram pada default_payment_next_month
    fiq = sns.set(rc={'figure.figsize':(10,8)})
    fiq = sns.FacetGrid(df_eda, row='default_payment_next_month', col='sex')
    fiq = fiq.set_titles(col_template="{col_name}", row_template="{row_name}")
    fiq = fiq.map(plt.hist, 'age')
    # Tampilkan plot di Streamlit
    st.pyplot(fig.figure)


    # Membuat Plot status pernikahan pada setiap default payment berdasarkan umur
    st.write('#### Plot status pernikahan pada setiap default payment berdasarkan umur')
    # Membuat mapping dari nilai lama ke nilai baru
    status_pernikahan = {1: 'menikah', 2: 'single', 3:'lainnya'}
    # Menggunakan map untuk mengubah label pada kolom 'marital_status'
    df_eda['marital_status'] = df_eda['marital_status'].map(status_pernikahan)
    # Membuat histogram pada default_payment_next_month
    fig = sns.set(rc={'figure.figsize':(10,8)})
    fig = sns.FacetGrid(df_eda, row='default_payment_next_month', col='marital_status')
    fig = fig.set_titles(col_template="{col_name}", row_template="{row_name}")
    fig = fig.map(plt.hist, 'age')
    # Tampilkan plot di Streamlit
    st.pyplot(fig.figure)


    # Membuat grafik status pernikahan dan status pendidikan berdasarkan default_payment_next_month
    st.write('#### Grafik status pernikahan dan status pendidikan berdasarkan default_payment_next_month')
    fig = plt.figure(figsize=(12,4))
    fig = ax = sns.barplot(x = "marital_status", y = "default_payment_next_month", hue = "education_level", data = df_eda, palette = 'rocket', errorbar = None)
    fig =plt.ylabel("% of Default", fontsize= 12)
    fig = plt.ylim(0,0.5)
    fig =plt.xticks([0,1,2],['Married', 'Single','Others'], fontsize = 12)
    fig = plt.legend(['Pasca Sarjana', 'Universitas', 'SMA'], title = 'Status Pendidikan', fontsize = 8)

    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.06, p.get_height()+0.03),fontsize=12)

    # Tampilkan plot di Streamlit
    st.pyplot(fig.figure)


    # Membuat Grafik gender dan status pendidikan berdasarkan default_payment_next_month
    st.write('#### Grafik gender dan status pendidikan berdasarkan default_payment_next_month')
    fig = plt.figure(figsize=(12,4))
    fig = ax = sns.barplot(x = "sex", y = "default_payment_next_month", hue = "education_level", data = df_eda, palette = 'rocket', errorbar = None)
    fig = plt.ylabel("% of Default", fontsize= 12)
    fig = plt.ylim(0,0.5)
    fig = plt.xticks([0,1],['Male', 'Female'], fontsize = 12)
    fig = plt.legend(['Pasca Sarjana', 'Universitas', 'SMA'], title = 'Status Pendidikan', fontsize = 8)

    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.06, p.get_height()+0.03),fontsize=12)

    # Tampilkan plot di Streamlit
    st.pyplot(fig.figure)


if __name__ == '__main__':
    run()
