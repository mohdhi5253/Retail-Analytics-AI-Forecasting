"""
Sales Forecasting Module

Developed by Mohammad Dhilawala
"""

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def load_sales_data(file_path):
    """Load feature-engineered sales data."""
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def prepare_monthly_sales(df):
    """Convert transaction-level data into monthly sales."""

    monthly_sales = (
        df.groupby(pd.Grouper(key="Date", freq="MS"))["Total_Sales"]
        .sum()
        .reset_index()
    )

    return monthly_sales


def train_forecasting_model(monthly_sales):
    """Train the final exponential smoothing model."""

    model = ExponentialSmoothing(
        monthly_sales["Total_Sales"],
        trend="add",
        seasonal=None,
        damped_trend=True
    ).fit()

    return model


def generate_forecast(model, months=6):
    """Generate future sales forecast."""

    forecast = model.forecast(months)

    return forecast


def create_forecast_table(monthly_sales, forecast):
    """Create a forecast DataFrame."""

    future_dates = pd.date_range(
        start=monthly_sales["Date"].max()
        + pd.offsets.MonthBegin(1),
        periods=len(forecast),
        freq="MS"
    )

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecast_Sales": forecast.values
    })

    return forecast_df


if __name__ == "__main__":

    input_file = "../data/retail_sales_features.csv"

    df = load_sales_data(input_file)

    monthly_sales = prepare_monthly_sales(df)

    model = train_forecasting_model(monthly_sales)

    forecast = generate_forecast(model, months=6)

    forecast_df = create_forecast_table(
        monthly_sales,
        forecast
    )

    forecast_df.to_csv(
        "../data/future_sales_forecast.csv",
        index=False
    )

    print("Forecast generated successfully.")
    print(forecast_df)