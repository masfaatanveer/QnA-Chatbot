<h1 align="center">🤖 QnA-Chatbot</h1>
<h3 align="center">A Fast & Lightweight Rule-Based NLP Chatbot using TF-IDF</h3>

<p align="center">
  <strong>Get instant answers from a smart chatbot trained on 1000+ real-world questions — without any heavy LLMs!</strong><br/>
  Built using Python, TF-IDF, cosine similarity and deployed via Streamlit.
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat-square"/>
  <img src="https://img.shields.io/badge/Streamlit-Deployed-orange.svg?style=flat-square"/>
  <img src="https://img.shields.io/badge/NLP-TFIDF%20%7C%20Cosine-brightgreen.svg?style=flat-square"/>
</div>

---


## 🧠 How It Works

- Reads a **CSV of 1000+ questions and answers** across various topics
- Converts user input + stored questions into **TF-IDF vectors**
- Uses **cosine similarity** to find the best-matching response
- If no match crosses a confidence threshold, returns a fallback message
- Runs inside a clean **Streamlit UI** for fast and easy use

---

## 🗂 Example Topics in Dataset

- General Knowledge  
- Science & Technology  
- Programming  
- Health & Wellness  
- Islamic / Spiritual  
- Education  
- FAQs, Casual Chat, and more...

---

## ⚙️ Run the Chatbot Locally

1. **Clone the repo**  
```bash
git clone https://github.com/masfaatanveer/QnA-Chatbot.git
cd QnA-Chatbot
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Run the app**  
```bash
streamlit run app.py
```

4. **Chat away!**  
Ask anything similar to the dataset — the bot will respond instantly.

---

## 📁 Project Structure

```
📁 QnA-Chatbot/
├── app.py                # Streamlit UI + chatbot logic
├── chatbot.py            # Core TF-IDF + cosine chatbot class
├── data/
│   └── qna_dataset.csv   # 1000+ question-answer pairs
├── demo.mp4              # Optional demo file for reference
├── requirements.txt
└── README.md
```

---

## 🔥 Why This Project?

- ⚡ Super lightweight — no LLMs or APIs needed  
- 🚀 Fast inference with 1000+ real QnA samples  
- 🧩 Easy to customize — just replace the CSV!  
- 💬 Works offline — perfect for internal, embedded, or edge use  
- 🧠 Great for demos, AI interviews, chatbot courses, or helpdesk bots

---

## 💡 Future Ideas

- Add feedback system to improve accuracy  
- Upgrade to contextual memory (or RAG-based)  
- Export chat history / save sessions  
- Add voice (speech-to-text) support  

---

## 🙋‍♂️ Created By

**Masfa Dhillon**  
[GitHub](https://github.com/masfaatanveer) • [LinkedIn](https://linkedin.com/in/masfa-tanveer-500474235)

---

## 📄 License

MIT License — Free to use, modify, and deploy with credit.

---
