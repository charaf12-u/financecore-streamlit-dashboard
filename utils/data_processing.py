import streamlit as st
import pandas as pd
from core.db_connection import get_engine
from core.queries import MAIN_QUERY
from utils.logger import *


# --> read data from database
def load_data():
    try:
        log_info("Loading data from database")
        # --> get database connection and execute query
        engine = get_engine()
        df = pd.read_sql(MAIN_QUERY, engine)
        # --> check empty dataframe
        if df.empty:
            log_warning("Database query returned an empty dataframe")

        return df

    except Exception as e:
        log_error(f"Error loading data: {str(e)}")
        raise


# --> clean data
def clean_data(df):
    try:
        # --> convert date_transaction to datetime
        df["date_transaction"] = pd.to_datetime(df["date_transaction"])
        # --> check for null
        if df["montant_eur"].isnull().sum() > 0:
            log_warning("Null values detected in montant_eur")
        df["montant_eur"] = df["montant_eur"].fillna(0)
        df["is_anomaly"] = df["is_anomaly"].fillna(False)
        # --> check for duplicates
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            log_warning(f"{duplicates} duplicate rows detected")
        df = df.drop_duplicates()

        log_info("Data cleaned successfully")

        return df

    except Exception as e:
        log_error(f"Error during data cleaning: {str(e)}")
        raise


# --> feature engineering
def feature_engineering(df):
    try:
        df["year"] = df["date_transaction"].dt.year
        df["month"] = df["date_transaction"].dt.month
        df["transaction_type"] = df["montant_eur"].apply(
            lambda x: "Positive" if x >= 0 else "Negative"
        )

        log_info("Feature engineering completed")

        return df

    except Exception as e:
        log_error(f"Feature engineering failed: {str(e)}")
        raise


# --> validate data
def validate_data(df):
    try:
        log_info(f"Shape: {df.shape}")

        null_counts = df.isnull().sum().sum()
        if null_counts > 0:
            log_warning(f"Dataset contains {null_counts} null values")

        log_info("Data validation completed")

        return df

    except Exception as e:
        log_error(f"Validation failed: {str(e)}")
        raise



@st.cache_data
def get_processed_data():

    df = load_data()
    df = clean_data(df)
    df = feature_engineering(df)
    df = validate_data(df)

    return df
