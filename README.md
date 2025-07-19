# Hiring Assistant Chatbot

This project is a hiring assistant chatbot for TalentScout, a fictional recruitment agency. The chatbot is designed to conduct initial screenings of candidates by gathering essential information and asking relevant technical questions.

## Project Overview

The chatbot is built using Python, Streamlit, and LangChain. It leverages a large language model (Google's Gemini Pro) to understand and respond to user input in a conversational manner. The chatbot maintains the context of the conversation to provide a seamless user experience.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hiring-assistant-chatbot.git
   cd hiring-assistant-chatbot
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory and add your Google API key:**
   ```
   GOOGLE_API_KEY="your_api_key"
   ```

## Usage

To run the chatbot, use the following command:

```bash
streamlit run app.py
```

This will open the chatbot interface in your web browser. You can interact with the chatbot by typing in the text input field.
