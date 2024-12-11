import snscrape.modules.twitter as sntwitter
import pandas as pd

# Liste pour stocker les tweets
tweets_data = []

# Utiliser snscrape pour collecter les tweets
query = "domestic violence"  # Votre mot-clé de recherche
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} lang:en').get_items()):
    if i > 100:  # Limiter à 100 tweets pour l'exemple
        break
    tweets_data.append({
        "created_at": tweet.date,
        "username": tweet.user.username,
        "text": tweet.content,
        "retweet_count": tweet.retweetCount,
        "like_count": tweet.likeCount
    })

# Convertir en DataFrame et sauvegarder dans un fichier CSV
df = pd.DataFrame(tweets_data)
df.to_csv("tweet_df.csv", index=False)
print("Les tweets ont été sauvegardés dans tweet_df.csv")
