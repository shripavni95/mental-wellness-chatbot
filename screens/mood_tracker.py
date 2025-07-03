import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class MoodTrackerScreen(tk.Toplevel):
    def __init__(self, username):
        super().__init__()
        self.title("Mood Tracker")
        self.geometry("400x400")
        self.configure(bg="#e6f2f2")
        self.username = username

        tk.Label(self, text="How are you feeling today?", font=("Arial", 14), bg="#e6f2f2").pack(pady=10)

        moods = ["Happy", "Sad", "Anxious", "Stressed", "Angry", "Motivated", "Tired"]
        for mood in moods:
            tk.Button(self, text=mood, width=20, command=lambda m=mood: self.save_mood(m)).pack(pady=5)

        tk.Button(self, text="View Mood History", command=self.show_history).pack(pady=20)

        self.history_text = tk.Text(self, height=6, width=40)
        self.history_text.pack()
        self.history_text.config(state='disabled')

    def save_mood(self, mood):
        conn = sqlite3.connect("mental_wellness.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS moods (username TEXT, mood TEXT, timestamp TEXT)")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO moods VALUES (?, ?, ?)", (self.username, mood, timestamp))
        conn.commit()
        conn.close()
        messagebox.showinfo("Saved", f"Mood '{mood}' saved!")

    def show_history(self):
        conn = sqlite3.connect("mental_wellness.db")
        c = conn.cursor()
        c.execute("SELECT mood, timestamp FROM moods WHERE username = ? ORDER BY timestamp DESC LIMIT 5", (self.username,))
        rows = c.fetchall()
        conn.close()

        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        for mood, ts in rows:
            self.history_text.insert(tk.END, f"{ts} - {mood}\n")
        self.history_text.config(state='disabled')
