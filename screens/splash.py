import tkinter as tk
from tkinter import ttk
import time
from screens import login_signup  # We'll create this next

class SplashScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mental Wellness Chatbot")
        self.geometry("500x300")
        self.configure(bg="#b2d8d8")  # soft teal/pastel background
        self.overrideredirect(True)   # removes window decorations

        # Center the window
        self.eval('tk::PlaceWindow . center')

        # App title label
        label = ttk.Label(self, text="Mental Wellness Chatbot\nfor College Students",
                          font=("Helvetica", 18, "bold"),
                          background="#b2d8d8", foreground="#0a3d62",
                          justify="center")
        label.pack(expand=True)

        # Show splash for 3 seconds then open login screen
        self.after(3000, self.goto_login)

    def goto_login(self):
        self.destroy()
        login_signup.LoginSignupScreen()

if __name__ == "__main__":
    SplashScreen().mainloop()
