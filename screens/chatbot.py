import tkinter as tk
from tkinter import scrolledtext
import yaml

class ChatBotScreen(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Chat with MentalBot")
        self.geometry("500x600")
        self.configure(bg="#F0F0F0")

        # Load YAML responses
        with open("mental_corpus/mental_health.yml", "r") as file:
            self.responses = yaml.safe_load(file)

        self.chat_window = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=60, height=25, state="disabled")
        self.chat_window.pack(pady=20)

        self.entry = tk.Entry(self, width=40)
        self.entry.pack(side=tk.LEFT, padx=10, pady=10)

        self.send_btn = tk.Button(self, text="Send", command=self.respond)
        self.send_btn.pack(side=tk.RIGHT, padx=10, pady=10)

        self.display_message("MentalBot: Hi! I'm here for your mental wellness.")

    def display_message(self, message):
        self.chat_window.config(state="normal")
        self.chat_window.insert(tk.END, message + "\n")
        self.chat_window.config(state="disabled")
        self.chat_window.see(tk.END)

    def respond(self):
        user_input = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        if user_input == "bye":
            self.display_message("MentalBot: Goodbye! Take care.")
            self.after(1000, self.destroy)
            return

        response = self.responses.get(user_input, "MentalBot: I'm here for you. Can you tell me more?")
        self.display_message("You: " + user_input)
        self.display_message("MentalBot: " + response)
