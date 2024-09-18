# Gemini Q&A and Image Insights 🧠🖼️

![Gemini AI](https://img.shields.io/badge/Powered%20by-Gemini%20AI-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.7+-yellow)

Gemini Q&A and Image Insights is a multi-functional application that integrates Google's Gemini AI to handle both text-based queries and image analysis. This project enables users to ask questions and upload images for analysis, providing dynamic responses powered by advanced large language models (LLMs) and computer vision technology.

## 🌟 Features

- **Text-Based Q&A**: Real-time answers to user questions using Gemini AI.
- **Image Insights**: Upload images for AI-powered analysis and description.
- **Streamlit Interface**: User-friendly and easy-to-deploy web application.
- **AI Model**: Leverages Gemini AI models (gemini-pro for Q&A, gemini-1.5-flash for image insights).

## 🚀 Key Functionalities

### Text Query Handling
- Input questions and receive streamed responses from Gemini AI.
- View and track chat history within the session.

### Image Processing & Insights
- Upload images (jpg, jpeg, png) with optional prompts.
- Receive detailed AI-generated insights based on image content.

### Session Management
- Preserve chat history for continuous conversation.
- Download responses as text files.

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Satviksangamkar/Gemini-Q-A-and-Image-Insights.git
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**
   Create a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the App**
   ```bash
   streamlit run filename.py
   ```

## 📘 Usage

### Q&A Functionality
1. Input your question in the text box.
2. Click "Ask the question".
3. View the AI's response in real-time.

### Image Insights
1. Upload an image via the sidebar.
2. Optionally provide a related prompt.
3. Click "Tell me about the image" for AI analysis.

## 📁 File Structure

- `qachat.py`: Main Q&A functionality handler.
- `vision.py`: Image upload and analysis module.
- `requirements.txt`: Project dependencies.
- `.env`: Secure storage for API key.
- `README.md`: Project documentation.

## 📋 Requirements

- Python 3.7+
- Streamlit
- Pillow
- Google Generative AI
- python-dotenv

## 🛠️ Technologies Used

- **Python**: Main programming language.
- **Streamlit**: Web app interface.
- **Google Generative AI (Gemini)**: Q&A and image analysis.
- **Pillow**: Image processing.
- **Dotenv**: Environment variable management.

## 🧠 Skills Involved

- **Python Programming**: Advanced scripting and application development.
- **AI and Machine Learning**: Integration of large language models and computer vision.
- **Web Development**: Creating interactive web applications with Streamlit.
- **API Integration**: Working with Google's Generative AI APIs.
- **Image Processing**: Handling and analyzing image data.
- **User Interface Design**: Creating an intuitive and responsive UI.
- **Version Control**: Using Git for project management.
- **Environment Management**: Handling dependencies and environment variables.
- **Documentation**: Creating clear and comprehensive README and inline comments.

## 🔮 Future Enhancements

- [ ] Multi-image comparison and insights.
- [ ] Implement caching for improved performance.
- [ ] Expand AI capabilities for diverse query types.
