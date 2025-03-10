import streamlit as st
import pandas as pd

# from pathlib import Path
from supabase import create_client, Client


@st.cache_resource
def conn_db() -> Client:
    url: str = st.secrets["supabase"]["url"]
    key: str = st.secrets["supabase"]["key"]

    client: Client = create_client(url, key)

    return client


@st.cache_resource
def run_query(_client):
    return _client.table("car_parts_monthly_sales").select("*").execute()


if __name__ == "__main__":
    st.set_page_config("DB connector", page_icon=":shark:")

    st.title("Query a database")
    if all(value for value in st.secrets["supabase"]):
        st.info("URL and JWT to connect DB is exist.")

    supa = conn_db()
    rows = run_query(supa)
    df = pd.json_normalize(rows.data)
    st.dataframe(df)
