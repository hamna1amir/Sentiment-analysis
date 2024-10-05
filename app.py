from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Sentiment Analysis Function
def analyze_sentiment(review):
    analysis = TextBlob(review)
    # Classify sentiment as positive or negative
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    else:
        return 'Negative'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        platform = request.form['platform']  # Get platform name
        review = request.form['review']  # Get review text
        sentiment = analyze_sentiment(review)  # Analyze sentiment
        return render_template('result.html', platform=platform, review=review, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
