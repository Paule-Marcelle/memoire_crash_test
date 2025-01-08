import praw
import pandas as pd
import time

# Configurer la connexion à Reddit avec vos identifiants
reddit = praw.Reddit(
    client_id="fdvtXXfxnHeESWoZXxzOcg",
    client_secret="2X0nscpj9tbPm3voYqNTAdciWfnFtg",
    user_agent="data_collection_project"
)

# Définir les mots-clés et subreddits
keywords = ["happy relationship", "healthy relationship", "positive vibes", "gratitude",
    "self-care", "personal growth", "relationship success", "love and support"]
subreddits = ["happy", "relationships", "selfimprovement", "KindVoice", "Marriage", "UpliftingNews", "CasualConversation"]
posts = []  # Liste pour stocker les résultats

# Boucle pour parcourir chaque subreddit et mot-clé
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    for keyword in keywords:
        print(f"Récupération des posts dans {subreddit_name} pour le mot-clé : {keyword}")
        # Rechercher des posts contenant le mot-clé
        # for submission in subreddit.search(keyword, limit=100):
        for submission in subreddit.hot(limit=100):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "created_utc": submission.created_utc,
                "author": submission.author.name if submission.author else "N/A",
                "subreddit": submission.subreddit.display_name
            })
        time.sleep(1)  # Pause d'une seconde pour éviter de surcharger l'API

# Convertir les données en DataFrame et les sauvegarder dans un CSV
df = pd.DataFrame(posts)
if not df.empty:
    df.to_csv("reddit_good.csv", index=False)
    print("Les données ont été sauvegardées dans reddit_posts.csv")
else:
    print("Aucun post trouvé avec les paramètres donnés.")
