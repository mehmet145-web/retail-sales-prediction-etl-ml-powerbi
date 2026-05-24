import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/online_retail.xlsx.csv")
PROCESSED_DATA_PATH = Path("data/processed/cleaned_retail.csv")

def transform_data():
    # Veriyi oku
    df = pd.read_csv(RAW_DATA_PATH, encoding="ISO-8859-1")

    print("Original Shape:", df.shape)

    # Eksik değerleri temizle
    df = df.dropna(subset=["CustomerID", "Description"])

    # Negatif quantity kaldır
    df = df[df["Quantity"] > 0]

    # Negatif fiyat kaldır
    df = df[df["UnitPrice"] > 0]

    # Duplicate kaldır
    df = df.drop_duplicates()

    # Tarih formatı
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Yeni kolon
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # Yıl / Ay
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month

    print("Cleaned Shape:", df.shape)

    # Kaydet
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print("Transformation completed.")
    print(f"Saved to: {PROCESSED_DATA_PATH}")

    return df

if __name__ == "__main__":
    transform_data()