# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt et installer les dépendances Python
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port que l'application utilise
EXPOSE 5000

# Définir la commande pour exécuter l'application
CMD ["python", "app.py"]

