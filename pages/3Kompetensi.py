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
st.subheader("Kompetensi yang akan di capai pada pembelajaran kali ini meliputi: Capaian Pembelajaran (CP), Tujuan Pembelajaran, dan Alur Tujuan Pembelajaran (ATP) pada materi Ekosistem")
st.write("##")

# Menambahkan CSS untuk mengatur warna latar belakang tab menjadi biru
st.markdown(
    """
    <style>
   .streamlit-tabs.stHorizontal > .tabs {
        background-color: blue;
    }
    .streamlit-tabs.stHorizontal > .tabs .tab[data-baseweb="tab"] {
        background-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Capaian Pembelajaran (CP)", "Tujuan Pembelajaran", " ALur Tujuan Pembelajaran (ATP)"])

with tab1:
   st.header("Capaian Pembelajaran (CP)")
   st.image("https://64.media.tumblr.com/d8c9eb60b10304f20253cc1c01146553/fc311c9e2e3f5970-d4/s640x960/de6f50e9345e64c57f20d1ff09bbef085e05c6ce.pnj")
   st.image("https://64.media.tumblr.com/0e7f02c2b423e81c9fd30bf10c10c5db/36ed59391e9ac7b6-2d/s1280x1920/f0c34240ccd2a6a3af36053672e9475d98ca4c0b.pnj")
with tab2:
   st.header("Tujuan Pembelajaran")
   st.image("https://64.media.tumblr.com/115ab57952922a97ba2aa1afa428ffaa/b53d2005dfafa745-ee/s640x960/c18c4a265d9c9228e8f7e036db46312bd338d40f.pnj")

with tab3:
   st.header("Alur Tujuan Pembelajaran(ATP)")
   st.image("https://64.media.tumblr.com/5488c65036cd6f724b9c1612d29a3012/651b9c5590e2e8d0-bd/s640x960/0efe086b7db9223a527cba61ab7b252b73a28434.pnj")

st.write("---")


# Tulis
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

from streamlit_extras.switch_page_button import switch_page

col1, col2= st.columns(2)
with col1:
   want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")
 
with col2:
   want_to_pemb = st.button("Next   \u25B6   Topik A (Memakan dan Dimakan)")
if want_to_pemb:
   switch_page("Topik A (Memakan dan Dimakan)")
