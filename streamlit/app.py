# import streamlit library to create the web app
import streamlit as st

# import pickle to load the trained machine learning model
import pickle

# import preprocessing function to clean inpur text
from utils.preprocessing import clean_text

# import sentiment analysis function
from utils.sentiment import analyze_sentiment

# import AI summarization function (Groq LLM)
from utils.summarizer import summarize_news

# load trained machine leaning model and TF-IDF vectorizer

# load the trained logistic Regression model from model.pkl
model = pickle.load(open("model.pkl","rb"))

# load the TF-IDF vectorizer
# it converts text into numerical features before predictions
# it must be the same vectorizer used during training
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

# configure streamlit web page

st.set_page_config(
    # browser tab title
    page_title="AI News Intelligence System",

    # browser tab icon
    page_icon="🧠",

    # use full browser width
    layout="Wide",

    # sidebar remains expanded when app opens
    initial_sidebar_state="expanded"
)

# sidebar

with st.sidebar:

    # sidebar title
    st.title("🧠 AI News")

    st.markdown("---")

    # display application features
    st.write("### Features")
    st.write("✅ Fake News Detection")
    st.write("😊 Sentiment Analysis")
    st.write("🤖 AI Summary")

    st.markdown("---")

    # sidebar footer
    st.caption("Built with Streamlit")

    # main heading

    st.title("🧠 AI News Intelligence System")

    # short application description
    st.markdown("""
    Detect **Fake News**, analyze **Sentiment**, and generate an AI Summary** in one click.
    """)

    # User input section

    # Large text area where the user pastes a news article
    news = st.text_area(

        "📰 Paste News Article",

        height=250,

        placeholder="Paste your news article here..."
    )

    # center the analyze button

    # create three columns
    # the button is placed in the middle column
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        # Anlyze button
        analyze = st.button(
            "🚀 Analyze News",
            use_container_width=True
        )

# run analysis when button is clicked

if analyze:

    # check wheather user entered any text
    if not news.strip():

        st.warning("⚠ Please enter a news article.")
    else:

        # show progress bar

        progress = st.progress(0)

        # text preprocessing

        # clean the news article
        # removes punctuation, stopwards, converts to lowercase, etc.
        cleaned_text = clean_text(news)

        progress.progress(25)

        # convert text into numerical features

        # transform cleaned text into TF-IDF vectors
        news_vector = vectorizer.transform([cleaned_text])

        progress.progress(50)

        # fake news prediction

        # predict wheather the news is real or fake
        prediction = model.predict(news_vector)[0]

        progress.progress(75)

        # sentiment analysis

        # determine whether the article has
        # positive, Negeative or Neutral sentiment
        sentiment = analyze_sentiment(cleaned_text)

        progress.progress(100)

        # display success message
        st.success("Analysis Completed ✅")

        st.markdown("---")

        # display prediction results

        col1, col2 = st.columns(2)

        # left column - Fake News Detection
        with col1:

            st.subheader("📰 Fake News Detection")

            if prediction == 1:

                st.success("✅ Real News")

            else:

                st.error("❌ Fake News")

            # right column - sentiment
            with col2:

                st.subheader("😊 Sentiment Analysis")

                st.info(sentiment)

            st.markdown("---")

            # AI generated summary

            st.subheader("🤖 AI Generated Summary")

            # show loading spinner while waiting for Groq response
            with st.spinner("Generating summary..."):

                summary = summarize_news(news)

            # display summary inside an expandable section
            with st.expander("📄 View Summary", expanded=True):

                st.write(summary)
            

# footer

st.markdown("---")

# display tecnologies used in the project
st.caption("Developed using Python . Stramlit-Learn . Groq")