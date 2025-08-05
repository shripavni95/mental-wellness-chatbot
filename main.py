import tkinter as tk
from screens.login_signup import LoginSignupScreen

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSignupScreen(root)
    root.mainloop()
