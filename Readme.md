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

## 📽 Demo

> 🎥 A quick preview of QnA-Chatbot in action

https://github.com/masfaatanveer/QnA-Chatbot/blob/363e1f8955b2ab1d2bf7c413bcf87f5a3a587718/demo.mp4



```

---

## 🧠 How It Works

- This chatbot reads a **CSV of 1000+ questions and answers** across various topics
- Converts user input + stored questions into **TF-IDF vectors**
- Uses **cosine similarity** to find the best-matching response
- If no match crosses a confidence threshold, it returns a fallback message
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

3. **Run Streamlit app**  
```bash
streamlit run app.py
```

4. **Chat away!**  
Ask anything similar to the dataset — and the bot will respond instantly.

---

## 📁 File Structure

```
📁 QnA-Chatbot/
├── app.py                # Streamlit UI + chatbot logic
├── chatbot.py            # Core TF-IDF + cosine chatbot class
├── data/
│   └── qna_dataset.csv   # 1000+ question-answer pairs
├── demo.mp4              
├── requirements.txt
└── README.md
```

---

## 🔥 Why This Project?

- ⚡ Super lightweight — no LLM needed  
- 🚀 Fast inference with 1000+ real QnA samples  
- 🧩 Easy to customize: just replace the CSV!  
- 💬 Works offline, ideal for embedded or enterprise setups  
- 🧠 Ideal for demos, helpdesk bots, AI interviews, or chatbot learning

---

## 💡 Future Ideas

- Add feedback system to improve answers  
- Upgrade to contextual memory or RAG  
- Export chat history  
- Add speech-to-text input  

---

## 🙋‍♂️ Created By

**Masfa Dhillon**  
[GitHub](https://github.com/masfaatanveer) • [LinkedIn](https://linkedin.com/in/masfa-tanveer-500474235)

---

## 📄 License

MIT License — free to use, modify, and deploy with credit.

---
