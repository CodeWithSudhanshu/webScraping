# 📰 News Sentiment Analyzer

## 📌 Overview

News Sentiment Analyzer is a Python-based project that combines Web Scraping and Natural Language Processing (NLP) to analyze the sentiment of live news headlines.

The application scrapes the latest headlines from Inshorts, performs sentiment analysis using TextBlob, categorizes headlines into Positive, Negative, or Neutral sentiments, and visualizes the results using Matplotlib.

---

## 🚀 Features

✅ Scrapes live news headlines from Inshorts

✅ Stores scraped data in CSV format

✅ Performs sentiment analysis using NLP

✅ Classifies headlines into:

* Positive
* Negative
* Neutral

✅ Visualizes sentiment distribution through bar charts

---

## 🛠️ Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas
* TextBlob
* Matplotlib

---

## 📊 Workflow

1. Fetch live news headlines from Inshorts.
2. Extract headline text using BeautifulSoup.
3. Store headlines in a Pandas DataFrame.
4. Save data to a CSV file.
5. Analyze sentiment polarity using TextBlob.
6. Categorize sentiments into Positive, Negative, or Neutral.
7. Visualize sentiment distribution using Matplotlib.

---

## 📂 Project Structure

```bash
News-Sentiment-Analyzer/
│
├── news_sentiment.py
├── news_headlines.csv
├── README.md
└── requirements.txt
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/News-Sentiment-Analyzer.git
cd News-Sentiment-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python news_sentiment.py
```

---

## 📈 Sample Output

### Sentiment Classification

| Headline                               | Sentiment |
| -------------------------------------- | --------- |
| Market gains amid positive outlook     | Positive  |
| Heavy rainfall disrupts transportation | Negative  |
| Government announces new policy        | Neutral   |

### Visualization

The program generates a bar chart displaying the number of Positive, Negative, and Neutral news headlines.

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

* Web Scraping
* Data Collection
* Natural Language Processing (NLP)
* Sentiment Analysis
* Data Visualization
* Python Libraries Integration

---

## 🔮 Future Improvements

* Streamlit Dashboard Integration
* Multiple News Source Support
* Sentiment Trend Analysis
* Word Cloud Visualization
* Real-Time News Monitoring
* Export Reports in PDF Format

---

