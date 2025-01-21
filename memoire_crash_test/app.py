from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Charger le modèle sauvegardé
model = joblib.load("rf_model.pkl")

# Charger le tokenizer (si utilisé dans ton pipeline)
# import pickle
# with open("tokenizer.pkl", "rb") as handle:
#     tokenizer = pickle.load(handle)

# Initialiser FastAPI
app = FastAPI()

# Définir une classe pour les données d'entrée
class PredictionInput(BaseModel):
    text: str  # Le texte à analyser

# Endpoint principal pour les prédictions
@app.post("/predict/")
def predict(balanced_df: PredictionInput):
    # Prétraiter le texte (si nécessaire, comme la tokenisation ou le padding)
    # Exemple : vectoriser avec un TF-IDF ou tokenizer
    # processed_text = tokenizer.transform([data.text])

    # Convertir le texte en un format adapté au modèle
    # Remplacer 'processed_text' par les caractéristiques attendues
    features = np.array([len(balanced_df.text)])  # Exemple simple : longueur du texte

    # Faire une prédiction
    prediction = model_rf.predict(features.reshape(1, -1))[0]
    prediction_label = "Potential Danger" if prediction == 1 else "No Danger"

    # Retourner la réponse
    return {"text": data.text, "prediction": prediction_label}
