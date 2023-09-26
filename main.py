# import streamlit as st
# import pickle
# import re
# import nltk
# from sklearn.preprocessing import LabelEncoder
# from nltk.corpus import stopwords
# # from nltk.stem.porter import PorterStemmer
# from PIL import Image
# from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
#
# import string
#
# def transform_text(text):
#     text = text.lower()
#     text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
#     text = re.sub(r'[[]]', ' ', text)
#     # appending to data_list
#     return text
#
# def predict(text):
#     output = nb.predict(text)
#     output_trans = le.inverse_transform(output)
#     return output_trans[0]
#
# cv = pickle.load(open('vectorizer.pkl', 'rb'))
# nb = pickle.load(open('model.pkl', 'rb'))
# le = pickle.load(open('label_encoding.pkl', 'rb'))
#
# st.title('Language Recognition')
#
# input_sms = st.text_area('Enter the message in any language')
#
# if st.button('Predict'):
#     # 1. Preprocess
#     transformed_sms = transform_text(input_sms)
#     # 2. Vectorize
#     X = cv.transform([transformed_sms])
#     # 3. Predict
#     y = predict(X)
#     # 4. Display
#     # col1 = st.columns(1)
#     # if y == 0:
#     st.button(y)
#         # not_spam = Image.open('not_spam.png')
#         # st.image(not_spam, caption='Not Spam!')
#         # with col1:
#         #     st.write('Not Spam!')
#         #     st.image('not_spam.png')
#     # else:
#     #     st.button('Spam!')
#         # spam = Image.open('spam.png')
#         # st.image(spam, caption='Spam!')
#         # with col1:
#         #     st.write('Spam!')
#         #     st.image('spam.png')
#

import streamlit as st
import pickle
import re
from sklearn.preprocessing import LabelEncoder
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

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
