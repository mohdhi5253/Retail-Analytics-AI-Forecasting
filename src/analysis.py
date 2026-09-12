"""
Retail Sales Analysis Module

Developed by Mohammad Dhilawala
"""

import pandas as pd


def load_features(file_path):
    """Load feature-engineered retail data."""
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def sales_by_category(df):
    """Calculate sales by product category."""
    return (
        df.groupby("Product_Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def sales_by_region(df):
    """Calculate sales by region."""
    return (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def sales_by_store(df):
    """Calculate sales by store."""
    return (
        df.groupby("Store_ID")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def monthly_sales(df):
    """Calculate monthly sales."""
    return (
        df.set_index("Date")
        .resample("MS")["Total_Sales"]
        .sum()
        .reset_index()
    )


def calculate_kpis(df):
    """Calculate important business KPIs."""

    total_sales = df["Total_Sales"].sum()
    total_units = df["Units_Sold"].sum()
    average_unit_price = df["Unit_Price"].mean()
    average_discount = df["Discount_Percentage"].mean()
    average_rating = df["Store_Rating"].mean()

    return {
        "total_sales": total_sales,
        "total_units": total_units,
        "average_unit_price": average_unit_price,
        "average_discount": average_discount,
        "average_rating": average_rating,
    }


if __name__ == "__main__":

    file_path = "../data/retail_sales_features.csv"

    df = load_features(file_path)

    print("===== RETAIL SALES ANALYSIS =====")
    print()

    kpis = calculate_kpis(df)

    for key, value in kpis.items():
        print(f"{key}: {value:,.2f}")

    print("\nTop Categories:")
    print(sales_by_category(df).head())

    print("\nTop Regions:")
    print(sales_by_region(df))

    print("\nTop Stores:")
    print(sales_by_store(df).head())