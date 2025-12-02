import subprocess
import traceback
import time
import os
from replit import db
from flask import Flask
from threading import Thread
# Import waitress
from waitress import serve

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
    # Run Flask using Waitress (Production WSGI server)
    port = int(os.getenv("PORT", 8000))
    
    # 'threads=6' handles multiple requests at once without blocking
    serve(app, host='0.0.0.0', port=port, threads=6)

def run_discourse_bot():
    while True:
        try:
            # Added flush=True to ensure logs appear immediately in Replit
            result = subprocess.run(["python", "discoursebot.py"], text=True, check=False)

            if result.returncode == 42:
                print("Shutdown sequence complete.")
                break  # stop restarting

            if result.returncode != 0:
                print("\nAn error occurred while running discoursebot.py:")
                print(f"Return Code: {result.returncode}")
                # args is a list, converting to string for clearer print
                print(f"Command: {' '.join(result.args)}") 
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
    db["version"] = "2.2.1"

    # Start the web server in a background thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Start discourse bot in the main thread
    run_discourse_bot()