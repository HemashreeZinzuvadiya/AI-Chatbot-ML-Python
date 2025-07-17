import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

# ==== Training Data ====
training_sentences = [
    "hi", "hello", "hey", "good morning", "good evening",
    "how are you", "what's up", "how do you do",
    "bye", "goodbye", "see you later", "exit",
    "what is your name", "who are you",
    "what can you do", "help me", "i need assistance"
]

training_labels = [
    "greeting", "greeting", "greeting", "greeting", "greeting",
    "ask_feeling", "ask_feeling", "ask_feeling",
    "goodbye", "goodbye", "goodbye", "goodbye",
    "name", "name",
    "capabilities", "capabilities", "capabilities"
]

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help?"],
    "ask_feeling": ["I'm just a bot, but I'm doing great!", "All systems go!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "name": ["I'm PyBot, your ML-powered assistant."],
    "capabilities": ["I can chat with you, answer simple questions, and learn new things."]
}

# ==== ML Training ====
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)
model = MultinomialNB()
model.fit(X, training_labels)

# ==== ML Chatbot Logic ====
def chatbot_response(user_input):
    X_test = vectorizer.transform([user_input])
    predicted_label = model.predict(X_test)[0]
    return random.choice(responses.get(predicted_label, ["Sorry, I didn't understand that."]))

# ==== GUI with Tkinter ====
def send_message():
    user_input = entry_field.get()
    if user_input.strip() == "":
        return
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n", 'user')
    
    bot_reply = chatbot_response(user_input)
    chat_window.insert(tk.END, "PyBot: " + bot_reply + "\n\n", 'bot')
    
    chat_window.config(state=tk.DISABLED)
    entry_field.delete(0, tk.END)
    chat_window.yview(tk.END)

# GUI Setup
root = tk.Tk()
root.title("ML Chatbot - PyBot")
root.geometry("520x500")
root.resizable(False, False)
root.configure(bg="#F5F5F5")

# Chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Segoe UI", 11), bg="white", fg="black")
chat_window.pack(padx=10, pady=10)
chat_window.insert(tk.END, "PyBot: Hello! I'm PyBot, ask me something.\n\n", 'bot')
chat_window.tag_config('user', foreground='blue')
chat_window.tag_config('bot', foreground='green')
chat_window.config(state=tk.DISABLED)

# Entry + Button
entry_field = tk.Entry(root, font=("Segoe UI", 12), width=40)
entry_field.pack(side=tk.LEFT, padx=(10, 0), pady=10)

send_button = tk.Button(root, text="Send", command=send_message, font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", padx=10, pady=2)
send_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
