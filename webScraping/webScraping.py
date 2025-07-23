import requests
import pandas as pd
from bs4 import BeautifulSoup
import textblob.download_corpora
from textblob import TextBlob
import matplotlib.pyplot as plt

textblob.download_corpora.download_all()
# Lets go to the website
url = 'https://inshorts.com/en/read'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
headlines = soup.find_all('span', itemprop='headline')
for i, headline in enumerate(headlines):
    print(f"{i+1}. {headline.text}")

data = pd.DataFrame({'headline': [h.text for h in headlines]})

# Save 
data.to_csv('news_headlines.csv', index=False)

print("Saved to news_headlines.csv")

# Creating new columns
data['polarity'] = data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)

def check_sentiment(p):
    if p > 0:
        return 'Positive'
    elif p < 0:
        return 'Negative'
    else:
        return 'Neutral'

data['sentiment'] = data['polarity'].apply(check_sentiment)

print(data.head())

#  Now counting each sentiment type
data['sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])

plt.title("Sentiment of News Headlines")
plt.xlabel("Sentiment Type")
plt.ylabel("Number of Headlines")
plt.show()
