from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")  # Bot token from Render environment

# --- Personality setup ---
def start(update, context):
    update.message.reply_text("Hey 👋 I'm your coding buddy. Ask me anything!")

def chat(update, context):
    text = update.message.text.lower()

    # If user asks for C++ code
    if "code" in text or "cpp" in text or "c++" in text:
        # Simple example: printing hello world
        cpp_code = '''#include <iostream>
using namespace std;

int main() {
    cout << "Hello, world!" << endl;
    return 0;
}'''
        update.message.reply_text("Sure! Here's a simple C++ code snippet:\n\n" + cpp_code)
    
    # Otherwise, casual friendly chat
    else:
        responses = [
            "Sounds cool 😎 Tell me more!",
            "Haha, I get you! 🔥",
            "Interesting... wanna dive into some coding?",
            "That’s nice 👍 I can also write you some C++ if you want."
        ]
        import random
        update.message.reply_text(random.choice(responses))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    updater.start_polling()

# Webserver for Render
@app.route('/')
def home():
    return "Bot is running on Render ✅"

if __name__ == '__main__':
    main()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
