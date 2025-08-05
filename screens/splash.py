import tkinter as tk
from screens.login_signup import LoginSignupScreen  # adjust this path if needed

class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        self.root.geometry("600x400")
        self.root.configure(bg="#DCE6F1")

        # Splash message
        label = tk.Label(
            self.root,
            text="Welcome to the Mental Wellness Chatbot",
            font=("Helvetica", 16, "bold"),
            bg="#DCE6F1",
            fg="#333"
        )
        label.pack(expand=True)

        # Go to LoginSignup after 2 seconds
        self.root.after(2000, self.show_login_signup)

    def show_login_signup(self):
        self.root.destroy()
        login_root = tk.Tk()
        app = LoginSignupScreen(login_root)
        login_root.mainloop()


# Only run splash if this is the entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = SplashScreen(root)
    root.mainloop()
