import streamlit as st            # importing the streamlit as a variable st for making apps
from openai import OpenAI         # importing the open ai model
from dotenv import load_dotenv    # importing the .env file
import os                         # importing the operating system for env environment
load_dotenv()                     # loading the env file from dotenv



client = OpenAI(api_key=st.secrets["GROQ_API_KEY"],
   base_url="https://api.groq.com/openai/v1",)  # creating a client for the groq model using the api key from the env file
st.title("Question Answer chat bot")  # this is the title of the application
user = st.text_input("Question puchhh mai bataunga")

# creating the memory so that ai can remeber the messages

if "messages" not in st.session_state:
    st.session_state.messages =[{
        "role":"system",
        "content":"You are a helpful AI Assistant"
    }]

# this will show the chat history 
for msg in st.session_state.messages:
    st.write(f"{msg["role"]}:{msg["content"]}")


# this is for creating the ask button
if st.button("Ask"):
    if user:
         # saving the user messages
         st.session_state.messages.append({
             "role":"user",
             "content":user
         })


         # sending the history to the API
         response = client.chat.completions.create(
           model = "openai/gpt-oss-120b",
           messages =st.session_state.messages
        )
         
         ai_reply = response.choices[0].message.content
        # saving the ai reply
         st.session_state.messages.append({
             "role":"assistant",
             "content":ai_reply
         })
         st.write(ai_reply)
    else:
        st.write("pehle kuchh likh bhai")

if st.button("clear chat"):
    st.session_state.messages =[]
