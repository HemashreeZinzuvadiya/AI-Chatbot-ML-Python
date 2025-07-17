# 🤖 PyBot – AI Chatbot using Python & Machine Learning

PyBot is a simple AI chatbot built with Python, using Natural Language Processing (NLP) and Machine Learning for understanding user input. It features a graphical user interface (GUI) built with Tkinter for easy interaction.

---

## 🧠 Features

- Trained using scikit-learn's Naive Bayes classifier
- Uses TF-IDF for text vectorization
- GUI interface built with Tkinter
- Handles greetings, name questions, capability queries, and more
- Randomized responses for more natural interaction

---

## 🛠️ Technologies Used

- Python
- scikit-learn (for ML)
- Tkinter (for GUI)
- TfidfVectorizer (NLP vectorization)
- Multinomial Naive Bayes (ML model)

---

## 🖥️ GUI Preview

When you run the script, it opens a desktop chat window:

You: hi
PyBot: Hello!

You: what is your name
PyBot: I'm PyBot, your ML-powered assistant.


---

## 🏗️ How It Works

1. **Training Data:** Predefined sentences labeled by intent (e.g., greeting, name, goodbye)
2. **Vectorization:** Sentences are converted to numerical vectors using TF-IDF
3. **Model:** A Naive Bayes classifier predicts the intent of user input
4. **Response:** The bot replies with a randomly selected response from the predicted intent category

---

## ▶️ How to Run

### 1. Install Required Libraries

```bash
pip install scikit-learn

Now Run the ChatBot

python ChatBot.py
