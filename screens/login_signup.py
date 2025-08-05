import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

class LoginSignupScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / Signup")
        self.root.geometry("400x300")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Button(root, text="Login", command=self.login_user).pack(pady=10)
        tk.Button(root, text="Signup", command=self.signup_user).pack(pady=10)

    def get_db_connection(self):
        # Use project-relative path for database
        db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "users.db")
        conn = sqlite3.connect(db_path)
        return conn

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.root.destroy()
            self.open_home_screen(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def signup_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
            )
            conn.commit()
            messagebox.showinfo("Signup Success", "Account created successfully! Please log in.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Signup Failed", "Username already exists.")
        finally:
            conn.close()

    def open_home_screen(self, username):
        import screens.home  # Delayed import avoids circular import
        new_root = tk.Tk()
        screens.home.HomeScreen(new_root, username)
        new_root.mainloop()
