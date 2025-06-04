import streamlit as st
import openai

# Configure ta clé API OpenAI ici ou via Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Assistant Éducatif IA Multilingue")
st.write("Pose ta question en Wolof, Français ou Anglais")

# Entrée utilisateur
user_input = st.text_input("Ta question :")

# Choix de la langue
langue = st.selectbox("Choisis ta langue", ["Français", "Anglais", "Wolof"])

# Prépare le prompt selon la langue
def get_prompt(input_text, langue):
    if langue == "Français":
        return f"Réponds clairement à cette question : {input_text}"
    elif langue == "Anglais":
        return f"Answer this educational question clearly: {input_text}"
    elif langue == "Wolof":
        return f"Waññi ci wolof ci kaw laaj bii: {input_text}"
    else:
        return input_text

# Génère la réponse IA
if st.button("Envoyer") and user_input:
    prompt = get_prompt(user_input, langue)
    with st.spinner("L'IA réfléchit..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
            st.success("Réponse :")
            st.write(answer)
        except Exception as e:
            st.error(f"Erreur : {e}")