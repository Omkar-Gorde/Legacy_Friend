import streamlit as st
import requests
from PIL import Image

# Set up Streamlit app title and description
st.title("Image Classification for Civic Issues")
st.write(
    "Help filter out unnecessary posts using AI. Upload an image to check if it's relevant to civic issues."
)

# Hugging Face API setup - Replace with your Hugging Face API token
api_token = "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"
api_url = (
    "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
)
headers = {"Authorization": f"Bearer {api_token}"}

# Keywords representing civic issues
civic_keywords = [
    "traffic",
    "accident",
    "pothole",
    "roadblock",
    "pollution",
    "fire",
    "flood",
    "road",
    "repair",
]


def query(image_data):
    # Make the request to the Hugging Face API with image bytes
    response = requests.post(api_url, headers=headers, data=image_data)

    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response with captions
    else:
        st.write("Error:", response.status_code, response.content)
        return {
            "error": f"Classification failed with status code {response.status_code}"
        }


def is_relevant_caption(caption, keywords):
    # Check if any keyword is present in the generated caption
    return any(keyword.lower() in caption.lower() for keyword in keywords)


# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image and caption result
if uploaded_file is not None:
    # Display the image in the app
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the uploaded image to bytes
    image_data = uploaded_file.getvalue()
    st.write("Generating caption...")

    # Get the caption from the model
    result = query(image_data)

    # Display caption result
    if "error" not in result:
        caption = result[0].get("generated_text", "No caption generated.")
        st.write("Caption:", caption)

        # Check if the caption is relevant
        if is_relevant_caption(caption, civic_keywords):
            st.write("This image is *relevant* to civic issues.")
        else:
            st.write("This image is *not relevant* to civic issues.")
    else:
        st.write("Error:", result["error"])