# ============================================================
# RETAIL INTELLIGENCE COMMAND CENTER
# Retail Analytics & AI-Powered Sales Forecasting System
# Developed by Mohammad Dhilawala
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from textwrap import dedent

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Retail Intelligence Command Center",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# COLOR PALETTE

# Plotly visual theme
PLOTLY_TEMPLATE = "plotly_dark"

# ============================================================

NAVY = "#07111F"
NAVY_2 = "#0B1728"
CARD = "#101F33"
CARD_2 = "#14263D"

CYAN = "#38BDF8"
BLUE = "#3B82F6"
PURPLE = "#8B5CF6"
GREEN = "#22C55E"
YELLOW = "#F59E0B"
RED = "#EF4444"
PINK = "#EC4899"

TEXT = "#F8FAFC"
MUTED = "#94A3B8"
BORDER = "#243A55"

PALETTE = [
    CYAN,
    PURPLE,
    GREEN,
    YELLOW,
    PINK,
    BLUE,
    "#14B8A6",
    "#F97316"
]

# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    dedent(f"""
    <style>

    .stApp {{
        background:
            radial-gradient(
                circle at 90% 0%,
                rgba(56,189,248,0.09),
                transparent 28%
            ),
            radial-gradient(
                circle at 0% 100%,
                rgba(139,92,246,0.08),
                transparent 30%
            ),
            {NAVY};
        color: {TEXT};
    }}

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(
                180deg,
                #0D192A 0%,
                #07111F 100%
            );
        border-right: 1px solid {BORDER};
    }}

    section[data-testid="stSidebar"] > div {{
        padding-top: 1.5rem;
    }}

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    /* ---------------- HERO ---------------- */

    .hero {{
        padding: 1rem 0 0.5rem 0;
    }}

    .hero-title {{
        font-size: 3rem;
        font-weight: 850;
        line-height: 1.05;
        margin-bottom: 0.6rem;
       
    }}

    .hero-subtitle {{
        color: {MUTED};
        font-size: 1.02rem;
        margin-bottom: 0.8rem;
    }}

    .developer {{
        color: {CYAN};
        font-weight: 650;
        margin-bottom: 1rem;
    }}

    .pill {{
        display: inline-block;
        padding: 0.38rem 0.75rem;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
        border-radius: 999px;
        background: rgba(56,189,248,0.08);
        border: 1px solid rgba(56,189,248,0.25);
        color: #BAE6FD;
        font-size: 0.72rem;
        font-weight: 700;
    }}

    /* ---------------- KPI ---------------- */

    .kpi-card {{
        background:
            linear-gradient(
                145deg,
                rgba(16,31,51,0.98),
                rgba(11,23,40,0.98)
            );
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 1.15rem;
        min-height: 145px;
        box-shadow:
            0 12px 30px rgba(0,0,0,0.20);
        transition: all 0.2s ease;
    }}

    .kpi-card:hover {{
        transform: translateY(-3px);
        border-color: rgba(56,189,248,0.45);
        box-shadow:
            0 16px 35px rgba(0,0,0,0.28);
    }}

    .kpi-label {{
        color: {MUTED};
        font-size: 0.76rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}

    .kpi-value {{
        color: {TEXT};
        font-size: 1.85rem;
        font-weight: 800;
        margin-top: 0.45rem;
    }}

    .kpi-caption {{
        color: {MUTED};
        font-size: 0.72rem;
        margin-top: 0.35rem;
    }}

    /* ---------------- SECTION ---------------- */

    .section-title {{
        margin-top: 2rem;
        margin-bottom: 0.15rem;
        font-size: 1.6rem;
        font-weight: 800;
        color: {TEXT};
    }}

    .section-description {{
        color: {MUTED};
        margin-bottom: 1rem;
    }}

    /* ---------------- INSIGHTS ---------------- */

    .insight {{
        padding: 1rem 1.1rem;
        margin-bottom: 0.8rem;
        border-radius: 14px;
        background: {CARD};
        border: 1px solid {BORDER};
        border-left: 4px solid {CYAN};
    }}

    .insight-good {{
        border-left-color: {GREEN};
    }}

    .insight-warning {{
        border-left-color: {YELLOW};
    }}

    .insight-danger {{
        border-left-color: {RED};
    }}

    .insight-title {{
        font-weight: 750;
        margin-bottom: 0.3rem;
        color: {TEXT};
    }}

    .insight-text {{
        color: #CBD5E1;
        font-size: 0.88rem;
        line-height: 1.5;
    }}

    /* ---------------- HEALTH ---------------- */

    .health-box {{
        padding: 1rem 1.2rem;
        border-radius: 15px;
        background: rgba(34,197,94,0.07);
        border: 1px solid rgba(34,197,94,0.20);
        color: #BBF7D0;
    }}

    /* ---------------- SIDEBAR ---------------- */

    .side-title {{
        font-size: 1.35rem;
        font-weight: 800;
        color: {TEXT};
    }}

    .side-subtitle {{
        color: {MUTED};
        font-size: 0.78rem;
        margin-top: 0.2rem;
    }}

    .side-developer {{
        color: {CYAN};
        font-size: 0.78rem;
        font-weight: 650;
        margin-top: 0.7rem;
    }}

    /* ---------------- FOOTER ---------------- */

    .footer {{
        margin-top: 3rem;
        padding: 2rem 0;
        border-top: 1px solid {BORDER};
        text-align: center;
        color: {MUTED};
    }}

    .footer-name {{
        color: {CYAN};
        font-weight: 700;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    </style>
    """))

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):

    if pd.isna(value):
        return "₹0"

    value = float(value)

    if abs(value) >= 1_000_000_000:
        return f"₹{value / 1_000_000_000:.2f}B"

    if abs(value) >= 1_000_000:
        return f"₹{value / 1_000_000:.2f}M"

    if abs(value) >= 1_000:
        return f"₹{value / 1_000:.2f}K"

    return f"₹{value:,.0f}"


def number(value):

    if pd.isna(value):
        return "0"

    return f"{value:,.0f}"


def percentage(value):

    if pd.isna(value):
        return "0.00%"

    return f"{value:.2f}%"


def style_chart(fig, height=420):

    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            color=TEXT,
            family="Arial"
        ),
        template=PLOTLY_TEMPLATE,
        margin=dict(
            l=20,
            r=20,
            t=65,
            b=40
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        ),
        hoverlabel=dict(
            bgcolor=CARD_2,
            font_color=TEXT
        )
    )

    fig.update_xaxes(
        showgrid=False,
        color=MUTED
    )

    fig.update_yaxes(
        gridcolor="rgba(148,163,184,0.12)",
        color=MUTED
    )

    return fig


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    path = Path("data/retail_sales_features.csv")

    if not path.exists():

        st.error(
            "❌ data/retail_sales_features.csv was not found."
        )

        st.stop()

    data = pd.read_csv(path)

    data["Date"] = pd.to_datetime(
        data["Date"],
        errors="coerce"
    )

    return data


@st.cache_data
def load_forecast():

    possible_files = [
        Path("data/future_sales_forecast.csv"),
        Path("outputs/reports/six_month_forecast.csv")
    ]

    for path in possible_files:

        if path.exists():

            forecast = pd.read_csv(path)

            if "Date" in forecast.columns:

                forecast["Date"] = pd.to_datetime(
                    forecast["Date"],
                    errors="coerce"
                )

            return forecast

    return pd.DataFrame()


@st.cache_data
def load_segmentation():

    path = Path("data/store_segmentation.csv")

    if not path.exists():
        return pd.DataFrame()

    return pd.read_csv(path)


df = load_data()
forecast_df = load_forecast()
segmentation_df = load_segmentation()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html(
        dedent("""
        <div>
            <div class="side-title">
                <span class="side-icon">🎯</span>
                <span>Retail Intelligence</span>
            </div>

            <div class="side-subtitle">
                Management Command Center
            </div>

            <div class="side-developer">
                👨‍💻 Developed by Mohammad Dhilawala
            </div>
        </div>
        """))

    st.divider()

    st.markdown("### 🔎 Analysis Filters")

    # Date filter
    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()

    selected_dates = st.date_input(
        "📅 Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(selected_dates, tuple):

        if len(selected_dates) == 2:

            start_date = selected_dates[0]
            end_date = selected_dates[1]

        else:

            start_date = selected_dates[0]
            end_date = selected_dates[0]

    else:

        start_date = selected_dates
        end_date = selected_dates

    # Region
    region_list = sorted(
        df["Region"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_regions = st.multiselect(
        "🌎 Region",
        region_list,
        default=region_list
    )

    # Store
    store_list = sorted(
        df["Store_ID"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_stores = st.multiselect(
        "🏪 Store",
        store_list,
        default=store_list
    )

    # Category
    category_list = sorted(
        df["Product_Category"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_categories = st.multiselect(
        "🛍️ Product Category",
        category_list,
        default=category_list
    )

    st.divider()

    st.markdown("### ⚙️ Dashboard Options")

    show_tables = st.checkbox(
        "Show detailed tables",
        value=True
    )

# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    (df["Date"].dt.date >= start_date)
    &
    (df["Date"].dt.date <= end_date)
    &
    (df["Region"].isin(selected_regions))
    &
    (df["Store_ID"].isin(selected_stores))
    &
    (df["Product_Category"].isin(selected_categories))
].copy()

if filtered_df.empty:

    st.error(
        "No data matches the selected filters."
    )

    st.stop()

# ============================================================
# HEADER
# ============================================================

st.html(
    dedent("""
    <div class="hero">

        <div class="hero-title">
            <span class="hero-icon">🎯</span>
            <span class="hero-text">Retail Intelligence Command Center</span>
        </div>

        <div class="hero-subtitle">
            AI-powered retail analytics • Sales intelligence •
            Forecasting • Store segmentation • Decision support
        </div>

        <div class="developer">
            👨‍💻 Developed by Mohammad Dhilawala
        </div>

        <span class="pill">LIVE ANALYTICS</span>
        <span class="pill">73K+ TRANSACTIONS</span>
        <span class="pill">2023–2024 DATA</span>
        <span class="pill">AI DECISION SUPPORT</span>

    </div>
    """))

st.caption(
    f"📅 Analysis Period: {start_date} → {end_date}   |   "
    f"📊 Records Analyzed: {len(filtered_df):,}"
)

# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["Total_Sales"].sum()

total_units = filtered_df["Units_Sold"].sum()

avg_transaction = (
    total_sales / len(filtered_df)
)

avg_rating = filtered_df["Store_Rating"].mean()

avg_price = filtered_df["Unit_Price"].mean()

avg_discount = filtered_df[
    "Discount_Percentage"
].mean()

# Top store
store_summary = (
    filtered_df
    .groupby("Store_ID")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

top_store = (
    store_summary.index[0]
    if len(store_summary) > 0
    else "N/A"
)

# Top category
category_summary = (
    filtered_df
    .groupby("Product_Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

top_category = (
    category_summary.index[0]
    if len(category_summary) > 0
    else "N/A"
)

# ============================================================
# PERFORMANCE PULSE
# ============================================================

st.html(
    '<div class="section-title">⚡ Performance Pulse</div>')

st.caption(
    "Management-level snapshot of the selected retail portfolio."
)

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.html(
        dedent(f"""
        <div class="kpi-card">

            <div class="kpi-label">
                💰 Total Sales
            </div>

            <div class="kpi-value">
                {money(total_sales)}
            </div>

            <div class="kpi-caption">
                Selected analysis period
            </div>

        </div>
        """))

with k2:

    st.html(
        dedent(f"""
        <div class="kpi-card">

            <div class="kpi-label">
                📦 Units Sold
            </div>

            <div class="kpi-value">
                {number(total_units)}
            </div>

            <div class="kpi-caption">
                Total quantity sold
            </div>

        </div>
        """))

with k3:

    st.html(
        dedent(f"""
        <div class="kpi-card">

            <div class="kpi-label">
                🧾 Avg Transaction
            </div>

            <div class="kpi-value">
                {money(avg_transaction)}
            </div>

            <div class="kpi-caption">
                Sales per transaction
            </div>

        </div>
        """))

with k4:

    st.html(
        dedent(f"""
        <div class="kpi-card">

            <div class="kpi-label">
                ⭐ Store Rating
            </div>

            <div class="kpi-value">
                {avg_rating:.2f}
            </div>

            <div class="kpi-caption">
                Average store rating
            </div>

        </div>
        """))

k5, k6, k7, k8 = st.columns(4)

with k5:

    st.metric(
        "💵 Average Unit Price",
        money(avg_price)
    )

with k6:

    st.metric(
        "🏷️ Average Discount",
        percentage(avg_discount)
    )

with k7:

    st.metric(
        "🏆 Top Store",
        top_store
    )

with k8:

    st.metric(
        "🛍️ Top Category",
        top_category
    )

# ============================================================
# BUSINESS HEALTH
# ============================================================

st.html(
    '<div class="section-title">❤️ Business Health Monitor</div>')

health_score = 50

if avg_rating >= 4:
    health_score += 15

if avg_discount <= 15:
    health_score += 10

if total_units > 0:
    health_score += 10

if total_sales > 0:
    health_score += 15

health_score = min(
    health_score,
    100
)

if health_score >= 80:

    health_status = "Excellent"
    health_icon = "🟢"

elif health_score >= 65:

    health_status = "Healthy"
    health_icon = "🟡"

else:

    health_status = "Needs Attention"
    health_icon = "🔴"

h1, h2 = st.columns([1, 3])

with h1:

    st.metric(
        "Business Health",
        f"{health_score}/100",
        health_status
    )

with h2:

    st.progress(
        health_score / 100
    )

    st.html(
        dedent(f"""
        <div class="health-box">
            {health_icon}
            <b>{health_status}</b> —
            Overall business health calculated from sales activity,
            units sold, store ratings and discount behavior.
        </div>
        """))

# ============================================================
# MAIN TABS
# ============================================================

tabs = st.tabs(
    [
        "🏠 Executive Overview",
        "📈 Sales Intelligence",
        "🔮 Forecast Lab",
        "🏪 Store Intelligence",
        "🤖 AI Insights",
        "🔍 Data Explorer"
    ]
)

# ============================================================
# TAB 1
# EXECUTIVE OVERVIEW
# ============================================================

with tabs[0]:

    st.html(
        '<div class="section-title">📊 Executive Overview</div>')

    st.caption(
        "A management view of revenue trends, categories, regions and customers."
    )

    # Monthly trend
    monthly = (
        filtered_df
        .set_index("Date")
        .resample("MS")["Total_Sales"]
        .sum()
        .reset_index()
    )

    monthly["Moving_Average"] = (
        monthly["Total_Sales"]
        .rolling(
            3,
            min_periods=1
        )
        .mean()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=monthly["Date"],
            y=monthly["Total_Sales"],
            mode="lines+markers",
            name="Monthly Sales",
            line=dict(
                color=CYAN,
                width=3
            ),
            marker=dict(
                size=7
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=monthly["Date"],
            y=monthly["Moving_Average"],
            mode="lines",
            name="3-Month Moving Average",
            line=dict(
                color=PURPLE,
                width=2,
                dash="dash"
            )
        )
    )

    fig.update_layout(
        title="Monthly Sales Momentum",
        xaxis_title="Month",
        yaxis_title="Sales (₹)"
    )

    st.plotly_chart(
        style_chart(fig),
        use_container_width=True
    )

    # Category and region
    c1, c2 = st.columns(2)

    with c1:

        cat = (
            filtered_df
            .groupby("Product_Category")["Total_Sales"]
            .sum()
            .sort_values()
            .reset_index()
        )

        fig = px.bar(
            cat,
            x="Total_Sales",
            y="Product_Category",
            orientation="h",
            text_auto=".2s",
            title="🛍️ Category Revenue Ranking",
            color="Total_Sales",
            color_continuous_scale=[
                "#172554",
                "#38BDF8"
            ]
        )

        fig.update_coloraxes(
            showscale=False
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    with c2:

        region = (
            filtered_df
            .groupby("Region")["Total_Sales"]
            .sum()
            .sort_values()
            .reset_index()
        )

        fig = px.bar(
            region,
            x="Region",
            y="Total_Sales",
            text_auto=".2s",
            title="🌎 Regional Performance",
            color="Total_Sales",
            color_continuous_scale=[
                "#312E81",
                "#8B5CF6"
            ]
        )

        fig.update_coloraxes(
            showscale=False
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    # Customer and payment
    c3, c4 = st.columns(2)

    with c3:

        customer = (
            filtered_df
            .groupby("Customer_Type")["Total_Sales"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            customer,
            values="Total_Sales",
            names="Customer_Type",
            hole=0.60,
            title="👥 Customer Revenue Mix",
            color_discrete_sequence=[
                CYAN,
                PURPLE,
                PINK,
                GREEN
            ]
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    with c4:

        payment = (
            filtered_df
            .groupby("Payment_Mode")["Total_Sales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            payment,
            x="Payment_Mode",
            y="Total_Sales",
            text_auto=".2s",
            title="💳 Payment Mode Performance",
            color="Payment_Mode",
            color_discrete_sequence=PALETTE
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

# ============================================================
# TAB 2
# SALES INTELLIGENCE
# ============================================================

with tabs[1]:

    st.html(
        '<div class="section-title">📈 Sales Intelligence</div>')

    st.caption(
        "Commercial analysis across years, brands, promotions and stores."
    )

    # Yearly
    yearly = (
        filtered_df
        .groupby("Year")["Total_Sales"]
        .sum()
        .reset_index()
    )

    yearly["Growth"] = (
        yearly["Total_Sales"]
        .pct_change()
        * 100
    )

    c1, c2 = st.columns(2)

    with c1:

        fig = px.bar(
            yearly,
            x="Year",
            y="Total_Sales",
            text_auto=".2s",
            title="📊 Yearly Sales Performance",
            color="Total_Sales",
            color_continuous_scale=[
                "#1E3A8A",
                "#38BDF8"
            ]
        )

        fig.update_coloraxes(
            showscale=False
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    with c2:

        if len(yearly) >= 2:

            latest_growth = yearly["Growth"].iloc[-1]

            st.metric(
                "📈 Latest YoY Growth",
                percentage(latest_growth)
            )

            if latest_growth > 0:

                st.success(
                    "Sales increased compared with the previous year."
                )

            elif latest_growth < 0:

                st.warning(
                    "Sales decreased compared with the previous year."
                )

        else:

            st.info(
                "Select a wider date range to calculate YoY growth."
            )

    # Brand analysis
    if "Brand" in filtered_df.columns:

        brands = (
            filtered_df
            .groupby("Brand")["Total_Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .sort_values()
            .reset_index()
        )

        fig = px.bar(
            brands,
            x="Total_Sales",
            y="Brand",
            orientation="h",
            text_auto=".2s",
            title="🏷️ Top 10 Brands",
            color="Total_Sales",
            color_continuous_scale=[
                "#4C1D95",
                "#A78BFA"
            ]
        )

        fig.update_coloraxes(
            showscale=False
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    # Promotion / holiday
    c1, c2 = st.columns(2)

    with c1:

        promo = (
            filtered_df
            .groupby("Promotion_Applied")["Total_Sales"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            promo,
            values="Total_Sales",
            names="Promotion_Applied",
            hole=0.60,
            title="🎯 Promotion Sales Mix",
            color_discrete_sequence=[
                CYAN,
                PURPLE
            ]
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    with c2:

        holiday = (
            filtered_df
            .groupby("Holiday_Flag")["Total_Sales"]
            .sum()
            .reset_index()
        )

        holiday["Holiday_Type"] = (
            holiday["Holiday_Flag"]
            .map(
                {
                    0: "Non-Holiday",
                    1: "Holiday"
                }
            )
            .fillna(
                holiday["Holiday_Flag"].astype(str)
            )
        )

        fig = px.bar(
            holiday,
            x="Holiday_Type",
            y="Total_Sales",
            text_auto=".2s",
            title="📅 Holiday Sales Comparison",
            color="Holiday_Type",
            color_discrete_sequence=[
                CYAN,
                PINK
            ]
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    # Store leaderboard
    store_rank = (
        filtered_df
        .groupby(
            [
                "Store_ID",
                "Store_Location",
                "Region"
            ],
            as_index=False
        )
        .agg(
            Sales=("Total_Sales", "sum"),
            Units=("Units_Sold", "sum"),
            Rating=("Store_Rating", "mean")
        )
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig = px.bar(
        store_rank.head(10)
        .sort_values("Sales"),
        x="Sales",
        y="Store_ID",
        orientation="h",
        text_auto=".2s",
        title="🏆 Top 10 Stores",
        color="Rating",
        color_continuous_scale=[
            "#065F46",
            "#22C55E"
        ],
        hover_data=[
            "Store_Location",
            "Region",
            "Units",
            "Rating"
        ]
    )

    st.plotly_chart(
        style_chart(fig),
        use_container_width=True
    )

# ============================================================
# TAB 3
# FORECAST LAB
# ============================================================

with tabs[2]:

    st.html(
        '<div class="section-title">🔮 Forecast Lab</div>')

    st.caption(
        "Future sales projection generated by the project's forecasting workflow."
    )

    if forecast_df.empty:

        st.warning(
            "Forecast file was not found."
        )

        st.info(
            "Expected file: data/future_sales_forecast.csv"
        )

    else:

        # Detect forecast column
        possible_forecast_columns = [
            "Forecast_Sales",
            "Forecast",
            "Forecasted_Sales",
            "Predicted_Sales",
            "yhat"
        ]

        forecast_column = None

        for column in possible_forecast_columns:

            if column in forecast_df.columns:

                forecast_column = column
                break

        if forecast_column is None:

            numeric_columns = (
                forecast_df
                .select_dtypes(
                    include=np.number
                )
                .columns
                .tolist()
            )

            if numeric_columns:

                forecast_column = numeric_columns[-1]

        if forecast_column is None:

            st.error(
                "Could not identify the forecast sales column."
            )

        else:

            historical = (
                df
                .groupby(
                    pd.Grouper(
                        key="Date",
                        freq="MS"
                    )
                )["Total_Sales"]
                .sum()
                .reset_index()
            )

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=historical["Date"],
                    y=historical["Total_Sales"],
                    mode="lines+markers",
                    name="Historical Sales",
                    line=dict(
                        color=CYAN,
                        width=3
                    )
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=forecast_df["Date"],
                    y=forecast_df[forecast_column],
                    mode="lines+markers",
                    name="Forecast",
                    line=dict(
                        color=PURPLE,
                        width=3,
                        dash="dash"
                    ),
                    marker=dict(
                        size=8
                    )
                )
            )

            if not forecast_df.empty:

                fig.add_vline(
                    x=forecast_df["Date"].min(),
                    line_dash="dot",
                    line_color=YELLOW,
                    annotation_text="Forecast Start"
                )

            fig.update_layout(
                title="Historical Sales vs Forecast",
                xaxis_title="Month",
                yaxis_title="Sales (₹)"
            )

            st.plotly_chart(
                style_chart(fig, 480),
                use_container_width=True
            )

            forecast_total = (
                forecast_df[forecast_column].sum()
            )

            forecast_average = (
                forecast_df[forecast_column].mean()
            )

            latest_actual = (
                historical["Total_Sales"].iloc[-1]
            )

            forecast_change = (
                (
                    forecast_average
                    - latest_actual
                )
                / latest_actual
                * 100
            )

            f1, f2, f3, f4 = st.columns(4)

            with f1:

                st.metric(
                    "🔮 Avg Monthly Forecast",
                    money(forecast_average)
                )

            with f2:

                st.metric(
                    "📅 Forecast Horizon",
                    f"{len(forecast_df)} Months"
                )

            with f3:

                st.metric(
                    "💰 Forecast Total",
                    money(forecast_total)
                )

            with f4:

                st.metric(
                    "📈 vs Latest Actual",
                    percentage(forecast_change)
                )

            st.markdown(
                "### 📋 Forecast Schedule"
            )

            forecast_display = forecast_df.copy()

            if "Date" in forecast_display.columns:

                forecast_display["Date"] = (
                    forecast_display["Date"]
                    .dt.strftime("%B %Y")
                )

            forecast_display[forecast_column] = (
                forecast_display[forecast_column]
                .map(money)
            )

            st.dataframe(
                forecast_display,
                use_container_width=True,
                hide_index=True
            )

            forecast_download = (
                forecast_df
                .to_csv(index=False)
                .encode("utf-8")
            )

            st.download_button(
                "⬇️ Download Forecast",
                forecast_download,
                "future_sales_forecast.csv",
                "text/csv"
            )

# ============================================================
# TAB 4
# STORE INTELLIGENCE
# ============================================================

with tabs[3]:

    st.html(
        '<div class="section-title">🏪 Store Intelligence</div>')

    st.caption(
        "Analyze store performance and machine-learning segmentation."
    )

    store_data = (
        filtered_df
        .groupby(
            [
                "Store_ID",
                "Store_Location",
                "Region"
            ],
            as_index=False
        )
        .agg(
            Total_Sales=("Total_Sales", "sum"),
            Units_Sold=("Units_Sold", "sum"),
            Avg_Rating=("Store_Rating", "mean")
        )
    )

    c1, c2 = st.columns(2)

    with c1:

        fig = px.bar(
            store_data
            .sort_values("Total_Sales")
            .tail(10),
            x="Total_Sales",
            y="Store_ID",
            orientation="h",
            text_auto=".2s",
            title="🏆 Top Store Revenue",
            color="Total_Sales",
            color_continuous_scale=[
                "#164E63",
                "#38BDF8"
            ]
        )

        fig.update_coloraxes(
            showscale=False
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    with c2:

        fig = px.scatter(
            store_data,
            x="Total_Sales",
            y="Units_Sold",
            size="Total_Sales",
            color="Region",
            hover_name="Store_ID",
            hover_data=[
                "Store_Location",
                "Avg_Rating"
            ],
            title="📊 Store Value vs Volume",
            color_discrete_sequence=PALETTE
        )

        st.plotly_chart(
            style_chart(fig),
            use_container_width=True
        )

    # Segmentation
    if not segmentation_df.empty:

        st.markdown(
            "### 🧩 Store Segmentation"
        )

        if "Segment" in segmentation_df.columns:

            segments = (
                segmentation_df["Segment"]
                .value_counts()
                .reset_index()
            )

            segments.columns = [
                "Segment",
                "Store_Count"
            ]

            c1, c2 = st.columns(2)

            with c1:

                fig = px.pie(
                    segments,
                    values="Store_Count",
                    names="Segment",
                    hole=0.58,
                    title="Segment Distribution",
                    color_discrete_sequence=[
                        CYAN,
                        PURPLE,
                        PINK,
                        GREEN
                    ]
                )

                st.plotly_chart(
                    style_chart(fig),
                    use_container_width=True
                )

            with c2:

                fig = px.bar(
                    segments,
                    x="Segment",
                    y="Store_Count",
                    text="Store_Count",
                    title="Stores by Segment",
                    color="Segment",
                    color_discrete_sequence=PALETTE
                )

                st.plotly_chart(
                    style_chart(fig),
                    use_container_width=True
                )

            if show_tables:

                st.dataframe(
                    segmentation_df,
                    use_container_width=True,
                    hide_index=True
                )

    else:

        st.info(
            "Store segmentation file is not available."
        )

# ============================================================
# TAB 5
# AI INSIGHTS
# ============================================================

with tabs[4]:

    st.html(
        '<div class="section-title">🤖 AI-Powered Business Intelligence</div>')

    st.caption(
        "Automated business observations based on the selected data."
    )

    # Category
    category_sales = (
        filtered_df
        .groupby("Product_Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    best_category = category_sales.index[0]

    best_category_sales = category_sales.iloc[0]

    st.html(
        dedent(f"""
        <div class="insight">

            <div class="insight-title">
                🛍️ Category Leader
            </div>

            <div class="insight-text">
                <b>{best_category}</b> is currently the
                highest-performing category with sales of approximately
                <b>{money(best_category_sales)}</b>.
            </div>

        </div>
        """))

    # Region
    region_sales = (
        filtered_df
        .groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    best_region = region_sales.index[0]

    best_region_sales = region_sales.iloc[0]

    st.html(
        dedent(f"""
        <div class="insight">

            <div class="insight-title">
                🌎 Regional Leader
            </div>

            <div class="insight-text">
                <b>{best_region}</b> is generating the highest
                regional sales at approximately
                <b>{money(best_region_sales)}</b>.
            </div>

        </div>
        """))

    # Store
    store_sales = (
        filtered_df
        .groupby("Store_ID")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    best_store = store_sales.index[0]

    best_store_sales = store_sales.iloc[0]

    st.html(
        dedent(f"""
        <div class="insight insight-good">

            <div class="insight-title">
                🏆 Store Champion
            </div>

            <div class="insight-text">
                <b>{best_store}</b> is the strongest store
                in the selected portfolio, generating approximately
                <b>{money(best_store_sales)}</b>.
            </div>

        </div>
        """))

    # Customer
    customer_sales = (
        filtered_df
        .groupby("Customer_Type")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    best_customer = customer_sales.index[0]

    customer_share = (
        customer_sales.iloc[0]
        / customer_sales.sum()
        * 100
    )

    st.html(
        dedent(f"""
        <div class="insight">

            <div class="insight-title">
                👥 Customer Intelligence
            </div>

            <div class="insight-text">
                <b>{best_customer}</b> customers represent approximately
                <b>{customer_share:.1f}%</b> of selected sales.
            </div>

        </div>
        """))

    # Discount
    if avg_discount > 15:

        st.html(
            dedent(f"""
            <div class="insight insight-warning">

                <div class="insight-title">
                    🏷️ Discount Alert
                </div>

                <div class="insight-text">
                    Average discount is <b>{avg_discount:.2f}%</b>.
                    Management should review whether discounting is
                    generating sufficient sales value.
                </div>

            </div>
            """))

    else:

        st.html(
            dedent(f"""
            <div class="insight insight-good">

                <div class="insight-title">
                    ✅ Discount Efficiency
                </div>

                <div class="insight-text">
                    Average discount is <b>{avg_discount:.2f}%</b>,
                    indicating relatively controlled discount activity.
                </div>

            </div>
            """))

    # Anomaly detection
    monthly_ai = (
        filtered_df
        .set_index("Date")
        .resample("MS")["Total_Sales"]
        .sum()
        .reset_index()
    )

    if len(monthly_ai) >= 4:

        mean_sales = monthly_ai["Total_Sales"].mean()

        std_sales = monthly_ai["Total_Sales"].std()

        if std_sales > 0:

            monthly_ai["Z_Score"] = (
                monthly_ai["Total_Sales"]
                - mean_sales
            ) / std_sales

            anomalies = monthly_ai[
                monthly_ai["Z_Score"].abs() >= 2
            ]

        else:

            anomalies = pd.DataFrame()

    else:

        anomalies = pd.DataFrame()

    if not anomalies.empty:

        st.html(
            dedent(f"""
            <div class="insight insight-danger">

                <div class="insight-title">
                    🚨 Sales Anomaly Detector
                </div>

                <div class="insight-text">
                    Detected <b>{len(anomalies)}</b>
                    unusual monthly sales movement(s).
                    These periods deserve additional management review.
                </div>

            </div>
            """))

    else:

        st.html(
            dedent("""
            <div class="insight insight-good">

                <div class="insight-title">
                    ✅ Sales Stability
                </div>

                <div class="insight-text">
                    No major monthly sales anomalies were detected
                    in the current selection.
                </div>

            </div>
            """))

    # Recommendations
    st.markdown(
        "### 💡 Management Recommendations"
    )

    recommendations = [
        f"Prioritize inventory planning for {best_category}.",
        f"Study successful practices in the {best_region} region.",
        f"Use {best_store} as a benchmark for store performance.",
        "Use targeted promotions instead of unnecessary broad discounts.",
        "Monitor monthly sales anomalies for early business intervention."
    ]

    for item in recommendations:

        st.html(
            dedent(f"""
            <div class="insight">

                <div class="insight-text">
                    💡 {item}
                </div>

            </div>
            """))

# ============================================================
# TAB 6
# DATA EXPLORER
# ============================================================

with tabs[5]:

    st.html(
        '<div class="section-title">🔍 Data Explorer</div>')

    st.caption(
        "Explore the filtered dataset used by the dashboard."
    )

    d1, d2, d3, d4 = st.columns(4)

    with d1:

        st.metric(
            "📊 Records",
            f"{len(filtered_df):,}"
        )

    with d2:

        st.metric(
            "🏪 Stores",
            filtered_df["Store_ID"].nunique()
        )

    with d3:

        st.metric(
            "🛍️ Categories",
            filtered_df["Product_Category"].nunique()
        )

    with d4:

        st.metric(
            "🌎 Regions",
            filtered_df["Region"].nunique()
        )

    st.markdown(
        "### 📋 Filtered Dataset"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=500,
        hide_index=True
    )

    csv_data = (
        filtered_df
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        "⬇️ Download Filtered Dataset",
        csv_data,
        "filtered_retail_sales.csv",
        "text/csv"
    )

# ============================================================
# FOOTER
# ============================================================

st.html(
    dedent("""
    <div class="footer">

        <div style="font-size:22px;">
            🎯 <b>Retail Intelligence Command Center</b>
        </div>

        <br>

        Retail Analytics • AI Forecasting •
        Store Segmentation • Business Intelligence

        <br><br>

        <span class="footer-name">
            👨‍💻 Developed by Mohammad Dhilawala
        </span>

        <br><br>

        <small>
            Retail Analytics & AI-Powered Sales Forecasting System
            <br>
            Academic Major Project • Python • Streamlit • Machine Learning
        </small>

    </div>
    """))