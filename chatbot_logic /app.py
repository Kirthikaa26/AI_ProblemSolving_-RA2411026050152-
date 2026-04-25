import streamlit as st
import re

# Rules
rules = [
    ("hello(X)", "Hello X! How can I help you?"),
    ("order(X)", "Your order for X has been placed."),
    ("bye", "Goodbye!")
]

# Unification function
def unify(pattern, user_input):
    pattern = pattern.replace("(", "\\(").replace(")", "\\)")
    pattern = pattern.replace("X", "(.*)")
    match = re.match(pattern, user_input)
    return match.group(1) if match else None

# Response function
def get_response(user_input):
    for pattern, response in rules:
        value = unify(pattern, user_input)
        if value is not None:
            return pattern, response.replace("X", value)
    return "No match", "Sorry, I didn't understand."

# Streamlit UI
st.title("AI Chatbot Logic Engine")

user_input = st.text_input("Enter your query (e.g., hello(John))")

if st.button("Submit"):
    pattern, response = get_response(user_input)
    
    st.write("**User Input:**", user_input)
    st.write("**Matched Rule:**", pattern)
    st.write("**Response:**", response)
