from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Set up the API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get responses
def get_gemini_response(prompt, image):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use the updated model
    if prompt:
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

# Sidebar for inputs
st.sidebar.header("Input Options")
input_prompt = st.sidebar.text_input("Input Prompt: ", key="input")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Instructions
st.markdown("### Instructions")
st.write("Upload an image and enter a prompt to get information about the image.")

# Main area for image display
st.header("Gemini Application")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
else:
    image = None
    st.warning("Please upload an image to proceed.")

submit = st.button("Tell me about the image")

# If the submit button is clicked
if submit:
    if image is None:
        st.error("Please upload an image before submitting.")
    else:
        with st.spinner("Generating response..."):
            response = get_gemini_response(input_prompt, image)
        
        st.subheader("The Response is")
        st.markdown(response)  # Use markdown for better formatting

        # Add a download button for the response if it exists
        if response:
            st.download_button("Download Response", response, file_name="response.txt", mime="text/plain")
