# Streamlit Chatbot Template
# The response is currently a placeholder, just replace it later
import streamlit as st

# Set the page title
st.title("Simple Chatbot")

# This basically just initalizes the chat history in the session state (if it doesn't alr exist)
# Session state persists data across refreshes/reruns of the script
if "messages" not in st.session_state:
    st.session_state.messages = []

# Just displays all previous chat messages 
# (because streamlit refreshes everything, this will keep the chats rendered)
for message in st.session_state.messages:
    # Create a chat message container for each message (message container is just the box with the message)
    with st.chat_message(message["role"]):
        st.write(message["content"])

# This makes an input textbox specifically designed for chatbot UI thingies
user_input = st.chat_input("Type your message here...")

# When user submits a message
if user_input:
    # Adding user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Displaying the message
    with st.chat_message("user"):
        st.write(user_input)
    
    # For now, we just repeat back what the user said (CHANGE THIS WITH AN ACTUAL CHATBOT IF YOU WANT)
    bot_response = f"You said: {user_input}"
    
    # Adding the bot response to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })
    
    # Displaying the "bot" response
    with st.chat_message("assistant"):
        st.write(bot_response)
    
    # Rerunning to update the chat display (basically just refreshing components)
    st.rerun()
