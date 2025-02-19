import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download necessary resources
nltk.download("vader_lexicon")

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def get_sentiment_vader(text):
    """Analyze sentiment using VADER (returns a score between -1 and 1)."""
    score = sia.polarity_scores(text)
    return score["compound"]

def get_sentiment_textblob(text):
    """Analyze sentiment using TextBlob (returns a polarity score between -1 and 1)."""
    return TextBlob(text).sentiment.polarity

if __name__ == "__main__":
    test_text = "Stock market is crashing! Investors are panicking!"
    print(f"VADER Sentiment: {get_sentiment_vader(test_text)}")
    print(f"TextBlob Sentiment: {get_sentiment_textblob(test_text)}")