# import streamlit as st

# with st.chat_message('user'):
#     st.text('Hi')

# with st.chat_message('assistant'):
#     st.text('How can I help you?')

# with st.chat_message('user'):
#     st.text('My name is shivam.')


# user_input  = st.chat_input(placeholder='type here...')

# if user_input:
#     with st.chat_message('user'):
#         st.text(user_input)

#-------------------------------------------
# import streamlit as st

# message_history = []

# # loading the conversation history
# for message in message_history:
#     with st.chat_message(message['role']):
#         st.text(message['content'])

# user_input = st.chat_input(placeholder="type here...")

# if user_input:
#     #first add the message to message history
#     message_history.append({'role':'user','content':user_input})
#     with st.chat_message('user'):
#         st.text(user_input)

#     #add the message to the message_history
#     message_history.append({'role':'assistant','content':user_input})
#     with st.chat_message('assistant'):
#         st.text(user_input)

#-----------------------------------------------------
# import streamlit as st


# if 'message_history' not in st.session_state:
#     st.session_state['message_history'] = []

# for message in st.session_state['message_history']:
#     with st.chat_message(message['role']):
#         st.text(message['content'])

# user_input = st.chat_input(placeholder='type here...')

# if user_input:
#     st.session_state['message_history'].append({'role':'user','content':user_input})
#     with st.chat_message('user'):
#         st.text(user_input)

#     st.session_state['message_history'].append({'role':'assistant','content':user_input})
#     with st.chat_message('assistant'):
#         st.text(user_input)

#-----------------------------------------

# import streamlit as st

# # st.session_state:
# # Streamlit reruns the entire script whenever user interacts with UI.
# # session_state helps preserve variables/data across reruns.

# # Check whether 'message_history' exists in session_state
# # If not present, initialize it as an empty list
# if 'message_history' not in st.session_state:
#     st.session_state['message_history'] = []

# # Iterate through all stored messages
# # This helps display old chat history after every rerun
# for message in st.session_state['message_history']:

#     # st.chat_message():
#     # Creates a chat bubble UI similar to ChatGPT.
#     # Role determines alignment/style ('user' or 'assistant').

#     with st.chat_message(message['role']):

#         # st.text():
#         # Displays plain text exactly as provided.
#         # Does not support markdown formatting.

#         st.text(message['content'])

# # st.chat_input():
# # Creates an input box fixed at the bottom of chat UI.
# # Returns user-entered text when submitted.

# user_input = st.chat_input(placeholder='type here...')

# # Execute only when user enters a message
# if user_input:

#     # append():
#     # Adds new dictionary/message to message_history list.
#     # Used to persist chat conversation.

#     # Store user message in session_state
#     st.session_state['message_history'].append({'role':'user','content':user_input})

#     # Display user message in chat UI
#     with st.chat_message('user'):
#         st.text(user_input)

#     # Currently assistant simply echoes user message
#     # Store assistant response in session_state
#     st.session_state['message_history'].append({'role':'assistant','content':user_input})

#     # Display assistant response in UI
#     with st.chat_message('assistant'):
#         st.text(user_input)

#-----------------------------------------------------------
# import streamlit as st
# from langgraph_backend import chatbot
# from langchain_core.messages import HumanMessage

# CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# if 'message_history' not in st.session_state:
#     st.session_state['message_history'] = []

# for message in st.session_state['message_history']:
#     with st.chat_message(message['role']):
#         st.text(message['content'])

# user_input = st.chat_input(placeholder='type here...')

# if user_input:
#     st.session_state['message_history'].append({'role':'user','content':user_input})
#     with st.chat_message('user'):
#         st.text(user_input)

#     response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    
#     ai_message = response['messages'][-1].content
#     # first add the message to message_history
#     st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
#     with st.chat_message('assistant'):
#         st.text(ai_message)

#------------------------------------------------------
import streamlit as st

# Import chatbot object from backend file
# chatbot here is your compiled LangGraph application
from langgraph_backend import chatbot

# HumanMessage is used to send user input to LLM in LangChain format
from langchain_core.messages import HumanMessage


# CONFIG:
# Used to pass runtime configuration to LangGraph.
# thread_id helps maintain memory/conversation persistence.

CONFIG = {
    'configurable': {
        'thread_id': 'thread-1'
    }
}


# st.session_state:
# Stores variables across Streamlit reruns.
# Without this, chat history disappears after every interaction.

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# Display all previous chat messages stored in session_state
# This recreates the full chat UI after every rerun.

for message in st.session_state['message_history']:

    # st.chat_message():
    # Creates chat bubble container.
    # Role determines whether message appears as user or assistant.

    with st.chat_message(message['role']):

        # st.text():
        # Displays plain text exactly as it is.
        # Does not render markdown formatting.

        st.text(message['content'])


# st.chat_input():
# Creates chat textbox at bottom of screen.
# Returns entered text when user submits message.

user_input = st.chat_input(placeholder='type here...')


# Runs only when user submits input
if user_input:

    # Store user message in session_state history
    # append() adds new item to list

    st.session_state['message_history'].append({
        'role':'user',
        'content':user_input
    })

    # Display user message immediately in UI
    with st.chat_message('user'):
        st.text(user_input)


    # chatbot.invoke():
    # Sends current message to LangGraph chatbot.
    # config contains thread_id for memory persistence.

    response = chatbot.invoke(
        {
            'messages': [
                HumanMessage(content=user_input)
            ]
        },
        config=CONFIG
    )


    # Extract final AI response from message list
    # response['messages'] returns complete conversation messages

    ai_message = response['messages'][-1].content


    # Store assistant response in session history
    # So it persists across reruns

    st.session_state['message_history'].append({
        'role': 'assistant',
        'content': ai_message
    })


    # Display assistant response in chat UI
    with st.chat_message('assistant'):
        st.text(ai_message)
