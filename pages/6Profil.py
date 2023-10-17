import streamlit as st

# Menghilangkan tombol Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Mengganti Background dengan gambar
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://64.media.tumblr.com/f1b799a9001ef3c5039b8c2df732302a/bee820355e1c5385-b5/s500x750/087d44811a92dbcaaead66ac876d8a0e9258e9d5.pnj");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba{0, 0, 0, 0};
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url("https://64.media.tumblr.com/c63175929c962183549281fdb1d3d691/853fbeae28c192bb-2f/s1280x1920/633e7b556e7bd06a088997c8540b62f16db7ea33.pnj");
background-size: cover;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Mulai Title
def main():
    st.title("Profil Pengembang Ecobot")
    st.write("---")

    col1, col2 = st.columns(2)  # Membagi layar menjadi dua kolom

    # Isi kolom pertama
    with col1:
        st.header("Pengembang")
        st.image("https://64.media.tumblr.com/71cc949c33c2a11f8ebfeec4da8ed25f/8668cd133f446a1c-7e/s1280x1920/26ebef31acf2b00120788f09d4f749628dd4d867.pnj", width=200)
        st.write("---")
        st.write("Nama: Wahyuni")
        st.write("Alamat: Cilacap, Jawa Tengah, Indonesia")
        st.write("Instansi: Universitas Negeri Semarang")
        st.write("Fakultas: Ilmu Pendidikan dan Psikologi")
        st.write("Jurusan: Pendidikan Guru Sekolah Dasar")

    # Isi kolom kedua
    with col2:
        st.header("Dosen Pembimbing")
        st.image("https://simpeg.unnes.ac.id/index.php/simpeg_portofolio/load_photo/198312172009122003")
        st.write("---")
        st.write("Nama: Ibu Desi Wulandari, S.Pd., M.Pd.")
        st.write("NIP: 198312172009122003")
        st.write("Jabatan: Lektor Universitas Negeri Semarang")

if __name__ == "__main__":
    main()


st.write("---")
st.write("---")
st.write("Untuk saran dan masukan hub: 085758447988")


#Ganti Page Berdampingan
st.markdown(
    """
    <style>
    .stButton button {
        font-size: 18px;
        background-color: #ff8c00; /* Ubah dengan kode warna coklat pastel yang diinginkan */
        color: white;
        width:100%
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("---")

from streamlit_extras.switch_page_button import switch_page

want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")



