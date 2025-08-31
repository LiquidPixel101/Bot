import subprocess
import traceback
import time
import os
from replit import db
from flask import Flask
from threading import Thread

print(
"""
|--------------|
|              |
|     BOT      |
|              |
|--------------|
"""
)

# Initialize Flask app
app = Flask(__name__)

# Define a simple health check endpoint
@app.route('/')
def health_check():
    return {"status": "Bot is running"}, 200

def run_flask():
    # Run Flask on the port specified by Replit (default 8000)
    port = int(os.getenv("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)

def run_discourse_bot():
    while True:
        try:
            result = subprocess.run(["python", "discoursebot.py"], text=True, check=False)

            if result.returncode == 42:
                print("Shutdown sequence complete.")
                break  # stop restarting

            if result.returncode != 0:
                print("\nAn error occurred while running discoursebot.py:")
                print(f"Return Code: {result.returncode}")
                print(f"Command: {result.args}")
                print(f"Output: {result.stdout}")
                print(f"Error: {result.stderr}")
                time.sleep(0.5)
                continue

            print("Bot exited cleanly. Stopping.")
            break

        except Exception:
            print("\nAn unexpected error occurred:")
            print(traceback.format_exc())
            time.sleep(0.5)


if __name__ == "__main__":
    db["version"]="2.2.1"
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start discourse bot in the main thread
    run_discourse_bot()
