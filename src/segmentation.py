
"""
Store Segmentation Module

Uses K-Means clustering to group stores
based on sales and sales volume.

Developed by Mohammad Dhilawala
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def create_store_features(df):
    """Create store-level performance features."""

    store_features = (
        df.groupby(
            ["Store_ID", "Store_Location", "Region"]
        )
        .agg(
            Total_Sales=("Total_Sales", "sum"),
            Total_Units_Sold=("Units_Sold", "sum"),
            Average_Unit_Price=("Unit_Price", "mean"),
            Average_Discount=("Discount_Percentage", "mean"),
            Average_Rating=("Store_Rating", "mean")
        )
        .reset_index()
    )

    return store_features


def perform_segmentation(store_features, clusters=3):
    """Perform K-Means store segmentation."""

    features = store_features[
        [
            "Total_Sales",
            "Total_Units_Sold",
            "Average_Unit_Price"
        ]
    ]

    scaler = StandardScaler()

    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(
        n_clusters=clusters,
        random_state=42,
        n_init=10
    )

    store_features["Cluster"] = kmeans.fit_predict(
        scaled_features
    )

    return store_features, kmeans


def assign_segment_names(store_features):
    """Convert numerical clusters into business-friendly segments."""

    cluster_sales = (
        store_features
        .groupby("Cluster")["Total_Sales"]
        .mean()
        .sort_values(ascending=False)
    )

    segment_names = {}

    clusters = list(cluster_sales.index)

    if len(clusters) >= 3:

        segment_names[clusters[0]] = "High Value Stores"
        segment_names[clusters[1]] = "High Volume Stores"
        segment_names[clusters[2]] = "Lower Performance Stores"

    store_features["Segment"] = (
        store_features["Cluster"]
        .map(segment_names)
    )

    return store_features


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/retail_sales_features.csv"
    )

    store_features = create_store_features(df)

    store_features, model = perform_segmentation(
        store_features
    )

    store_features = assign_segment_names(
        store_features
    )

    store_features.to_csv(
        "../data/store_segmentation.csv",
        index=False
    )

    print("Store segmentation completed.")

    print(
        store_features[
            [
                "Store_ID",
                "Store_Location",
                "Region",
                "Total_Sales",
                "Total_Units_Sold",
                "Segment"
            ]
        ]
    )