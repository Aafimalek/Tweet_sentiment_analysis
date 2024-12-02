
# Twitter Sentiment Analysis Web App

A user-friendly web application for analyzing the sentiment of tweets from any Twitter user. Leveraging machine learning, the app provides insights into whether tweets are generally positive or negative. It uses Flask as a backend server, a pre-trained model for sentiment analysis, and a simple yet elegant frontend.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [License](#license)

---

### Features

- **Fetch Tweets**: Retrieves the latest tweets from a given Twitter user using Twitter API v2.
- **Sentiment Analysis**: Analyzes each tweet's sentiment (positive or negative) using a machine learning model.
- **Easy-to-Use UI**: Simple input field and responsive design, making the app accessible on both desktop and mobile.

---

### Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-learn (with a saved model and vectorizer)
- **Twitter API**: v2 Endpoints for tweet retrieval

---

### Project Structure

```
project-root/
├── app.py                  # Backend (Flask app)
├── tweet_model.joblib      # Trained model
├── vectorizer.joblib       # Trained vectorizer
├── templates/
│   └── index.html          # Frontend HTML file
└── static/
    ├── style.css           # CSS styling
    └── script.js           # JavaScript frontend logic

```

---

### Setup and Installation

#### Prerequisites

- **Python 3.8+**
- **Twitter Developer Account** with API v2 access
- **Flask**, **joblib**, **requests**, **scikit-learn**

#### Step 1: Clone the Repository

```bash
git clone https://github.com/Aafimalek/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

#### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 3: Set Up Twitter API Keys

1. Go to the Twitter Developer Portal and create an application.
2. Obtain your **Bearer Token**.
3. Add your Bearer Token to the `app.py` file:

```python
BEARER_TOKEN = "your_bearer_token_here"
```

#### Step 4: Run the Application

```bash
cd backend
python app.py
```

#### Step 5: Open the Application

1. Open `frontend/index.html` in your browser.
2. Input a Twitter username to start analyzing sentiments.

---

### Usage

1. **Enter Twitter Username**: Type in the handle (without the `@`) of any Twitter user.
2. **Click "Analyze"**: The app will fetch the user's recent tweets and analyze them.
3. **View Results**: The app displays each tweet with a sentiment label (Positive/Negative).

---

### Screenshots

#### Homepage
![Homepage]![{C59D90A6-411B-40B8-99A9-123B976035C4}](https://github.com/user-attachments/assets/f8e13b3a-19ce-46a2-b02c-32b938201f59)


#### Sentiment Analysis Results
![Results](path_to_results_screenshot.png)

---

### Future Improvements

- **Enhanced Sentiment Categories**: Add more sentiment classes like "Neutral" or "Mixed".
- **Data Visualization**: Use charts to show sentiment distribution.
- **Additional Filters**: Filter tweets by date or topic.
- **Authentication**: Allow users to log in with their Twitter accounts.

---

### License

This project is licensed under the MIT License.

