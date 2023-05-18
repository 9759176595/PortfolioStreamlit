import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Raj's Portfolio", page_icon=":tada:", layout="wide")


# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()


# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
# lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_49rdyysj.json")
# lottie_url = "https://assets10.lottiefiles.com/packages/lf20_49rdyysj.json"
# lottie_json = load_lottieurl(lottie_url)
# st_lottie(lottie_json)

img_contact_form = Image.open("images/caption5.png")
img_lottie_animation = Image.open("images/steg.png")

# ---- HEADER SECTION ----
with st.container():
    st.header("Hi, I am Raj :wave:")
    st.title("A Data Analyst From Havells")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://www.youtube.com/channel/UCtEx5WivPjemwKuqlqfoxcg)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/channel/UCtEx5WivPjemwKuqlqfoxcg)")
    # with right_column:
    #     st_lottie(lottie_coding)
        # st_lottie(lottie_coding, height=300, key="coding")
        # st.lottie(lottie_json)
        # st.image(img_lottie_animation)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Figurine CrypAnalysis")
        st.write(
            """
            Learn how to use CryptoGraphy in Data Hidig!
            Here two techniques one from Crypto and another from Bits are used to encrypt the data,
            inside the image.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/channel/UCtEx5WivPjemwKuqlqfoxcg)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Image Caption Generator")
        st.write(
            """
            Want to generate Captions from random image?
            In this project, I generate captions from image using 8kFlair dataset :nerd_face: 
            Watch it out...
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/channel/UCtEx5WivPjemwKuqlqfoxcg)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Image Caption Generator")
        st.write(
            """
            Want to generate Captions from random image?
            In this project, I generate captions from image using 8kFlair dataset :nerd_face: 
            Watch it out...
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/channel/UCtEx5WivPjemwKuqlqfoxcg)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
