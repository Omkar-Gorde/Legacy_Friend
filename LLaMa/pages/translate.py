import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit page title
st.title("English to Marathi Translator")

# Text input for user
input_text = st.text_area("Enter text in English:", "")

# Perform translation when button is clicked
if st.button("Translate"):
    if input_text:
        try:
            # Translate the text
            translated_text = GoogleTranslator(source='en', target='mr').translate(input_text)
            
            # Display the result
            st.write(f"**Translated Text in Marathi:** {translated_text}")
        except Exception as e:
            st.write(f"Error: {str(e)}")
    else:
        st.write("Please enter some text to translate.")
