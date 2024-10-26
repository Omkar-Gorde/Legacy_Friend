import streamlit as st
from transformers import pipeline

# Load the sentiment-analysis pipeline from transformers
@st.cache_resource  # Cache the model to speed up load times
def load_model():
    return pipeline("sentiment-analysis")

sentiment_analyzer = load_model()

# Streamlit page title
st.title("Simple Sentiment Analysis with AI")

# Text input for user
input_text = st.text_area("Enter text for sentiment analysis:", "")

# Perform sentiment analysis when button is clicked
if st.button("Analyze Sentiment"):
    if input_text:
        # Run the sentiment analysis pipeline
        result = sentiment_analyzer(input_text)
        sentiment = result[0]['label']
        score = result[0]['score']

        # Display the result
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Confidence:** {score:.2f}")
    else:
        st.write("Please enter some text to analyze.")

