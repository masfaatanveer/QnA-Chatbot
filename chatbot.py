import nltk
import streamlit as st
from streamlit_chat import message
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = pd.read_csv('chatbot_dataset.csv')

corpus_pairs = list(zip(data['pattern'].str.lower(), data['response']))


nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

user_inputs = [pair[0] for pair in corpus_pairs]
responses = [pair[1] for pair in corpus_pairs]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(user_inputs)

def chatbot_response(user_input):
    user_input_processed = user_input.lower()
    user_vector = vectorizer.transform([user_input_processed])
    similarity_scores = cosine_similarity(user_vector, vectors)
    most_similar_index = similarity_scores.argmax()
    max_similarity = similarity_scores[0, most_similar_index]
    threshold = 0.3

    if max_similarity < threshold:
        return "I'm sorry, I don't understand. Can you please rephrase?"
    else:
        return responses[most_similar_index]

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
        }
        .block-container {
            padding: 2rem;
        }
        .stTextInput>div>div>input {
            background-color: #161b22;
            color: white;
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 12px;
        }
        .stButton>button {
            background-color: #238636;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #2ea043;
        }
        .header {
            color: #58a6ff;
            font-size: 32px;
            margin-bottom: 1rem;
            text-align: center;
        }
        .sidebar .sidebar-content {
            background-color: #161b22;
            padding: 1rem;
            border-radius: 10px;
        }
        .sidebar-header {
            font-size: 22px;
            color: #58a6ff;
            margin-bottom: 1rem;
        }
        .sidebar-text {
            font-size: 16px;
            color: #c9d1d9;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state['history'] = []

with st.sidebar:
    st.markdown("<div class='sidebar-header'>🤖 Main Doremon ka door ka rishtedaar hoon, par meri jeb khali hai!</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<div class='sidebar-text'>📌 Sample Questions:</div>", unsafe_allow_html=True)
    for q in user_inputs[:6]:
        st.markdown(f"<div class='sidebar-text'>- {q.capitalize()}</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<div class='sidebar-text'>Created with ❤️ by someone who believes in making tech a little more human</div>", unsafe_allow_html=True)

st.markdown("<h1 class='header'>Sawal kro </h1>", unsafe_allow_html=True)

for i, (sender, message_text) in enumerate(st.session_state['history']):
    if sender == "user":
        message(message_text, is_user=True, key=f"user_{i}")
    else:
        message(message_text, key=f"bot_{i}")

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state['history'].append(("user", user_input))
    bot_response = chatbot_response(user_input)
    st.session_state['history'].append(("bot", bot_response))
    st.rerun()
