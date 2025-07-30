import tkinter as tk
from tkinter import scrolledtext, Entry, Button
from chatterbot import ChatBot  # type: ignore
from chatterbot.trainers import ChatterBotCorpusTrainer  # type: ignore
import os

# Setup chatbot
chatbot = ChatBot(
    "MentalBot",
    read_only=False,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm here to listen. Can you share more?",
            "maximum_similarity_threshold": 0.90  # ⬅️ better matching
        }
    ],
    database_uri="sqlite:///db.sqlite3"
)

# Training setup
trainer = ChatterBotCorpusTrainer(chatbot)

# Absolute path to custom YAML file
custom_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../mental_corpus"))
custom_file = os.path.join(custom_dir, "mental_health.yml")

if os.path.exists(custom_file):
    try:
        # Train using corpus module path if __init__.py exists
        trainer.train("mental_corpus.mental_health")
        print("✅ Successfully trained on custom mental health corpus.")
    except Exception as e:
        print(f"⚠️ Custom corpus training failed: {e}")
        print("👉 Falling back to default English corpus.")
        trainer.train("chatterbot.corpus.english")
else:
    print("⚠️ Custom corpus file not found at", custom_file)
    print("👉 Training on default English corpus instead.")
    trainer.train("chatterbot.corpus.english")


# GUI setup
class ChatbotScreen(tk.Toplevel):
    def __init__(self, username):
        super().__init__()
        self.title(f"Chat with MentalBot - {username}")
        self.geometry("500x500")
        self.configure(bg="#f0f8ff")

        self.chat_area = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            width=60,
            height=20,
            state="disabled"
        )
        self.chat_area.pack(pady=10)

        self.entry = Entry(self, width=50)
        self.entry.pack(pady=(0, 10))
        self.entry.bind("<Return>", self.get_response)

        send_btn = Button(self, text="Send", command=self.get_response)
        send_btn.pack()

    def get_response(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.chat_area.configure(state="normal")
        self.chat_area.insert(tk.END, f"You: {user_input}\n")

        try:
            reply = chatbot.get_response(user_input)
            self.chat_area.insert(tk.END, f"MentalBot: {reply.text}\n\n")  # ✅ safer than str(reply)
        except Exception as e:
            self.chat_area.insert(tk.END, "MentalBot: Sorry, I encountered an error.\n\n")
            print(f"❌ Error getting response: {e}")

        self.chat_area.configure(state="disabled")
        self.chat_area.see(tk.END)
        self.entry.delete(0, tk.END)
 