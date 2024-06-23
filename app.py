import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()  # Load environment variables from .env file

secret_key = os.getenv("SECRET_KEY")
# Configure the Google Generative AI API
genai.configure(api_key=secret_key)

# Function to get response from Gemini
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Initialize session state
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'name': '',
        'age': 16,  # Set a valid default age within the range
        'education': '',
        'skills': '',
        'interests': '',
        'preferred_industries': ''
    }

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Define the sidebar navigation
st.sidebar.title("Career Guidance Chat")
page = st.sidebar.radio("Go to", ["User Profile", "Chat"])

if 'query' not in st.session_state:
    st.session_state.query = ""

# User Profile Page
if page == "User Profile":
    st.title("User Profile")

    # User inputs
    st.session_state.user_profile['name'] = st.text_input("Name", st.session_state.user_profile['name'])
    st.session_state.user_profile['age'] = st.number_input(
        "Age", min_value=16, max_value=100, step=1, value=st.session_state.user_profile['age'])
    st.session_state.user_profile['education'] = st.text_input("Highest Education Level", st.session_state.user_profile['education'])
    st.session_state.user_profile['skills'] = st.text_area("Skills (comma-separated)", st.session_state.user_profile['skills'])
    st.session_state.user_profile['interests'] = st.text_area("Interests (comma-separated)", st.session_state.user_profile['interests'])
    st.session_state.user_profile['preferred_industries'] = st.text_area("Preferred Industries (comma-separated)", st.session_state.user_profile['preferred_industries'])

    st.write("Profile details saved in session state. Navigate to the Chat page to use them.")

# Chat Page
elif page == "Chat":
    st.title("Career Guidance Chat")

    example_prompts = [
        "give me a career path tailored for my profile and interests?",
        "give some instructions to make a best resume with resources?",
        "What are some most impotent trends in the current job market?",
        "Can you suggest some common interview questions for sde?"
    ]
    
    def set_query(prompt):
        st.session_state.query = prompt

    # Create a container for horizontal scroll
    scrollable_container = st.container()
    with scrollable_container:
        # Use Streamlit columns for horizontal arrangement
        cols = st.columns(len(example_prompts))
        for i, prompt in enumerate(example_prompts):
            with cols[i]:
                if st.button(prompt, key=f"btn_{i}"):
                    set_query(prompt)

    query = st.text_area("What do you want to know? (e.g., suitable career paths, resume tips, interview questions)", st.session_state.query)
    if st.button("Submit"):
        if not query or query == "": 
            query = st.session_state.query
        if not query:
            st.error("Please enter your query.")
        else:
            # Craft the prompt using the stored user profile
            user_profile = st.session_state.user_profile
            profile_str = (f"Name: {user_profile['name']}, Age: {user_profile['age']}, "
                           f"Education: {user_profile['education']}, Skills: {user_profile['skills']}, "
                           f"Interests: {user_profile['interests']}, Preferred Industries: {user_profile['preferred_industries']}")
            
            full_prompt = f"**Imagine yourself as career consultant, Review profile of job-seeker:**\n{profile_str}\n\n** .Help the user by providing answer to the following query {query.lower()}. Don't answer if above query is not related to career advice or job related, instead say 'It's not related to my expertise' **\n\nResponse:"

            # Get response from Gemini
            response = get_gemini_response(full_prompt)

            # Append the query and response to chat history
            st.session_state.chat_history.append((query, response))

    # Display chat history
    if st.session_state.chat_history:
        st.subheader("Chat")
        for i, (q, r) in enumerate(reversed(st.session_state.chat_history)):
            st.markdown(f"""
                <div style="background-color: #E7D4B5;color: black; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                    <strong><span style="font-size: 2.5rem">👨🏻‍💻 </span></strong><br/> {q}
                </div>
                <div style="background-color: #B6C7AA;color: black; padding: 20px; border-radius: 5px; margin-bottom: 10px;">
                    <strong><span style="font-size: 2.5rem">🤖</span></strong><br/>  {r}
            """, unsafe_allow_html=True)
            st.markdown("---")

# For clearing the chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.session_state.query = ""
    st.experimental_rerun()
