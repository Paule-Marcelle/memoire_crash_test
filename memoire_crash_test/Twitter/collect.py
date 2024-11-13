import tweepy
import pandas as pd
import time

# Remplacez cette valeur par votre Bearer Token Twitter v2
bearer_token = "AAAAAAAAAAAAAAAAAAAAALhDwgEAAAAAPXaZF2r7osdcG20GdtIRp%2BbR6go%3DL3S9X5ig6A5y5lGsv8lQZz6fmw6QODkOVLxs1euqHJRIJYrbsW"

# Configuration de l'authentification avec l'API v2
client = tweepy.Client(bearer_token=bearer_token)

# Liste des mots-clés
keywords = ["domestic violence", "abuse", "toxic relationship","mistreatment", "gaslighting","emotional abuse", "physical abuse"]

# Liste pour stocker les tweets
tweets_data = []

# Parcourir chaque mot-clé et collecter les tweets associés
for keyword in keywords:
    print(f"Collecte des tweets pour le mot-clé : {keyword}")
    query = f"{keyword} lang:en"
    
    try:
        # Rechercher des tweets contenant le mot-clé
        response = client.search_recent_tweets(query=query, max_results=50, tweet_fields=["created_at", "text", "author_id"])
        
        # Extraire les données des tweets
        for tweet in response.data:
            tweets_data.append({
                "created_at": tweet.created_at,
                "author_id": tweet.author_id,
                "text": tweet.text,
                "keyword": keyword
            })
        
        # Pause pour éviter de surcharger l'API (30 secondes de pause)
        time.sleep(30)

    except tweepy.errors.TooManyRequests as e:
        print("Trop de requêtes ! Attente de 15 minutes pour réessayer...")
        time.sleep(15 * 60)  # Attendre 15 minutes avant de réessayer

# Convertir les données en DataFrame et sauvegarder dans un fichier CSV
df = pd.DataFrame(tweets_data)
df.to_csv("tweets_data.csv", index=False)
print("Les tweets ont été sauvegardés dans tweets_data.csv")
