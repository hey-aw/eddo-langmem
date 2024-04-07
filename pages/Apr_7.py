import streamlit as st

# Define initial messages
messages = [
    {"role": "ai", "content": "Welcome back to your Reflection Journal!"},
    {
        "role": "ai",
        "content": "Let's start by revisiting your science lesson today. Do you remember the videos we watched of objects in collisions?",
    },
    {
        "role": "human",
        "content": "Yes! The slow-motion stuff was crazy, especially the golf ball and the glass shattering.",
    },
    {"role": "ai", "content": "What was the most surprising thing you observed?"},
    {
        "role": "human",
        "content": "Definitely the laser making the glass bend. I didn't think something so hard could change shape like that, even a tiny bit.",
    },
]

# Chat area
st.title("Reflection Journal")

# Display the initial messages
for message in messages:
    if message["role"] == "ai":
        st.chat_message(name="Eddo", avatar="🦔").write(message["content"])
    else:
        st.chat_message(name="Emily", avatar="🦄").write(message["content"])

# User input
user_input = st.chat_input("Your Response", key="input")

if user_input:
    st.chat_message

    # Placeholder for fetching an AI response
    ai_response = (
        "That's an interesting observation! Would you like to explore that idea more?"
    )
    st.chat_message(ai_response)
