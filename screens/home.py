import tkinter as tk
from screens.chatbot import ChatbotScreen
from screens.mood_tracker import MoodTrackerScreen
from screens.breathing import BreathingExercisesScreen  

from screens.app_launcher import show_login_signup_screen  # ✅ fixed import

class HomeScreen(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.title("Mental Wellness Chatbot - Home")
        self.geometry("400x400")
        self.configure(bg="#e6f9f5")

        tk.Label(self, text=f"Welcome, {self.username}!", font=("Arial", 14), bg="#e6f9f5").pack(pady=10)

        tk.Button(self, text="Chat with Bot", width=25, command=self.open_chatbot).pack(pady=10)
        tk.Button(self, text="Mood Tracker", width=25, command=self.open_mood_tracker).pack(pady=10)
        tk.Button(self, text="Breathing Exercises", width=25, command=self.open_breathing).pack(pady=10)
        tk.Button(self, text="Profile / Logout", width=25, command=self.logout_user).pack(pady=10)

    def open_chatbot(self):
        self.destroy()
        ChatbotScreen(self.username)

    def open_mood_tracker(self):
        self.destroy()
        MoodTrackerScreen(self.username)

    def open_breathing(self):
        self.destroy()
        BreathingExercisesScreen(self.username).mainloop()


    def logout_user(self):  # ✅ Log out and return to login screen
        self.destroy()
        show_login_signup_screen()
