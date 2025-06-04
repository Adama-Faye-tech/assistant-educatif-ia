import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Assistant Éducatif IA Multilingue")

ta_question = st.text_input("Pose ta question")

if ta_question:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": ta_question}]
    )
    answer = response.choices[0].message.content
    st.write(answer)