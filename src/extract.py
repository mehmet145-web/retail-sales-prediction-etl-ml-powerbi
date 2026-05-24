import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/online_retail.xlsx.csv")

def extract_data():
    df = pd.read_csv(RAW_DATA_PATH, encoding="ISO-8859-1")

    print("Extract completed")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(df.head())

    return df

if __name__ == "__main__":
    extract_data()