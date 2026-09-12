# Retail Analytics & AI-Powered Sales Forecasting System

## 👨‍💻 Developed By

**Mohammad Dhilawala**

Academic Major Project

---

## 📌 Project Overview

The Retail Analytics & AI-Powered Sales Forecasting System is an interactive data analytics and machine learning application designed to analyze retail sales performance and support business decision-making.

The system transforms retail transaction data into meaningful business insights using data cleaning, exploratory data analysis, time-series forecasting, store segmentation, and an interactive Streamlit dashboard.

---

## 🌐 Live Project:
[https://lnkd.in/dBTCgMzd](https://retail-analytics-ai-forecasting.streamlit.app/)

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze retail sales performance.
- Identify sales trends and patterns.
- Compare product categories and regions.
- Analyze store-level performance.
- Study customer and payment behavior.
- Forecast future sales using time-series forecasting.
- Segment stores using K-Means clustering.
- Detect unusual sales periods.
- Generate automated business insights.
- Present results through an interactive dashboard.

---

## 📊 Dataset

The project uses a retail sales dataset containing approximately **73,000 transaction records** covering:

**January 2023 to December 2024**

The dataset contains information about:

- Date
- Store
- Store Location
- Product
- Product Category
- Product Subcategory
- Brand
- Unit Price
- Units Sold
- Total Sales
- Discount
- Revenue
- Customer Type
- Payment Mode
- Promotion
- Stock
- Store Rating
- Region
- Holiday Flag

---

## 🧹 Data Processing

The data processing pipeline includes:

1. Loading the original Excel dataset.
2. Converting dates into proper datetime format.
3. Removing duplicate records.
4. Cleaning text fields.
5. Validating numerical values.
6. Checking missing values.
7. Creating time-based features.
8. Saving the cleaned dataset.

---

## 📈 Exploratory Data Analysis

The project analyzes:

- Monthly sales trends
- Yearly sales
- Product category performance
- Regional performance
- Store performance
- Customer type
- Payment methods
- Brand performance
- Promotions
- Holiday vs non-holiday sales
- Discounts
- Stock levels
- Store ratings
- Correlations between numerical variables

---

## 🔮 Sales Forecasting

The forecasting module uses **Exponential Smoothing with a damped trend** to estimate future sales.

The project evaluates forecasting approaches including:

- Baseline Forecast
- Moving Average
- Linear Regression
- Exponential Smoothing

The final model is trained using the historical monthly sales data and produces a **6-month future sales forecast**.

The forecast is stored in:

`data/future_sales_forecast.csv`

---

## 🧩 Store Segmentation

K-Means clustering is used to group stores according to their performance characteristics.

The segmentation identifies:

- High Value Stores
- High Volume Stores
- Lower Performance Stores

The segmentation output is stored in:

`data/store_segmentation.csv`

---

## 🤖 AI-Powered Business Intelligence

The dashboard generates automated business observations such as:

- Leading product category
- Highest-performing region
- Top-performing store
- Customer revenue contribution
- Unusual sales periods
- Management recommendations

These insights help convert analytical results into practical business decisions.

---

## 🖥️ Interactive Dashboard

The dashboard is developed using **Python and Streamlit**.

### Dashboard sections

- 🎯 Executive Overview
- 📊 Sales Intelligence
- 🔮 Forecast Lab
- 🏪 Store Intelligence
- 🤖 AI Insights

### Dashboard features

- Interactive date filtering
- Region filtering
- Store filtering
- Product category filtering
- KPI cards
- Interactive charts
- Forecast visualization
- Store segmentation
- Anomaly detection
- Business recommendations
- Forecast download

---

## 🛠️ Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Plotly
- Streamlit

### Machine Learning

- Scikit-learn
- K-Means Clustering

### Forecasting

- Statsmodels
- Exponential Smoothing

### Data Storage

- Excel
- CSV

### Development Environment

- Visual Studio Code
- Jupyter Notebook
- Python Virtual Environment

---

## 📁 Project Structure

```text
Retail-Analytics-AI-Forecasting
│
├── data/
├── models/
├── notebooks/
├── src/
├── dashboard/
├── outputs/
├── README.md
└── requirements.txt
