"""
Data Cleaning Module
Retail Analytics & AI-Powered Sales Forecasting System

Developed by Mohammad Dhilawala
"""

import pandas as pd


def load_data(file_path):
    """Load the original retail sales Excel dataset."""
    df = pd.read_excel(file_path, engine="openpyxl")
    return df


def clean_data(df):
    """Clean and validate the retail sales dataset."""

    # Convert date
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Remove unnecessary spaces from text columns
    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove records with invalid dates
    df = df.dropna(subset=["Date"])

    return df


def save_cleaned_data(df, output_path):
    """Save cleaned data as CSV."""
    df.to_csv(output_path, index=False)


if __name__ == "__main__":

    input_file = "../data/4877028-Retail_Sales_Data.xlsx"
    output_file = "../data/cleaned_retail_sales.csv"

    data = load_data(input_file)
    cleaned_data = clean_data(data)

    save_cleaned_data(
        cleaned_data,
        output_file
    )

    print("Data cleaning completed.")
    print(f"Rows: {len(cleaned_data):,}")
    print(f"Columns: {len(cleaned_data.columns)}")