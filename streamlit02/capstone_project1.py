import streamlit as st
import pandas as pd

# import numpy as np
import plotly.express as px
# import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/master/12_dashboard_capstone/data/quarterly_canada_population.csv"
title = "Population of Canada"
st.set_page_config(title, layout="centered")


@st.cache_data
def read_df():
    df = pd.read_csv(URL)
    return df


# Convert String date to float
@st.cache_data
def format_date_for_comparison(date):
    if date[1] == "2":
        return float(date[2:]) + 0.25
    elif date[1] == "3":
        return float(date[2:]) + 0.5
    elif date[1] == "4":
        return float(date[2:]) + 0.75
    else:
        return float(date[2:])


# Compare start_date and end_date
@st.cache_data
def end_before_start(start_date, end_date):
    start_date = format_date_for_comparison(start_date)
    end_date = format_date_for_comparison(end_date)

    if start_date > end_date:
        return True
    else:
        return False


def display_dashboard(start_date, end_date, location):
    tab1, tab2 = st.tabs(["Population of Change", "Compare"])

    with tab1:
        st.subheader(f"Population Change from {start_date} to {end_date}")

        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            initial = df.loc[df["Quarter"] == start_date, location].item()
            final = df.loc[df["Quarter"] == end_date, location].item()

            percentage_diff = round((final - initial) / initial * 100, 2)
            delta = f"{percentage_diff}%"
            st.metric(start_date, value=initial)
            st.metric(end_date, value=final, delta=delta)

        with col2:
            start_idx = df.loc[df["Quarter"] == start_date].index.item()
            end_idx = df.loc[df["Quarter"] == end_date].index.item()
            filtered_df = df.iloc[start_idx : end_idx + 1]

            fig1 = px.line(
                filtered_df,
                x="Quarter",
                y=location,
                title=f"Population Change of {location}",
            )
            st.plotly_chart(fig1)

    with tab2:
        st.subheader("Compare with other locations")
        all_targets = st.multiselect(
            "Choose other locations",
            options=filtered_df.columns[1:],
            default=[location],
        )

        fig2 = px.scatter(
            filtered_df,
            x="Quarter",
            y=all_targets,
        )
        st.plotly_chart(fig2)


if __name__ == "__main__":
    # Page setting
    df = read_df()

    st.title(title)
    st.write(
        "Source table can be found [here](https://www150.statcan.gc.ca/n1/pub/71-607-x/71-607-x2018005-eng.htm)"
    )

    with st.expander("See full data table"):
        st.dataframe(df)

    with st.form(key="form1"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("Choose a starting date")
            start_qt = st.selectbox(
                "Quarter",
                options=("Q1", "Q2", "Q3", "Q4"),
                index=2,
                key="start_qt",
            )
            start_year = st.slider(
                "Year", 1991, 2023, 1991, step=1, key="start_y"
            )

        with col2:
            st.write("Choose an end date")
            end_qt = st.selectbox(
                "Quarter",
                options=("Q1", "Q2", "Q3", "Q4"),
                index=0,
                key="end_qt",
            )
            end_year = st.slider("Year", 1991, 2023, 2023, step=1, key="end_y")

        with col3:
            st.write("Choose a location")
            location = st.selectbox("Choose a location", options=df.columns[1:])

        submitted = st.form_submit_button("Analyze", type="primary")

    # concatenate quarter and year
    start_date = f"{start_qt} {start_year}"
    end_date = f"{end_qt} {end_year}"

    # Show all values entered in input widgets
    with st.expander("Check all input in json."):
        st.json(
            {
                "start_date": start_date,
                "end_date": end_date,
                "location": location,
            }
        )

    if (
        start_date not in df["Quarter"].tolist()
        or end_date not in df["Quarter"].tolist()
    ):
        st.error("No data available. Check your quarter and year selection")
    elif end_before_start(start_date, end_date):
        st.error("Dates don't work. Start date must come before end date.")
    else:
        display_dashboard(start_date, end_date, location)
