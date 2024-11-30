import openai
import streamlit as st

# Set up the OpenAI API key
openai.api_key = 'your-openai-api-key'

# Function to interact with OpenAI's GPT model
def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or "gpt-3.5-turbo" depending on your preference
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,  # Controls randomness: 0.0 is deterministic, 1.0 is more random
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit page configuration
st.set_page_config(page_title="GPT Chat", page_icon=":robot:")

# Title and Description
st.title("GPT Chat Interface")
st.markdown("Welcome to the GPT chat interface powered by OpenAI's GPT-3.5! Ask me anything.")

# Chat history container
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to display chat history
def display_chat():
    for chat in st.session_state.history:
        st.markdown(f"**User:** {chat['user']}")
        st.markdown(f"**GPT:** {chat['gpt']}")

# User input form
with st.form(key="chat_form"):
    user_input = st.text_input("You:", "")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    # Add user input to history
    st.session_state.history.append({"user": user_input, "gpt": ""})
    
    # Get GPT response
    gpt_response = get_gpt_response(user_input)
    
    # Add GPT response to history
    st.session_state.history[-1]["gpt"] = gpt_response
    
    # Clear input box for next message
    st.experimental_rerun()

# Display chat history
display_chat()
