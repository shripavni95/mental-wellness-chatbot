import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from screens.home import HomeScreen  # ✅ This import is now safe!

class LoginSignupScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mental Wellness Chatbot - Login / Signup")
        self.geometry("400x300")
        self.configure(bg="#e0f7fa")
        self.eval('tk::PlaceWindow . center')

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Label(self, text="Username:", bg="#e0f7fa").pack(pady=(20, 5))
        self.username_entry = tk.Entry(self, textvariable=self.username_var)
        self.username_entry.pack()

        tk.Label(self, text="Password:", bg="#e0f7fa").pack(pady=(10, 5))
        self.password_entry = tk.Entry(self, textvariable=self.password_var, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login_user).pack(pady=(15, 5))
        tk.Button(self, text="Signup", command=self.signup_user).pack()

    def get_db_connection(self):
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "users.db")
        return sqlite3.connect(db_path)

    def login_user(self):
        username = self.username_var.get()
        password = self.password_var.get()
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()
        if result:
            self.destroy()
            HomeScreen(username).mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def signup_user(self):
        username = self.username_var.get()
        password = self.password_var.get()
        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Signup successful! Please login.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()
