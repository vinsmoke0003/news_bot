from flask import Flask, request
from twilio.rest import Client
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Config
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
TO_NUMBER = os.getenv("MY_WHATSAPP_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH)

import random  # 👈 Add this at the top

def get_top_headlines():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    res = requests.get(url).json()

    articles = res.get('articles', [])
    random.shuffle(articles)  # 👈 Shuffle articles

    articles = articles[:10]  # Now take random 10
    if not articles:
        return "⚠️ No headlines available right now."

    return "\n\n".join([f"{i+1}. {a['title']}" for i, a in enumerate(articles)])



@app.route("/send-news", methods=["GET"])
def send_news():
    headlines = get_top_headlines()
    message = f"🗞 Top 10 Headlines Today:\n\n{headlines}"

    client.messages.create(
        from_=FROM_NUMBER,
        to=TO_NUMBER,
        body=message
    )
    return "Sent", 200

@app.route("/")
def home():
    return "✅ Flask is running. Go to /send-news to send WhatsApp news."

if __name__ == "__main__":
    headlines = get_top_headlines()
    message = f"🗞 Top 10 Headlines Today:\n\n{headlines}"

    client.messages.create(
        from_=FROM_NUMBER,
        to=TO_NUMBER,
        body=message
    )

    print("✅ News sent to WhatsApp!")

    # Optional: keep Flask running if needed
    # app.run(port=5000, debug=True)
