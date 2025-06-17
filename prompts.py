import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_answer_from_gpt(device_name, question):
    prompt = f"You are a helpful assistant that explains how to use the medical device: {device_name}. Answer this question: {question}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
