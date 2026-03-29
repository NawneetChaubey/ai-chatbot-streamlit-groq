import streamlit as st            # importing the streamlit as a variable st for making apps
from openai import OpenAI         # importing the open ai model
from dotenv import load_dotenv    # importing the .env file
import os                         # importing the operating system for env environment
load_dotenv()                     # loading the env file from dotenv
client = OpenAI(api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",)  # creating a client for the groq model using the api key from the env file
st.title("Question Answer chat bot")  # this is the title of the application
user = st.text_input("Question puchhh mai bataunga")
if st.button("Ask"):
    if user:
         response = client.chat.completions.create(
           model = "openai/gpt-oss-120b",
           messages =[
            {"role":"user","content":user}
        ]
        )
         st.write(response.choices[0].message.content)
    else:
        st.write("pehle kuchh likh bhai")