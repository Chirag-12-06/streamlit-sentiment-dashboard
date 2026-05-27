import streamlit as st
import pandas as pd
import plotly.express as px
import ast
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title("Sentiment Analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")

st.markdown("This application is a Streamlit dashboard that analyzes the sentiment of tweets about US airlines.🐦")
st.sidebar.markdown("This application is a Streamlit dashboard that analyzes the sentiment of tweets about US airlines.🐦")

PATH ="Tweets.csv"

@st.cache_data
def load_data():
    data_temp=pd.read_csv(PATH)
    data_temp["tweet_created"]=pd.to_datetime(data_temp["tweet_created"])
    return data_temp

data=load_data()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tweets", len(data))
col2.metric(
    "Positive",
    len(data[data.airline_sentiment == "positive"]))
col3.metric(
    "Neutral",
    len(data[data.airline_sentiment == "neutral"]))
col4.metric(
    "Negative",
    len(data[data.airline_sentiment == "negative"]))

st.sidebar.subheader("Show a Random Tweet")
random_tweet=st.sidebar.radio("Sentiment", ("Positive","Neutral","Negative"))
st.sidebar.markdown(data.query("airline_sentiment == @random_tweet.lower()")[["text"]].sample(n=1).iat[0,0])


st.sidebar.markdown("### Number of Tweets by Sentiments")
select=st.sidebar.selectbox("Visualization Type", ["Histogram","Pie Chart"], key='1')
sentiment_count=data["airline_sentiment"].value_counts()
sentiment_count=pd.DataFrame({"Sentiment":sentiment_count.index,"Tweets":sentiment_count.values})

if not st.sidebar.checkbox("Hide", True):
    st.sidebar.markdown("### Number of Tweets by Sentiments")
    if(select == "Histogram"):
        fig=px.bar(sentiment_count,x="Sentiment",y="Tweets",color="Tweets", height=500)
        st.plotly_chart(fig)
    else:
        fig=px.pie(sentiment_count,values="Tweets", names="Sentiment")
        st.plotly_chart(fig)

st.sidebar.subheader("When and Where are users tweeting from?")
hour=st.sidebar.slider("Hour of Day", 0, 23)
modified_data=data[data["tweet_created"].dt.hour == hour]
modified_data = modified_data.dropna(subset=["tweet_coord"])
modified_data["tweet_coord"] = modified_data["tweet_coord"].apply(ast.literal_eval)
modified_data["lat"] = modified_data["tweet_coord"].apply(lambda x: x[0])
modified_data["lon"] = modified_data["tweet_coord"].apply(lambda x: x[1])

if not st.sidebar.checkbox("Close", True, key = "2"):
    st.markdown("### Tweets locations based on time of the day")
    st.markdown("%i tweets between %i:00 and %i:00" % (len(modified_data), hour, (hour+1)%24))
    st.map(modified_data[["lat","lon"]])
    if st.sidebar.checkbox("Show Raw Data", False):
        st.write(modified_data)


st.sidebar.subheader("Breakdown Airline Tweets by Sentiments")
choice = st.sidebar.multiselect("Pick Airline", ("US Airways", "United", "American", "Southwest", "Delta", "Virgin America"), key='0')

if(len(choice)>0):
    choice_data=data[data.airline.isin(choice)]
    choice_fig=px.histogram(choice_data, x="airline", y="airline_sentiment", histfunc="count", color="airline_sentiment", facet_col="airline_sentiment", labels={"airline_Sentiment":"Tweets"}, height=600, width=800)
    st.plotly_chart(choice_fig)

st.sidebar.subheader("Word Cloud")
word_sentiment=st.sidebar.radio("Display word cloud for which sentiment?", ("Positive", "Negative", "Neutral"))

if not st.sidebar.checkbox("Close", True, key="3"):
    st.header("Wordcloud for %s sentiment" % (word_sentiment))
    df=data[data.airline_sentiment == word_sentiment.lower()]
    WORDS=" ".join(df["text"])
    PROCESSED_WORDS=' '.join([word for word in WORDS.split() if "http" not in word and not word.startswith("@") and word != "RT"])
    wordcloud=WordCloud(stopwords=STOPWORDS, background_color="white", height=400, width=800).generate(PROCESSED_WORDS)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)