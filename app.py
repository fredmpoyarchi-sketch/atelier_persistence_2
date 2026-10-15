from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/api/v1/stats/produits", methods=["GET"])
def analyser_produits():
    # Source de données publique en ligne (JSON)
    url = "https://dummyjson.com/products"
   
    # 1. Extraction : Lecture directe du flux JSON distant
    donnees = pd.read_json(url)
   
    # 2. Transformation : Extraction de la liste 'products' en DataFrame
    df = pd.DataFrame(list(donnees["products"]))
   
    # 3. Manipulation d'une Series : Sélection de la colonne 'price'
    series_prix = df["price"]
   
    # 4. Analyse statistique descriptive
    stats = series_prix.describe().to_dict()
   
    # 5. Réponse RESTful
    return jsonify({
        "total_produits": int(stats["count"]),
        "prix_moyen": round(stats["mean"], 2),
        "prix_min": stats["min"],
        "prix_max": stats["max"],
        "apercu_colonnes": list(df.columns)
    }), 200
