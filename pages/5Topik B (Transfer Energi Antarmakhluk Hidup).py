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

# Pilihan Ganda
st.title("TOPIK B (TRANSFER ENERGI ANTARMAKHLUK HIDUP)")

tab1, tab2 = st.tabs(["Transfer Energi Antarmakhluk Hidup", "KUIS TOPIK B"])

with tab1:
    st.header("Transfer Energi Antarmakhluk Hidup")
    st.write("---")
    st.image("https://64.media.tumblr.com/851a17f747284052116b81ce81fad611/7b5d04a0a9f9cd60-bf/s540x810/65a7beb65c88cb0ff3a0ec382d857d91fae4cda1.pnj")
    st.subheader("Bagaimana transfer energi yang terjadi pada suatu ekosistem?")
    st.write("Rantai makanan menggambarkan jalur alur energi yang ada pada suatu ekosistem.")
    st.write("Para saintis memperkirakan energi yang digunakan oleh makhluk hidup sebesar 90%. Artinya, hanya ada 10% sisa energi yang bisa dikonsumsi oleh makhluk hidup lain melalui transfer energi.")
    st.write("Transfer energi dapat digambarkan dalam bentuk piramida makanan.")
    with st.expander("Piramida Makanan"):
        st.subheader("Piramida Makanan")
        st.image('https://64.media.tumblr.com/2d7e51b1b18cd72168ddf925d49c75b5/47777aaa2a98d776-45/s540x810/81877e03756f0fca2dcdef183f10de36cebd1392.pnj', 'Gambar piramida makanan')
        st.write("Pada piramida makanan, semakin rendah tingkatannya akan semakin banyak jumlah tumbuhan atau hewan yang termasuk di dalamnya. Sebaliknya, semakin tinggi tingkatannya, maka semakin besar ukuran dan semakin sedikit jumlah hewan yang termasuk di dalamnya.")
        st.write("Dekomposer tidak digambarkan dalam piramida ini karena dekomposer dapat berada dalam setiap tingkatan selama ada senyawa organik yang bisa diuraikan.")
        st.write("---")
        st.write("Untuk lebih memahami materi mengenai transfer energi, Mari baca lebih lanjut [Bahan Ajar Selengkapnya](https://docs.google.com/document/d/1ZGMHIbYWM9dl4WJClQp8-9xraw79_-XFNbxDEUF_neI/edit?usp=sharing) dan simak video pembelajaran berikut.")
        st.video("https://youtube.com/watch?v=CGVcKH2LZCM&feature=share")
        st.write("---")
        st.write("Nah, setelah membaca bahan ajar dan mengamati video pembelajaran tersebut, berarti kamu telah memahami tentang transfer energi. Sekarang cobalah lakukan percobaan transfer energi berikut!")
        submit = st.button("Percobaan tentang Transfer Energi   \u2193")
        if submit:
            st.write("Lakukan percobaan proses transfer energi pada jaring-jaring makanan berikut secara berkelompok.")
            st.image("https://64.media.tumblr.com/f3876bbefe4c27292ef8e65222a6ac1e/eb4629e1d6c5670a-4e/s2048x3072/8eee55d28a4447d01db533159197854c8ad09805.pnj")
            st.write("---")
            st.write("Untuk memahami langkah-langkah percobaan, simak video berikut!")
            st.video("https://youtu.be/Exa2ns600WY")
        st.write("---")
        st.write("---")
        st.write("Untuk mengukur pemahaman kamu mengenai transfer energi, mari kerjakan kuis dengan menekan tombol KUIS TOPIK B pada bagian atas   ⬆⬆⬆")


