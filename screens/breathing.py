import tkinter as tk
import time
import threading

class BreathingScreen(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.title("Breathing Exercise")
        self.geometry("400x300")
        self.configure(bg="#d0f0f0")

        self.label = tk.Label(self, text="Let's do a breathing exercise...", font=("Helvetica", 16), bg="#d0f0f0")
        self.label.pack(pady=30)

        self.instruction = tk.Label(self, text="", font=("Helvetica", 28), fg="blue", bg="#d0f0f0")
        self.instruction.pack(pady=10)

        start_btn = tk.Button(self, text="Start Exercise", command=self.start_breathing)
        start_btn.pack(pady=20)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_breathing(self):
        instructions = [("Inhale...", 4), ("Hold...", 4), ("Exhale...", 4)]
        def cycle():
            for _ in range(3):  # Repeat the cycle 3 times
                for text, sec in instructions:
                    self.instruction.config(text=text)
                    self.update()
                    time.sleep(sec)
            self.instruction.config(text="Great job!")

        threading.Thread(target=cycle).start()

    def on_close(self):
        self.destroy()
        from screens.home import HomeScreen
        HomeScreen(self.username)
