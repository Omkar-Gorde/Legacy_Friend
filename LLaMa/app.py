import streamlit as st
from transformers import pipeline
import pandas as pd
# Load the sentiment-analysis pipeline from transformers

def get_data():
    df_main = pd.read_csv('feedback.csv')
    return df_main

@st.cache_resource  # Cache the model to speed up load times
def load_model():
    return pipeline("sentiment-analysis")



import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Login Page", page_icon=":bar_chart:", layout="centered")
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://img.freepik.com/free-photo/indian-republic-day-celebration-digital-art-with-people_23-2151070643.jpg?t=st=1729920275~exp=1729923875~hmac=fe988e53c78ae5239f4bbfbc72cd6f7bc9d1e843c9a4bade258604df81d3bd27&w=1380");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

another_img="https://w0.peakpx.com/wallpaper/139/711/HD-wallpaper-financial-stock-market-graph-on-stock-market-investment-trading-bullish-point-bearish-point-trend-of-graph-for-business-idea-and-all-art-work-design-vector-illustration-5299428-vector-art-at-vecteezy.jpg"
sec_img="https://wallpapers.com/images/high/stock-market-simple-representation-mqustwxvlchtj32h.webp"


my_js=  f'''
alert('welcome Admin, your authorization was successful');

'''




st.markdown(
    "<h1 style='color: black;'>PoliMeta: Bridge the gap between policies and People with AI</h1>",
    unsafe_allow_html=True
)


st.write(
    """
    Welcome to **PoliMeta**, an AI-powered platform for enhancing citizen engagement and policymaking.
    
    Here, your feedback is crucial! Just like your votes, your opinions shape the future of our communities. 
    Participate in providing valuable insights that will help drive effective and inclusive policies.
    """
)

# Create a sidebar with fancy buttons and informative message
with st.sidebar:
    st.header("Why Your Participation Matters")
    st.write(
        """
        Your feedback is not just important; it's vital! Here’s why:
        
        - **Empowerment**: Your voice influences policy decisions.
        - **Representation**: Ensure that your needs and concerns are addressed.
        - **Impact**: Contribute to data-driven insights that shape the future.
        """
    )

    # Fancy buttons
    if st.button("Join the Conversation", key='join'):
        st.write("Thank you for joining! Your feedback will be invaluable.")
    
    if st.button("Learn More About Policies", key='learn_more'):
        st.write("Explore how your input can impact local policies.")

    # Style with custom CSS
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50; /* Green */
            color: white;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .stButton>button:hover {
            background-color: #45a049; /* Darker green */
        }
        
        .stSidebar {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )



  




# Custom CSS to set the background image (with a relative path)
background_css = """
<style>
body {
    background-image: url('stock1.jpg');
    background-size: cover;
}
</style>
"""

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)





