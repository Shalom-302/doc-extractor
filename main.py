import streamlit as st
import streamlit.components.v1 as components

# Fonction pour créer un bouton personnalisé
def custom_button(label, url):
    button_html = f'''
    <a href="{url}" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; color: #fff; background-color: #007bff; border: none; border-radius: 5px; text-decoration: none;">
        {label}
    </a>
    '''
    st.markdown(button_html, unsafe_allow_html=True)

# Titre de l'application principale
st.title("Bienvenue sur notre Plateforme IA")

# Description
st.write("""
## Votre solution complète pour l'analyse de documents avec l'intelligence artificielle.

Choisissez l'une de nos applications IA ci-dessous pour commencer. Nos outils sont conçus pour vous aider à extraire et à analyser les informations de vos documents de manière rapide et précise.
""")

# Barre de navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choisissez une application", ["Accueil", "CV Analyser", "Carte d'identité Analyser", "Permis de conduire Analyser", "Factures Analyser"])

# Contenu de la page
if page == "Accueil":
    st.header("Bienvenue sur la page d'accueil")
    st.write("""
    ### Notre plateforme offre les applications suivantes :
    - **CV Analyser**: Analysez et extrayez des informations de vos CV.
    - **Carte d'identité Analyser**: Analysez et extrayez des informations de vos Cartes d'identité.
    - **Permis de conduire Analyser**: Analysez et extrayez des informations de vos Permis de conduire.
    - **Factures Analyser**: Analysez et extrayez des informations de vos Factures.
    """)
elif page == "CV Analyser":
    st.header("CV Analyser")
    st.write("Analysez et extrayez des informations de vos CV.")
    custom_button("Accéder à CV Analyser", "https://cv-ai-deepseek.streamlit.app/")
elif page == "Carte d'identité Analyser":
    st.header("Carte d'identité Analyser")
    st.write("Analysez et extrayez des informations de vos Cartes d'identité.")
    custom_button("Accéder à Carte d'identité Analyser", "https://cni-analyser.streamlit.app/")
elif page == "Permis de conduire Analyser":
    st.header("Permis de conduire Analyser")
    st.write("Analysez et extrayez des informations de vos Permis de conduire.")
    custom_button("Accéder à Permis de conduire Analyser", "https://drive-licence-analyzer.streamlit.app/")
elif page == "Factures Analyser":
    st.header("Factures Analyser")
    st.write("Analysez et extrayez des informations de vos Factures.")
    custom_button("Accéder à Factures Analyser", "https://invoice-extraction.streamlit.app/")

# Pied de page
st.sidebar.markdown("---")
st.sidebar.write("© 2025 Kaanari. Tous droits réservés.")