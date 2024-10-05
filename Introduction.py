import os
from dotenv import load_dotenv
import streamlit as st
###############################################################
# Obtenir le répertoire du script actuel
current_directory = os.path.dirname(__file__)
# Construire le chemin vers l'icône de manière dynamique à partir du répertoire principal
favicon_path = os.path.join(current_directory, 'static', 'Stats.png')

st.set_page_config(
    page_title="Validate Sample",
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
    # if st.session_state.logged_in:
    #     st.success("✅ Accès accordé ! Vous avez le droit d'utiliser l'application ...")

    # else:
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
                #st.success("✅ Accès accordé ! Vous avez le droit d'utiliser l'application ...")
                st.title("Guide et documentation de l'application 💡")
                st.header('Introduction')
                st.markdown("""
                Bienvenue dans la version limitée de l'application d'analyse statistique pour les dossiers d'assurance de Sanlam. 
                Cet outil est conçu pour évaluer la représentativité des échantillons en fonction de divers critères et tests statistiques. 
                Dans cette version, on se concentre sur le critère ou le test de comparaison de la moyenne ou de la proportion de l'échantillon par rapport à celle hypothétique de la population. 
                Le test Z sera utilisé si les conditions relatives à la taille de l'échantillon requises pour ce test sont remplies ; sinon, le test binomial sera appliqué. 
                Pour réaliser cette analyse, l'échantillon utilisé doit contenir deux variables ou colonnes : la première est une variable d'identification servant à identifier l'observation, et la deuxième est la variable binaire cible qui résume ou regroupe toutes les autres variables.

                Par exemple, si l'on dispose d'un échantillon multivarié ou multidimensionnel et que l'on étudie la catégorisation des dossiers en fonction de la présence ou de l'absence d'anomalies, et si l'on cherche à déterminer si les caractéristiques de cet échantillon peuvent être extrapolées à la population entière, la variable binaire la plus importante, qui résume ou regroupe toutes les autres variables, pourrait être le type de dossier (dossier normal ou dossier suspect contenant des anomalies).
                Dans ce cas, la variable binaire ciblée est le type de dossier. On effectuera donc une analyse unidimensionnelle binaire basée sur cette variable pour vérifier si l'échantillon est un candidat probable à être extrapolé à la population. Si tel est le cas, il faudra confirmer cette extrapolation par une analyse multidimensionnelle couvrant diverses caractéristiques statistiques pertinentes afin d'obtenir des conclusions fiables.
                """)

                st.header('Informations Nécessaires pour l\'Analyse Unidimensionnelle')
                st.markdown("""
                    
                    ➤ Moyenne (ou Proportion) Attendue :
                        
                        ● Il s'agit simplement de la proportion attendue ou hypothétique d'une catégorie spécifique dans la population. 
                        Par exemple, si vous estimez ou supposez que 60 % des dossiers dans la population sont des anomalies, vous devez saisir cette proportion (60 % ou 0,6) dans l'application pour la comparer à celle que vous observez dans votre échantillon.
                    
                    ➤ Seuil de Significativité (α) :
                    
                        ● Le niveau de signification alpha (α) ou l'erreur de Type I est le seuil de risque que vous acceptez pour rejeter à tort l'hypothèse nulle. Autrement dit, c'est le risque de conclure à tort qu'il y a une différence significative entre la moyenne ou la proportion de votre échantillon et celle de la population, alors qu'en réalité, il n'y en a pas. Les niveaux de signification courants sont 1%, 5% ou 10%.        
                        
                        ● Pour le seuil de significativité alpha, il est généralement facultatif dans notre application, mais par défaut, nous utilisons 5%, ce qui est recommandé pour la plupart des analyses statistiques.

                    ➤ Interprétation des Résultats :
                    
                        ● Hypothèse Nulle (H₀) : La moyenne de l'échantillon n'est pas statistiquement différente de celle de la population.

                        ● Hypothèse Alternative (H₁) : La moyenne de l'échantillon est significativement différente de celle de la population.
                        
                        Si la p-value est inférieure ou égale au seuil alpha (α) que vous avez choisi, cela indique une différence statistiquement significative entre la moyenne de l'échantillon et celle de la population.

                    ➤ Les tests utilisés dans cette analyse:
                        
                        ● Pour assurer un résultat plus robuste et statistiquement fiable, le test Z sera utilisé si les conditions relatives à la taille de l'échantillon requises pour ce test sont remplies. Sinon, le test binomial sera appliqué.        
                    
                    ➤ Remarques:

                        ● En cas de résultat négatif (c'est-à-dire lorsque la moyenne de l'échantillon diffère significativement de celle de la population), un processus de sous-échantillonnage sera automatiquement lancé si la taille de l'échantillon est d'au moins 500 observations. Ce processus consistera à extraire aléatoirement 20 % de l'échantillon pour créer un sous-échantillon et le tester. Si le test (z-test ou test binomial) du sous-échantillon donne un résultat positif (c'est-à-dire que nous ne pouvons pas rejeter l'hypothèse nulle), un bouton permettant de télécharger ce sous-échantillon sera affiché, et un message sera également affiché recommandant d'utiliser une analyse multidimensionnelle pour vérifier ou valider, si les caractéristiques du sous-échantillon (par exemple la moyenne) peuvent être extrapolées à la population.
                        En revanche, si le test est négatif, nous passerons au deuxième sous-échantillon, et ce jusqu'à un maximum de 100 itérations. La sélection de 500 comme seuil pour la taille de l'échantillon n'est pas arbitraire ; elle permet de garantir une probabilité équitable pour les proportions ou les moyennes des sous-échantillons. Avec ce seuil, nous assurons la possibilité de couvrir toutes les proportions de 0 % à 100 %, ce qui augmente la probabilité d'obtenir des résultats positifs dans la comparaison de la moyenne du sous-échantillon avec celle de la population.
                        
                        ● Si le résultat de l'analyse est positif (c'est-à-dire que nous ne pouvons pas rejeter l'hypothèse nulle), l'échantillon ou le sous-échantillon est considéré comme un candidat probable pour être extrapolé à la population. Un message automatique s'affichera pour vous recommander de réaliser une analyse multidimensionnelle. 
                        Cette analyse comprendra des tests avancés tels que Kruskal-Wallis, le test du chi-deux, etc., afin d'examiner d'autres caractéristiques de l'échantillon et de les comparer à celles de la population. La conclusion finale de l'analyse multidimensionnelle, basée sur la comparaison des résultats des tests avec les hypothèses fournies en s'appuyant sur l'expertise métier en assurance, déterminera si l'échantillon ou le sous-échantillon peut être extrapolé à la population. Si les résultats montrent une conformité acceptable selon les seuils définis en relation avec le métier, alors l'échantillon ou le sous-échantillon pourra être considéré comme représentatif de la population. Sinon, il ne pourra pas être extrapolé à la population.
                        
                """)

                st.header('Conseils pour éviter le déclenchement des erreurs dans l\'application')
                st.markdown("""
                    ● Avant de cliquer sur le bouton "Analyser", assurez-vous que la moyenne attendue (ou la proportion) de la population a été saisie.

                    ● Après avoir téléversé les données de l'échantillon et saisi la moyenne ou la proportion hypothétique de la population, veuillez choisir la catégorie que vous souhaitez analyser (la catégorie représentant une valeur de 1 ou un cas de succès, par exemple, la catégorie "vrai", "anomalie" ou "1"). Ensuite, cliquez sur le bouton "Analyser" pour compléter l'analyse.
                    """)

                st.header('Conclusion')
                st.markdown("""
                    ● Le test statistique utilisé dans l'analyse (Ztest ou test binomial) nécessite la moyenne hypothétique ou la moyenne réelle de la population. Bien que cela puisse être considéré comme une limitation, il est important de noter que, dans le contexte de l'échantillonnage, l'accès à cette information ainsi qu'à d'autres informations pertinentes sur la population est essentiel. Ces données peuvent être fournies par la pratique ou l'expertise métier.         
                    
                    ● La version complète de l'application, incluant l'analyse multidimensionnelle, sera communiquée après que les utilisateurs potentiels, tels que les gestionnaires en assurance, seront à l'aise avec cette version limitée et se seront familiarisés avec ses fonctionnalités.    
                    """)

            else:
                if st.session_state.tries<5:
                    st.warning("⚠️ Clé invalide. Veuillez réessayer.")
                    st.session_state.tries+=1
                else:
                    st.error("Trop de tentatives d'accès. Veuillez contacter : [khalil.blm2000@gmail.com].")
                    

# Exécuter la fonction d'accès pour afficher le formulaire de validation d'accès
login_modal()


