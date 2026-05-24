import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/cleaned_retail.csv")
OUTPUT_PATH = Path("data/processed/featured_retail.csv")

def create_features():
    df = pd.read_csv(INPUT_PATH)

    # Tarih dönüşümü
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Gün bilgileri
    df["Day"] = df["InvoiceDate"].dt.day
    df["WeekDay"] = df["InvoiceDate"].dt.day_name()
    df["Hour"] = df["InvoiceDate"].dt.hour

    # Ortalama sipariş değeri
    customer_avg = (
        df.groupby("CustomerID")["TotalPrice"]
        .mean()
        .reset_index()
    )

    customer_avg.columns = ["CustomerID", "AvgCustomerSpend"]

    df = df.merge(customer_avg, on="CustomerID", how="left")

    print("Feature engineering completed.")
    print(df.head())

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved to: {OUTPUT_PATH}")

    return df

if __name__ == "__main__":
    create_features()