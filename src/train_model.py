import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

DATA_PATH = Path("data/processed/featured_retail.csv")
MODEL_PATH = Path("models/sales_model.pkl")

def train_model():
    # Veriyi oku
    df = pd.read_csv(DATA_PATH)
    df = df.sample(n=50000, random_state=42)

    # Kullanılacak feature'lar
    features = [
        "Quantity",
        "UnitPrice",
        "Month",
        "Day",
        "Hour",
        "AvgCustomerSpend"
    ]

    # Hedef değişken
    target = "TotalPrice"

    X = df[features]
    y = df[target]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestRegressor(
        n_estimators=30,
        random_state=42,
        n_jobs=-1
    )

    # Eğit
    model.fit(X_train, y_train)

    # Tahmin
    predictions = model.predict(X_test)

    # Hata metriği
    mae = mean_absolute_error(y_test, predictions)

    print(f"Model trained successfully.")
    print(f"Mean Absolute Error: {mae:.2f}")

    # Kaydet
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train_model()