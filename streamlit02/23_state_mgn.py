import streamlit as st
from datetime import date, timedelta


def add_timedelta():
    initial = st.session_state["start_date"]
    if st.session_state["radio_range"] == "7 days":
        st.session_state["end_date"] = initial + timedelta(days=7)

    elif st.session_state["radio_range"] == "28 days":
        st.session_state["end_date"] = initial + timedelta(days=28)

    else:
        pass


def subtract_timedelta():
    final = st.session_state["end_date"]
    if st.session_state["radio_range"] == "7 days":
        st.session_state["start_date"] = final - timedelta(days=7)

    elif st.session_state["radio_range"] == "28 days":
        st.session_state["start_date"] = final - timedelta(days=28)

    else:
        pass


# main
if __name__ == "__main__":
    st.set_page_config("Advanced State Mangement")
    st.title("Advanced State Management")

    st.subheader("Store widget value in session state")
    st.slider("Select a number", 0, 10, key="slider1")
    st.write(st.session_state)

    st.subheader("Initialize widget value with session state")

    if "num_input" not in st.session_state:
        st.session_state["num_input"] = 5

    st.number_input("Pick a number", 0, 10, key="num_input")

    st.subheader("Use callbacks")

    st.markdown("#### Select your time range")

    radio_select = st.radio(
        "Select a range",
        ["7 days", "28 days", "custom"],
        horizontal=True,
        key="radio_range",
        on_change=add_timedelta,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.date_input("Start date", key="start_date", on_change=add_timedelta)
    with col2:
        st.date_input("End date", key="end_date", on_change=subtract_timedelta)
