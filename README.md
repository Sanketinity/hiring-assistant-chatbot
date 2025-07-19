# Hiring Assistant Chatbot

An intelligent conversational AI system designed to streamline the initial candidate screening process for recruitment agencies. Built with modern NLP technologies and a user-friendly interface.

## Project Overview

The Hiring Assistant Chatbot is a sophisticated recruitment tool developed for TalentScout that automates the initial candidate screening process. This AI-powered chatbot conducts structured interviews by gathering essential candidate information and asking relevant technical questions based on their expertise.

### Key Capabilities:
- **Automated Information Gathering**: Systematically collects candidate details including contact information, experience, and technical skills
- **Dynamic Technical Assessment**: Generates contextual technical questions based on the candidate's stated tech stack
- **Sentiment Analysis**: Real-time emotion detection to gauge candidate responses and engagement
- **Conversation Memory**: Maintains context throughout the entire interview session
- **Professional Interface**: Clean, intuitive web-based chat interface with custom styling
- **Structured Workflow**: Follows a predefined 10-step screening process for consistency

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Google API key for Gemini AI model
- Git (for cloning the repository)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sanketinity/hiring-assistant-chatbot.git
   cd hiring-assistant-chatbot
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

5. **Obtain Google API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key for Gemini
   - Copy the key to your `.env` file

6. **Verify Installation**
   ```bash
   streamlit run app.py
   ```

## Usage Guide

### Starting the Application
```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501`

### Interview Process
1. **Initial Greeting**: The chatbot introduces itself and explains the process
2. **Information Collection**: Systematically gathers:
   - Full name
   - Email address
   - Phone number
   - Years of experience
   - Desired position(s)
   - Current location
   - Technical skills/stack
3. **Technical Assessment**: Asks 3-5 relevant questions based on stated technologies
4. **Conclusion**: Thanks candidate and explains next steps

### Features During Interview
- **Real-time Sentiment Analysis**: View candidate emotion analysis in the sidebar
- **Conversation History**: Full chat history maintained throughout session
- **Exit Command**: Type 'exit' to end the interview gracefully
- **Error Handling**: Graceful handling of API errors and edge cases

## Technical Details

### Architecture Overview
The application follows a modular architecture with clear separation of concerns:

```
├── app.py              # Main application entry point
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # Custom UI styling
└── .env               # Environment variables (not tracked)
```

### Libraries and Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| `streamlit` | Latest | Web application framework and UI |
| `langchain` | Latest | LLM orchestration and memory management |
| `langchain-google-genai` | Latest | Google Gemini AI integration |
| `python-dotenv` | Latest | Environment variable management |
| `text2emotion` | Latest | Sentiment analysis and emotion detection |
| `nltk` | Latest | Natural language processing utilities |
| `Pillow` | Latest | Image processing (for potential logo display) |

### Model Configuration
- **Primary Model**: Google Gemini 1.5 Flash
- **Temperature**: 0.7 (balanced creativity and consistency)
- **Memory Type**: ConversationBufferMemory (full conversation context)
- **Prompt Engineering**: Structured template with clear instructions

### Data Flow
1. User input → Streamlit interface
2. Input processing → LangChain prompt template
3. Context injection → Conversation memory
4. AI generation → Google Gemini API
5. Response processing → Sentiment analysis
6. Output rendering → Streamlit chat interface

## Prompt Design

### Core Prompt Strategy
The chatbot uses a carefully crafted prompt template that ensures consistent, professional interactions:

```python
prompt_template = """You are a friendly and professional hiring assistant chatbot for a company called TalentScout.
Your goal is to conduct an initial screening of candidates by following these steps:
1. Greet the candidate and introduce yourself.
2. Ask for the candidate's full name.
3. Ask for the candidate's email address.
4. Ask for the candidate's phone number.
5. Ask for the candidate's years of experience.
6. Ask for the candidate's desired position(s).
7. Ask for the candidate's current location.
8. Ask for the candidate's tech stack (programming languages, frameworks, databases, etc.).
9. Based on the tech stack, ask 3-5 relevant technical questions. One by one
10. After the questions, thank the candidate for their time and explain the next steps.

Keep the conversation friendly and professional. Maintain the context of the conversation.
"""
```

### Key Design Principles

1. **Sequential Structure**: 10-step process ensures no information is missed
2. **Context Awareness**: Conversation history maintained for natural flow
3. **Adaptive Questioning**: Technical questions generated based on candidate's skills
4. **Professional Tone**: Balanced friendly and business-appropriate language
5. **Clear Instructions**: Explicit guidance for consistent behavior

### Technical Question Generation
The AI dynamically generates relevant technical questions by:
- Analyzing the candidate's stated tech stack
- Selecting appropriate difficulty levels
- Asking questions one at a time for better engagement
- Covering different aspects (theoretical, practical, problem-solving)

## Challenges & Solutions

### Challenge 1: Maintaining Conversation Context
**Problem**: Early versions lost context between interactions, leading to repetitive questions.

**Solution**: Implemented LangChain's ConversationBufferMemory to maintain full conversation history, ensuring the chatbot remembers all previous interactions and can reference earlier responses.

### Challenge 2: Dynamic Technical Question Generation
**Problem**: Creating relevant technical questions based on diverse technology stacks mentioned by candidates.

**Solution**: Designed a flexible prompt that instructs the AI to analyze the candidate's tech stack and generate contextually appropriate questions. The AI leverages its training data to ask relevant questions across different technologies.

### Challenge 3: Handling API Rate Limits and Errors
**Problem**: Google Gemini API calls could fail due to rate limits or network issues.

**Solution**: Implemented comprehensive error handling with try-catch blocks, user-friendly error messages, and graceful degradation. The application continues to function even when API calls fail.

### Challenge 4: Real-time Sentiment Analysis
**Problem**: Integrating emotion detection without impacting conversation flow.

**Solution**: Used the text2emotion library for lightweight, real-time sentiment analysis displayed in a sidebar. This provides insights without interrupting the main conversation interface.

### Challenge 5: Professional UI/UX Design
**Problem**: Default Streamlit interface looked too basic for a professional recruitment tool.

**Solution**: Created custom CSS styling to enhance the visual appeal, implemented proper chat message formatting, and designed a clean, professional interface that builds candidate confidence.

### Challenge 6: Environment Configuration Management
**Problem**: Securely managing API keys and configuration across different deployment environments.

**Solution**: Implemented python-dotenv for environment variable management, created comprehensive setup instructions, and added proper .gitignore rules to prevent credential exposure.

### Challenge 7: Conversation Flow Control
**Problem**: Ensuring the chatbot follows the structured interview process without being too rigid.

**Solution**: Designed a flexible prompt that maintains the 10-step structure while allowing natural conversation flow. Added an 'exit' command for graceful conversation termination.

## Future Enhancements

- **Multi-language Support**: Expand to support interviews in multiple languages
- **Resume Analysis**: Integrate PDF resume parsing and analysis
- **Video Interview**: Add video call capabilities for remote screening
- **Analytics Dashboard**: Comprehensive reporting on candidate interactions
- **Integration APIs**: Connect with popular ATS (Applicant Tracking Systems)
- **Advanced Scoring**: Implement automated candidate scoring algorithms

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions, issues, or contributions, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ for modern recruitment processes**
