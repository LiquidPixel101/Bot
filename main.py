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
    app.run(host='0.0.0.0', port=port)

def run_discourse_bot():
    while True:
        try:
            # Update to correct filename: discoursebot (2).py
            subprocess.run(["python", "discoursebot.py"], check=True)
        except subprocess.CalledProcessError as e:
            print("\nAn error occurred while running discoursebot (2).py:")
            print(f"Return Code: {e.returncode}")
            print(f"Command: {e.cmd}")
            print(f"Output: {e.output}")
            print(f"Error: {e.stderr}")
        except Exception as e:
            print("\nAn unexpected error occurred:")
            print(traceback.format_exc())
        time.sleep(0.5)

if __name__ == "__main__":
    db["version"]="2.1.5"
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start discourse bot in the main thread
    run_discourse_bot()