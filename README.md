### Déploiement sur votre PC local

    0- Installer Docker : Assurez-vous que Docker est installé sur votre pc.
    1- Vérifiez que le dossier du projet se trouve sur votre PC, puis accédez-y via le terminal. 
    2- Construire l'image Docker par l'exécution la commande bash suivante:
    docker build -t statsapp:initial .

    # Note : statsapp est le nom de l'image Docker. Vous pouvez choisir un autre nom si vous le souhaitez.
    3- Exécuter le conteneur Docker par la commande bash suivante :
    docker run -d -p 8601:8601 statsapp:initial

    4- Accéder à l'application : Vous pouvez maintenant accéder à l'application via votre navigateur à l'adresse suivante :
        http://0.0.0.0:8601
        http://localhost:8601

### Déploiement sur un serveur

    0- Accéder au serveur : Connectez-vous au serveur où vous souhaitez déployer l'application.
    1- Installer Docker : Assurez-vous que Docker est installé sur le serveur.
    2- Transférer ou cloner le projet : Vous pouvez transférer le dossier du projet vers le serveur en utilisant scp ou rsync, ou le cloner directement depuis Git après avoir créé un dépôt et chargé le dossier du projet sur votre compte GitHub personnel ou d'entreprise. 
    3- Accéder à le dossier transféré et construire l'image Docker par l'exécution la commande bash suivante:
    docker build -t statsapp:initial .

    Note : statsapp est le nom de l'image Docker. Vous pouvez choisir un autre nom si vous le souhaitez.
    4- Exécuter le conteneur Docker par la commande bash suivante :
    docker run -d -p 8601:8601 statsapp:initial

    5- Accéder à l'application : Vous pouvez maintenant accéder à l'application via le navigateur en utilisant l'adresse IP du serveur et le port spécifié (8601), par exemple : http://<adresse-ip_de_votre_serveur>:8601
