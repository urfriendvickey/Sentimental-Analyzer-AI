import openai
import streamlit as st
from pathlib import Path
import configparser

cfg_reader = configparser.ConfigParser()
fpath = Path.cwd() / Path('config.ini')
cfg_reader.read(str(fpath))
openai.api_key = cfg_reader.get('API_KEY','OPENAI_API_KEY')

def get_response_from_chatgpt(text):
    prompt = f"identify and return the sentiment either positive or negative in given text. text: {text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Text Sentiment Analyzer that returns one-word sentiment."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )
    sentiment = response['choices'][0]['message']['content']
    return sentiment

st.title("Chat GPT Text Sentiment Analyser")
model = 'gpt-3.5-turbo'
text = st.text_input("Enter Text: ", value= "I love to read AI Books.")

if st.button('Submit'):
    with st.spinner('OpenAI in process'): 
        sentiment = get_response_from_chatgpt(text)
        st.success ('OpenAI process is complete')
    
    st.write(f"Sentiment: {sentiment}")
    #Display the sentiment to user 



