import tkinter as tk
import time
import threading

class BreathingApp(tk.Toplevel):
    def __init__(self, root, username):
        super().__init__(root)
        self.username = username  # ✅ Store username
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
            start_time = time.time()
            while time.time() - start_time < 240:  # Run for 4 minutes
                for text, sec in instructions:
                    if time.time() - start_time >= 240:
                        break
                    self.instruction.config(text=text)
                    self.update()
                    time.sleep(sec)
            self.instruction.config(text="Great job!")
            time.sleep(2)
            self.on_close()

        threading.Thread(target=cycle).start()

    def on_close(self):
        self.destroy()
        from screens.home import HomeScreen
        new_root = tk.Tk()
        HomeScreen(new_root, self.username)  # ✅ Pass username correctly
        new_root.mainloop()
