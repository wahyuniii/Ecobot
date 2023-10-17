import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.stateful_button import button


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
st.title("HALO DENGAN ECOBOT DISINI :wave:")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_gaj4x0te.json"
lottie_html = f'<div class="lottie" style="background-color: #FF000;"><lottie-player src="{lottie_url_hello}" background="transparent" speed="1" loop autoplay></lottie-player></div>'
st.markdown(lottie_html, unsafe_allow_html=True)
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")

# Menambahkan CSS untuk mengatur teks menjadi rata tengah, besar, dan latar belakang teks
import streamlit as st


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.markdown(
    """
    <style>
    .my-text {
        font-size: 16px;
    }
    .stTextInput input {
        background-color: #FFAE69;
    }
    .stTextInput label {
        font-size: 20px;
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="my-text">Untuk mulai belajar, tuliskan Namamu pada kolom dibawah ini kemudian tekan Submit  \u2193  \u2193  \u2193</p>', unsafe_allow_html=True)

my_input = st.text_input(st.session_state["my_input"])

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.markdown(f"Selamat datang **{my_input}**, Ecobot siap menemani belajarmu")
    st.write("Sebelum memulai belajar, bacalah petunjuk penggunaan Ecobot terlebih dahulu ya")
    st.image("https://64.media.tumblr.com/416da6f8b6af49d2d8475a4cc0b5a8bf/bd031b2ae1c4f058-7c/s400x600/e14ed91d552cc6096021fa5d8b1df44419919feb.pnj")

# Tulis