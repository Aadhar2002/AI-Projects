#Create a simple sentiment analyzer using Textblob
from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
# Test the sentiment analyzer
print(analyze_sentiment("I love this product!"))
print(analyze_sentiment("This is the worst experience ever."))
print(analyze_sentiment("It's okay, not great but not bad either."))
