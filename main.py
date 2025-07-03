import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "MentalWellnessBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=["chatterbot.logic.BestMatch"],
    database_uri="sqlite:///db.sqlite3"
)

trainer = ChatterBotCorpusTrainer(chatbot)
custom_corpus_path = os.path.join(os.path.dirname(__file__), 'mental_corpus', 'mental_health.yml')
 
if os.path.exists(custom_corpus_path):
    try:
        trainer.train("mental_corpus.mental_health")
        print("✅ Custom mental health corpus training complete.")
    except Exception as e:
        print(f"⚠️ Failed to train with custom corpus: {e}")
        trainer.train("chatterbot.corpus.english")
        print("ℹ️ Fallback: Trained with default English corpus.")
else:
    print("⚠️ Custom mental health corpus not found.")
    trainer.train("chatterbot.corpus.english")
    print("ℹ️ Fallback: Trained with default English corpus.")

# Launch GUI
try:
    from screens.app_launcher import show_login_signup_screen
    show_login_signup_screen()
except ImportError as e:
    print(f"❌ GUI launch failed: {e}")
    print("💡 Make sure 'screens/app_launcher.py' exists and defines 'show_login_signup_screen()'")