#Kuis
with tab2:
    def generate_questions():
        questions = [
            {
                'type': 'text',
                'question': 'Makhluk hidup mendapatkan energi dari makanan. Sebagian besar energi ini digunakan untuk ....',
                'options': ['A. tumbuh dan berkembang', 'B. tidur', 'C. disimpan', 'D. diberikan kepada hewan lain'],
                'answer': 'A. tumbuh dan berkembang'
            },
            {
                'type': 'image',
                'question': 'Populasi hewan yang paling banyak pada piramida di bawah ini adalah .... ',
                'image': 'https://64.media.tumblr.com/83efc7a5eca18eeb79e4e45566e4d5ea/68f9654dea135d25-38/s500x750/d0fddb8793419b7b0026a2713bb9412f5ecb7b38.pnj',
                'options': ['A. Burung Elang', 'B. Katak', 'C. Belalang', 'D. Ayam'],
                'answer': 'C. Belalang'
            },
            {
                'type': 'image',
                'question': 'Perhatikan makhluk hidup berikut!',
                'image' : 'https://64.media.tumblr.com/42a26aa5fddf1a79059c7db828d8470e/3daaf54603379a66-54/s500x750/26f1e6a426fdd95d4d40e0545a774f5c4b951455.pnj',
                'options': ['A. 1 dan 2', 'B. 2 dan 3', 'C. 2 dan 4', 'D. 3 dan 4'],
                'answer': 'B. 2 dan 3'
            },
            {
                'type': 'text',
                'question': 'Makhluk hidup yang memperoleh energi dari cahaya matahari dalam jaring-jaring makanan adalah ....',
                'options': ['A. Konsumen tingkat 1', 'B. Konsumen tingkat 2', 'C. Pengurai', 'D. Produsen'],
                'answer': 'D. Produsen'
            },
            {
                'type': 'image',
                'question': 'Pernyataan berikut yang benar terkait transfer energi dalam jaring-jaring makanan dari tabel di bawah adalah ....',
                'image': 'https://64.media.tumblr.com/ac239a0f67b65453b8e62fcf48e58434/312e0b632254481e-24/s540x810/871eb1de41a021296b272ec79a425d5c5844549f.pnj',
                'options': ['A. 1, 4, dan 5', 'B. 1, 2, dan 4', 'C. 1, 3, dan 5', 'D. 2, 3, dan 5'],
                'answer': 'A. 1, 4, dan 5'
            },
            {
                'type': 'text',
                'question': 'Komponen rantai makanan berikut yang tidak terdapat pada piramida makanan yaitu ....',
                'options': ['A. Produsen', 'B. Dekomposer', 'C. Konsumen tingkat 1', 'D. Konsumen tingkat 2'],
                'answer': 'B. Dekomposer'
            },
            {
                'type': 'image',
                'question': 'Pernyataan berikut yang tepat sesuai dengan piramida makanan berikut adalah ....',
                'image': 'https://64.media.tumblr.com/a44fd092a801b2916db2eb395d8cb9fa/b1a1cb7bb0b0645b-c2/s640x960/fac055b96078eed44a98411b9428841ab4d30890.pnj',
                'options': ['A. Energi pada kelinci lebih sedikit dari ular', 'B. Energi pada ular lebih banyak dari kelinci', 'C. Energi pada elang lebih sedikit dari ular', 'D. Energi pada elang lebih banyak dari tanaman'],
                'answer': 'C. Energi pada elang lebih sedikit dari ular'
            },
            {
                'type': 'text',
                'question': 'Mempelajari ekosistem mengajarkan pada kita bahwa manusia hidup berdampingan dengan makhluk hidup lainnya. Oleh karena itu, kita harus turut serta dalam menjaga keseimbangan ekosistem. Berikut ini yang bukan merupakan upaya dalam menjaga keseimbangan ekosistem disekitar kita adalah ....',
                'options': ['A. Membuang sampah tidak pada tempatnya', 'B. Menanam kembali tanaman sehingga dapat menjaga keberadaan produsen', 'C. Memanfaatkan dekomposer untuk membuat tanah menjadi subur', 'D. Tidak membunuh atau menangkap hewan sembarangan'],
                'answer': 'A. Membuang sampah tidak pada tempatnya'
            },
            {
                'type': 'image',
                'question': 'Siswa kelas 5 melakukan percobaan transfer energi pada jaring-jaring makanan. Berdasarkan gambar di bawah ini, banyaknya batu pada toples yang berlabelkan konsumen 1 sebanyak ....',
                'image': 'https://64.media.tumblr.com/33efbb71477024b52e30477f4020bcd6/cf327b34883a9013-c1/s1280x1920/e09968e72c3ea5e0ef1821144eb1f35aa9a9c8f4.pnj',
                'options': ['A. 15', 'B. 12', 'C. 10', 'D. 9'],
                'answer': 'C. 10'
            },
            {
                'type': 'text',
                'question': 'Pada jaring-jaring makanan, transfer energi semakin sedikit karena ....',
                'options': ['A. makhluk hidup semakin banyak', 'B. digunakan oleh makhluk hidup', 'C. tersimpan terlalu lama', 'D. kurangnya cahaya matahari'],
                'answer': 'B. digunakan oleh makhluk hidup'
            },
        ]
        return questions

    def display_question(question):
        if question['type'] == 'text':
            st.write('**Pertanyaan:**', question['question'])
            selected_option = st.radio('Pilih jawaban Anda:', question['options'])
        elif question['type'] == 'image':
            st.write('**Pertanyaan:**', question['question'])
            st.image(question['image'], use_column_width=True)
            selected_option = st.radio('Pilih jawaban Anda:', question['options'])
        else:
            pass
        return selected_option

    def main():
        st.title('Kuis Topik B- Transfer Energi Antarmakhluk Hidup')
        st.write('Jawablah pertanyaan berikut dengan menekan bulatan pada opsi jawaban yg menurut kamu benar!')
        questions = generate_questions()
        num_questions = len(questions)
        current_question = 0
        score = 0

        if 'current_question' in st.session_state:
            current_question = st.session_state.current_question
        if 'score' in st.session_state:
            score = st.session_state.score

        if current_question < num_questions:
            selected_option = display_question(questions[current_question])
            st.write('---')
            if st.button('Next', key='next_button', help='Jawaban Anda akan dikunci saat tombol Next ditekan'):
                if selected_option == questions[current_question]['answer']:
                    score += 1
                current_question += 1
        else:
            st.write('Anda telah menjawab semua pertanyaan.')
            st.write('Skor akhir Anda:', score, '/', num_questions)

        st.session_state.current_question = current_question
        st.session_state.score = score

    if __name__ == '__main__':
        main()


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
st.write("---")
st.write("---")

from streamlit_extras.switch_page_button import switch_page

col1, col2= st.columns(2)
with col1:
   want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")
 
with col2:
   want_to_pemb = st.button("Next   \u25B6   Profil")
if want_to_pemb:
   switch_page("Profil")
