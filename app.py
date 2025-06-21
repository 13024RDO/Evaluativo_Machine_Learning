
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("modelo_reposteria.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]  
    return jsonify({"prediccion_unidades_vendidas": round(prediction)})

@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify({
        "modelo": "Regresión Lineal",
        "r2_score": 0.82,  
        "rmse": 3.31        
    })

if __name__ == "__main__":
    app.run(debug=True)
