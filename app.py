from flask import Flask, request, jsonify, render_template
import os
import joblib
import requests
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Allow cross-origin requests

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGpXwwEAAAAAmC98NIQZodrXjawlo9t8JSsCt4Q%3DOuWXSqlrJa2tfxY1vE8pQ1D304zByXowGxYwK2sMKMmXPMNkO8"

def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["data"]["id"]

def fetch_user_tweets(username, max_results=50):
    user_id = get_user_id(username)
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {"max_results": max_results}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return [tweet["text"] for tweet in response.json()["data"]]

# Load model and vectorizer
with open("tweet_model.joblib", "rb") as model_file:
    model = joblib.load(model_file)
with open("vectorizer.joblib", "rb") as vec_file:
    vectorizer = joblib.load(vec_file)

# Route for the frontend page
@app.route('/')
def index():
    return render_template('index.html')

# Route for sentiment analysis
@app.route('/analyze', methods=['POST'])
def analyze_sentiments():
    data = request.json
    username = data.get("username")

    try:
        tweets = fetch_user_tweets(username)
        tweet_vectors = vectorizer.transform(tweets)
        predictions = model.predict(tweet_vectors)
        sentiments = predictions.tolist()
        return jsonify({"tweets": tweets, "sentiments": sentiments})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
