# Streamlit Sentiment Dashboard

Interactive Streamlit dashboard that visualizes sentiment analysis of tweets about US airlines using the provided Tweets.csv dataset.

**Deployed App**

- Live demo: [Streamlit Sentiment Dashboard](https://chirag-12-06-streamlit-sentiment-dashboard-app-q3rcub.streamlit.app/)

**Features**

- **Overview metrics:** Total tweets and counts by sentiment (positive, neutral, negative).
- **Random tweet:** View a random tweet by sentiment.
- **Visualizations:** Histogram or pie chart of sentiment distribution, per-airline sentiment breakdown, and a word cloud for selected sentiment.
- **Geolocation map:** Plot tweets on a map filtered by hour of day (if coordinates are present).

**Requirements**

- Python 3.8+
- Libraries: `streamlit`, `pandas`, `plotly`, `wordcloud`, `matplotlib`

**Installation**

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install streamlit pandas plotly wordcloud matplotlib
```

**Run the app**

```bash
streamlit run app.py
```

Open the URL shown by Streamlit (usually http://localhost:8501).

**Files**

- [app.py](app.py): Streamlit application source.
- [Tweets.csv](Tweets.csv): Dataset of tweets used by the dashboard.
- [README.md](README.md): This file.

**Notes**

- The app expects `Tweets.csv` to be located in the same folder as `app.py`. The dataset includes `tweet_created`, `airline_sentiment`, `text`, `airline`, and (optionally) `tweet_coord` columns.
- If geolocation mapping shows few points, many tweets may not include `tweet_coord` values.

**Troubleshooting**

- If the word cloud or plotting fails, confirm `wordcloud` and `matplotlib` are installed and restart the Streamlit server.
