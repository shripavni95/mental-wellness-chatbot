🧠 Mental Wellness Chatbot

A desktop application built using Python and Tkinter to support the mental well-being of college students. It includes login/signup, a mood tracker, breathing exercises, and an intelligent chatbot for emotional support.

💡 Features

- **Login & Sign-up** screen with basic validation
- **Mood Tracker** to log and reflect on daily emotional states
- **Breathing Exercises** for relaxation and stress relief
- **Chatbot** built using ChatterBot for mental wellness conversation
- **Multi-screen Navigation** using Tkinter frames
- **Data Storage** using SQLite database

---

🗂️ Project Structure

MENTALWELLNESSCHATBOT/
├── assets/ # Images and visual assets
├── ChatterBot/ # Pre-trained chatbot package
├── database/
│ ├── appdata.db # Main app database
│ ├── setup_db.py # DB setup script
│ └── users.db # User info DB
├── mental_corpus/
│ └── mental_health.yml # Custom chatbot corpus
├── screens/ # All UI screens
│ ├── app_launcher.py
│ ├── home.py
│ ├── login_signup.py
│ ├── mood_tracker.py
│ ├── breathing.py
│ ├── chatbot.py
│ └── splash.py
├── utils/ # Utility functions (if any)
├── venv/ # Virtual environment
└── main.py # Entry point to run the app
