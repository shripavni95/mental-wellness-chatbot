import tkinter as tk
from screens.chatbot import ChatBotScreen
from screens.mood_tracker import MoodTrackerScreen
from screens.breathing import BreathingApp
from screens.login_signup import LoginSignupScreen

class HomeScreen:
    def __init__(self, root, username):
        self.root = root
        self.username = username

        self.root.title("Home")
        self.root.geometry("400x400")

        welcome_label = tk.Label(root, text=f"Welcome, {username}!", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        chatbot_btn = tk.Button(root, text="Chatbot", width=20, command=self.open_chatbot)
        chatbot_btn.pack(pady=10)

        mood_btn = tk.Button(root, text="Mood Tracker", width=20, command=self.open_mood_tracker)
        mood_btn.pack(pady=10)

        breathing_btn = tk.Button(root, text="Breathing Exercise", width=20, command=self.open_breathing_exercise)
        breathing_btn.pack(pady=10)

        logout_btn = tk.Button(root, text="Logout", width=20, command=self.logout)
        logout_btn.pack(pady=10)

    def open_chatbot(self):
        self.root.destroy()
        new_root = tk.Tk()
        ChatBotScreen(new_root)
        new_root.mainloop()

    def open_mood_tracker(self):
        self.root.destroy()
        new_root = tk.Tk()
        MoodTrackerScreen(new_root, self.username)
        new_root.mainloop()

    def open_breathing_exercise(self):
        self.root.destroy()
        new_root = tk.Tk()
        BreathingApp(new_root, self.username)
        new_root.mainloop()

    def logout(self):
        self.root.destroy()
        new_root = tk.Tk()
        LoginSignupScreen(new_root)
        new_root.mainloop()
