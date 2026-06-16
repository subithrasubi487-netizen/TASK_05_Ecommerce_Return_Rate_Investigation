# ==========================================
# Ecommerce Return Rate Investigation
# Reusable Analysis Functions
# ==========================================

import pandas as pd


# Return Percentage

def calculate_return_percentage(df):

    total_orders = len(df)

    returned = (

        df["Return_Status"]

        .astype(str)

        .str.strip()

        .eq("Returned")

        .sum()

    )

    percentage = (

        returned / total_orders

    ) * 100

    return round(
        percentage,
        2
    )


# Missing Values

def check_missing(df):

    return df.isnull().sum()


# Remove Duplicates

def remove_duplicates(df):

    return df.drop_duplicates()


# Average Product Price

def average_price(df):

    return round(

        df["Product_Price"]

        .mean(),

        2

    )


# Average Delivery Duration

def average_delivery(df):

    return round(

        df["Days_to_Return"]

        .mean(),

        2

    )