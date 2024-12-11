import tweepy
import pandas as pd

# Votre Bearer Token Twitter v2
bearer_token = "AAAAAAAAAAAAAAAAAAAAALhDwgEAAAAAPXaZF2r7osdcG20GdtIRp%2BbR6go%3DL3S9X5ig6A5y5lGsv8lQZz6fmw6QODkOVLxs1euqHJRIJYrbsW"

# Configuration de l'authentification avec Tweepy et le Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# Test avec un mot-clé populaire
query = "news"  # Vous pouvez changer pour un mot-clé pertinent pour votre recherche
tweets_data = []

# Requête à l'API Twitter
try:
    response = client.search_recent_tweets(query=query, max_results=5)  # Limitez à 5 pour tester
    
    if response.data:
        for tweet in response.data:
            print(tweet.text)  # Affiche chaque tweet récupéré dans la console
            tweets_data.append({
                "created_at": tweet.created_at,
                "author_id": tweet.author_id,
                "text": tweet.text
            })
    else:
        print("Aucun tweet trouvé pour ce mot-clé.")
    
    # Enregistrer dans le CSV uniquement si des tweets ont été récupérés
    if tweets_data:
        df = pd.DataFrame(tweets_data)
        df.to_csv("tweet_df.csv", index=False)
        print("Les tweets ont été sauvegardés dans tweet_df.csv")
    else:
        print("Aucun tweet n'a été sauvegardé car aucune donnée n'a été trouvée.")

except tweepy.errors.TweepyException as e:
    print("Erreur lors de la récupération des tweets :", e)
