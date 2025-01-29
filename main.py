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
st.title("Welcome to Our AI Platform")

# Description
st.write("""
## Your complete solution for document analysis with artificial intelligence.

Choose one of our AI applications below to get started. Our tools are designed to help you extract and analyze information from your documents quickly and accurately.
""")

# Barre de navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose an application", ["Home", "Resume Analyzer", "ID Card Analyzer", "Driver's License Analyzer", "Invoice Analyzer"])

# Contenu de la page
if page == "Home":
    st.header("Welcome to the Home Page")
    st.write("""
    ### Our platform offers the following applications:
    - **Resume Analyzer**: Analyze and extract information from your resumes.
    - **ID Card Analyzer**: Analyze and extract information from your ID cards.
    - **Driver's License Analyzer**: Analyze and extract information from your driver's licenses.
    - **Invoice Analyzer**: Analyze and extract information from your invoices.
    """)
elif page == "Resume Analyzer":
    st.header("Resume Analyzer")
    st.write("Analyze and extract information from your resumes.")
    custom_button("Access Resume Analyzer", "https://cv-ai-deepseek.streamlit.app/")
elif page == "ID Card Analyzer":
    st.header("ID Card Analyzer")
    st.write("Analyze and extract information from your ID cards.")
    custom_button("Access ID Card Analyzer", "https://cni-analyser.streamlit.app/")
elif page == "Driver's License Analyzer":
    st.header("Driver's License Analyzer")
    st.write("Analyze and extract information from your driver's licenses.")
    custom_button("Access Driver's License Analyzer", "https://drive-licence-analyzer.streamlit.app/")
elif page == "Invoice Analyzer":
    st.header("Invoice Analyzer")
    st.write("Analyze and extract information from your invoices.")
    custom_button("Access Invoice Analyzer", "https://invoice-extraction.streamlit.app/")

# Pied de page
st.sidebar.markdown("---")
st.sidebar.write("© 2025 Kaanari. All rights reserved.")