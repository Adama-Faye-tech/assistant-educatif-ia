import streamlit as st
import requests
import json
from datetime import datetime
import time

# Configuration de la page
st.set_page_config(
    page_title="Assistant Éducatif IA",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS personnalisés
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .user-message {
        background-color: #f0f2f6;
        border-left-color: #667eea;
    }
    
    .assistant-message {
        background-color: #e8f4fd;
        border-left-color: #00cc88;
    }
    
    .language-selector {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour simuler une réponse de l'IA (remplacez par votre API)
def get_ai_response(question, language, subject=""):
    """
    Fonction pour obtenir une réponse de l'IA
    Dans un vrai projet, remplacez par un appel à votre API (OpenAI, Hugging Face, etc.)
    """
    
    # Dictionnaire des réponses par langue
    responses = {
        "français": {
            "greeting": "Bonjour ! Je suis votre assistant éducatif. Comment puis-je vous aider aujourd'hui ?",
            "math": "Voici une explication en mathématiques : ",
            "science": "Pour les sciences, voici ce que je peux vous expliquer : ",
            "history": "En histoire, voici les informations importantes : ",
            "default": "Merci pour votre question ! Voici ma réponse en français : "
        },
        "wolof": {
            "greeting": "Asalaam aleikum ! Man laa Assistant éducatif. Naka laa mën a dimm ?",
            "math": "Matematik yi, li laa mën a def : ",
            "science": "Ci science yi, li laa mën a kenn : ",
            "history": "Ci histoire yi, li laa war a xam : ",
            "default": "Jerejef ci sa lakk ! Li laa mën a tànk ci wolof : "
        },
        "english": {
            "greeting": "Hello! I'm your educational assistant. How can I help you today?",
            "math": "Here's a mathematics explanation: ",
            "science": "For science, here's what I can explain: ",
            "history": "In history, here are the important facts: ",
            "default": "Thank you for your question! Here's my response in English: "
        }
    }
    
    # Simulation d'un délai de traitement
    time.sleep(1)
    
    # Détection du sujet (simple)
    question_lower = question.lower()
    if any(word in question_lower for word in ["math", "calcul", "nombre", "equation"]):
        subject_key = "math"
    elif any(word in question_lower for word in ["science", "physique", "chimie", "biologie"]):
        subject_key = "science"
    elif any(word in question_lower for word in ["histoire", "history", "guerre", "roi"]):
        subject_key = "history"
    else:
        subject_key = "default"
    
    base_response = responses[language][subject_key]
    
    # Réponse simulée basée sur la question
    if "bonjour" in question_lower or "hello" in question_lower or "salut" in question_lower:
        return responses[language]["greeting"]
    else:
        return base_response + f"Je traite votre question '{question}' en {language}. Cette fonctionnalité sera connectée à un vrai modèle IA."

# Fonction pour détecter la langue (simple)
def detect_language(text):
    """Détection simple de la langue basée sur des mots-clés"""
    text_lower = text.lower()
    
    # Mots-clés français
    french_words = ["bonjour", "merci", "comment", "pourquoi", "que", "qui", "où", "quand"]
    # Mots-clés wolof
    wolof_words = ["naka", "ban", "noo", "nanu", "asalaam", "jerejef", "waaye"]
    # Mots-clés anglais
    english_words = ["hello", "thank", "how", "why", "what", "who", "where", "when"]
    
    french_count = sum(1 for word in french_words if word in text_lower)
    wolof_count = sum(1 for word in wolof_words if word in text_lower)
    english_count = sum(1 for word in english_words if word in text_lower)
    
    if french_count > wolof_count and french_count > english_count:
        return "français"
    elif wolof_count > french_count and wolof_count > english_count:
        return "wolof"
    elif english_count > french_count and english_count > wolof_count:
        return "english"
    else:
        return "français"  # par défaut

# Interface principale
def main():
    # En-tête
    st.markdown("""
    <div class="main-header">
        <h1>🎓 Assistant Éducatif IA Multilingue</h1>
        <p>Votre assistant pour apprendre en Wolof, Français et Anglais</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar pour les paramètres
    with st.sidebar:
        st.header("⚙️ Paramètres")
        
        # Sélection de langue
        st.markdown('<div class="language-selector">', unsafe_allow_html=True)
        st.subheader("🌍 Langue")
        
        language_choice = st.radio(
            "Choisissez votre langue préférée:",
            ["Détection automatique", "Français", "Wolof", "English"],
            index=0
        )
        
        # Matière
        st.subheader("📚 Matière")
        subject = st.selectbox(
            "Matière (optionnel):",
            ["Toutes", "Mathématiques", "Sciences", "Histoire", "Langues", "Autres"]
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Informations
        st.markdown("---")
        st.markdown("""
        ### 📖 Guide d'utilisation
        1. **Posez votre question** dans la zone de chat
        2. **Choisissez votre langue** ou laissez la détection automatique
        3. **Recevez une réponse** adaptée à votre niveau
        
        ### 🌟 Exemples de questions
        - *Français* : "Comment calculer l'aire d'un cercle ?"
        - *Wolof* : "Naka laa mën a xam histoire bu Senegaal ?"
        - *English* : "What is photosynthesis?"
        """)
    
    # Zone de chat principal
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.header("💬 Chat Éducatif")
        
        # Initialisation de l'historique des messages
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Affichage des messages précédents
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Zone de saisie
        if prompt := st.chat_input("Posez votre question éducative..."):
            # Détection de la langue si automatique
            if language_choice == "Détection automatique":
                detected_lang = detect_language(prompt)
                lang_display = {
                    "français": "🇫🇷 Français",
                    "wolof": "🇸🇳 Wolof", 
                    "english": "🇬🇧 English"
                }
                st.info(f"Langue détectée: {lang_display[detected_lang]}")
                selected_language = detected_lang
            else:
                lang_map = {
                    "Français": "français",
                    "Wolof": "wolof",
                    "English": "english"
                }
                selected_language = lang_map[language_choice]
            
            # Ajout du message utilisateur
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Génération de la réponse
            with st.chat_message("assistant"):
                with st.spinner("Génération de la réponse..."):
                    response = get_ai_response(prompt, selected_language, subject)
                    st.markdown(response)
                    
                    # Ajout de la réponse à l'historique
                    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with col2:
        st.header("📊 Statistiques")
        
        # Statistiques simples
        total_messages = len(st.session_state.messages) if "messages" in st.session_state else 0
        user_messages = total_messages // 2
        
        st.metric("Messages échangés", total_messages)
        st.metric("Questions posées", user_messages)
        
        # Bouton pour effacer l'historique
        if st.button("🗑️ Effacer l'historique"):
            st.session_state.messages = []
            st.rerun()
    
    # Pied de page
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🎓 Assistant Éducatif IA Multilingue | Développé avec Streamlit</p>
        <p><em>Prototype MVP - Connectez votre modèle IA préféré</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
