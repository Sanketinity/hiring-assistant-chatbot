# ============================================================================
# IMPORTS
# ============================================================================
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from PIL import Image
import text2emotion as te
import nltk

# Download required NLTK data
nltk.download('punkt_tab')

# ============================================================================
# CONFIGURATION
# ============================================================================
# Load environment variables
load_dotenv()

# Initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# ============================================================================
# PROMPT TEMPLATE
# ============================================================================
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

Conversation History:
{history}

Candidate: {input}
Hiring Assistant:
"""

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def load_css(file_path):
    """Load CSS file for styling the Streamlit app."""
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def analyze_sentiment(text):
    """
    Analyze the sentiment/emotion of the given text.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        tuple: (dominant_emotion, emotion_scores)
    """
    emotion_scores = te.get_emotion(text)
    if not emotion_scores:
        return "N/A", {}
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return dominant_emotion, emotion_scores


def get_llm_chain():
    """
    Initialize and return the LLM chain with memory for conversation context.
    
    Returns:
        LLMChain: Configured chain with prompt template and memory
    """
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=prompt_template
    )
    
    memory = ConversationBufferMemory(memory_key="history")
    
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=True
    )
    
    return llm_chain

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """
    Main function to run the Hiring Assistant Chatbot Streamlit application.
    """
    # Configure Streamlit page
    st.set_page_config(
        page_title="Hiring Assistant Chatbot", 
        page_icon=":briefcase:"
    )
    
    # Load custom CSS styling
    load_css("static/style.css")

    # Optional: Add company logo
    # Uncomment and replace with your own logo path
    # logo = Image.open("static/logo.png")
    # st.image(logo, width=100)

    # Page header and instructions
    st.title("Hiring Assistant Chatbot")
    st.write("Welcome to TalentScout! I'm here to help with the initial screening of candidates.")
    st.write("Please provide your information as requested. Type 'exit' to end the conversation.")

    # Initialize session state for LLM chain
    if "llm_chain" not in st.session_state:
        st.session_state.llm_chain = get_llm_chain()

    # Initialize session state for conversation messages
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Generate initial greeting from the assistant
        initial_greeting = st.session_state.llm_chain.run("Hi")
        st.session_state.messages.append({
            "role": "assistant", 
            "content": initial_greeting
        })

    # Display conversation history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    if user_input := st.chat_input("Your response:"):
        # Add user message to conversation
        st.session_state.messages.append({
            "role": "user", 
            "content": user_input
        })
        
        with st.chat_message("user"):
            st.markdown(user_input)

        # Process user input and generate response
        if user_input.lower() == "exit":
            response = ("Thank you for your time. The next step is a technical interview "
                       "with one of our engineers. We will be in touch with you shortly. "
                       "Have a great day!")
        else:
            try:
                # Generate AI response
                response = st.session_state.llm_chain.run(user_input)
                
                # Perform sentiment analysis
                dominant_emotion, emotion_scores = analyze_sentiment(user_input)
                
                # Display sentiment analysis in sidebar
                st.sidebar.subheader("Sentiment Analysis")
                st.sidebar.write(f"**Dominant Emotion:** {dominant_emotion}")
                st.sidebar.write("**Emotion Scores:**")
                st.sidebar.write(emotion_scores)
                
            except Exception as e:
                response = f"Sorry, an error occurred: {e}"
                st.error(response)

        # Add assistant response to conversation
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response
        })
        
        with st.chat_message("assistant"):
            st.markdown(response)


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
