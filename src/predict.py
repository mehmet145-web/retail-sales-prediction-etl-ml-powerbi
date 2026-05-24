import pandas as pd
from pathlib import Path
import joblib

DATA_PATH = Path("data/processed/featured_retail.csv")
MODEL_PATH = Path("models/sales_model.pkl")
OUTPUT_PATH = Path("data/processed/predictions.csv")

def make_predictions():
    # Veri
    df = pd.read_csv(DATA_PATH)

    # Sample küçült
    df = df.sample(n=10000, random_state=42)

    # Model yükle
    model = joblib.load(MODEL_PATH)

    # Feature'lar
    features = [
        "Quantity",
        "UnitPrice",
        "Month",
        "Day",
        "Hour",
        "AvgCustomerSpend"
    ]

    # Tahmin
    df["PredictedSales"] = model.predict(df[features])
    
    df["PredictedSales"] = df["PredictedSales"].astype(float).round(2)
    df["TotalPrice"] = df["TotalPrice"].astype(float).round(2)

    # Kaydet
    df.to_csv(OUTPUT_PATH, index=False)

    print("Predictions completed.")
    print(f"Saved to: {OUTPUT_PATH}")

    print(df[["TotalPrice", "PredictedSales"]].head())

if __name__ == "__main__":
    make_predictions()