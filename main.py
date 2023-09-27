import streamlit as st
import pickle
import re
from googletrans import Translator
from textblob import TextBlob
from sklearn.preprocessing import LabelEncoder
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import translators as ts

dict_lang = {'English': 'en',
             'French': 'fr',
             'Spanish': 'es',
             'Portugeese': 'pt',
             'Italian': 'it',
             'Russian': 'ru',
             'Sweedish': 'sv',
             'Malayalam': 'ms',
             'Dutch': 'nl',
             'Arabic': 'ar',
             'Turkish': 'tr',
             'German': 'de',
             'Tamil': 'ta',
             'Danish': 'de',
             'Kannada': 'kn',
             'Greek': 'el',
             'Hindi': 'hi'}


# Function to preprocess text
def transform_text(text):
    text = text.lower()
    text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    return text


# Function to predict language
def predict(text):
    output = nb.predict(text)
    output_trans = le.inverse_transform(output)
    return output_trans[0]


# Function to translate from different languages to English
def translate(text, language):
    translator = Translator()
    translated_text = translator.translate(text, dest='en')
    return translated_text.text


# Load pre-trained models and encoders
cv = pickle.load(open('vectorizer.pkl', 'rb'))
nb = pickle.load(open('model.pkl', 'rb'))
le = pickle.load(open('label_encoding.pkl', 'rb'))

# Set page title and background
st.set_page_config(
    page_title='Language Recognition App',
    page_icon='🌍',
    layout='centered',  # Center-align content
    initial_sidebar_state='collapsed'  # Sidebar initially collapsed
)

# Main title and description
st.title('Language Recognition App')
st.markdown('Detect the language of your text message!')

# Input text area
input_sms = st.text_area('Enter the message in any language')

# Predict button
if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    X = cv.transform([transformed_sms])
    # 3. Predict
    y = predict(X)
    # 4. Display result
    st.success(f'This message is in {y}!')
    # st.success(ts.translate_text(input_sms))

# Translation section
st.header('Translation Section')

# Select target language
target_language = st.selectbox('Select target language for translation:', list(dict_lang.keys()))

# Translate button
if st.button('Translate'):
    st.success(ts.translate_text(input_sms, to_language=dict_lang[target_language]))

# Footer
st.sidebar.image('logo.png', use_column_width=True)
st.sidebar.markdown('Created by Hasna Akbar Ali')

# Optional: Add background image or color to the app
st.markdown(
    """
    <style>
    body {
        background-image: url("background_image.jpg");
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
