"""
data_cleaning.py

This script loads a messy sales dataset and applies several cleaning steps. This shows Python data cleaning and 
usage of GitHub Copilot. 
It shows Python data cleaning and Copilot usage.
"""
import pandas as pd 

# Function: Load_data
# This function should open the raw CSV file and return a DataFrame. 
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    print("Columns detected in file:", df.columns.tolist())
    return df

# Function: Standardize column names 
# This function should clean the data by removing leading/trailing spaces, converting to lowercase, and replacing spaces with underscores.
def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )
    return df

#Convert text fields to strings and fix extra spaxes from string columns 
def clean_text_fields(df: pd.DataFrame) -> pd.DataFrame:
    if "prodname" in df.columns:
        df["prodname"] = df["prodname"].astype(str).str.strip()
    if "category" in df.columns:
        df["category"] = df["category"].astype(str).str.strip()
    return df

#Handle missing values 
#Drop rows with missing values 
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["price", "qty"])
    return df

# Remove rows with negative values
# Make negative values invalid 
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df

if __name__ == "__main__":
    # Load raw data, and define paths 
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    print("Columns in CSV:", df_raw.columns.tolist())
    print("Data Loaded Successfully")

    df_clean = standardize_column_names(df_raw)
    df_clean = clean_text_fields(df_clean)

    df_clean["price"] = pd.to_numeric(df_clean["price"], errors="coerce")
    df_clean["qty"] = pd.to_numeric(df_clean["qty"], errors="coerce")

    print("Data types after numeric conversion:\n", df_clean.dtypes)

    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)
    
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
    
    