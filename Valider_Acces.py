import os
from dotenv import load_dotenv
import streamlit as st
###############################################################
# Obtenir le répertoire du script actuel
current_directory = os.path.dirname(__file__)
# Construire le chemin vers l'icône de manière dynamique à partir du répertoire principal
favicon_path = os.path.join(current_directory, 'static', 'Stats.png')

st.set_page_config(
    page_title="Validate Access",
    page_icon=favicon_path,  
)
################################################################
# Initialiser l'état de la session pour le statut d'accès et le nombre de tentatives d'accès
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'tries' not in st.session_state:
    st.session_state.tries =0

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la variable locale
key = os.getenv('access_key', 'default_value')

# Fonction pour valider la clé d'entrée de l'utilisateur
def validate_key(input_key):
    return input_key == key

# Fonction  pour gérer le statut d'accès

def login_modal():
    if st.session_state.logged_in:
        st.success("✅ Accès accordé ! Vous avez le droit d'utiliser l'application ...")

    else:
      if st.session_state.tries>=5:
        st.warning("Trop de tentatives d'accès. Veuillez contacter : [khalil.blm2000@gmail.com].")
        st.stop()
      else:
        st.title("Valider l'accès à l'application")
        user_input = st.text_input("Entrez la clé secrète (email address):")
        submit_button = st.button("Valider")
        
        if submit_button:
            if validate_key(user_input):
                st.session_state.logged_in = True
                st.success("✅ Accès accordé ! Vous avez le droit d'utiliser l'application ...")
            else:
                if st.session_state.tries<5:
                    st.warning("⚠️ Clé invalide. Veuillez réessayer.")
                    st.session_state.tries+=1
                else:
                    st.error("Trop de tentatives d'accès. Veuillez contacter : [khalil.blm2000@gmail.com].")
                    

# Exécuter la fonction d'accès pour afficher le formulaire de validation d'accès
login_modal()


