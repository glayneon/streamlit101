import streamlit as st
from datetime import datetime, time

st.set_page_config(
    page_title="Assignment-1",
    layout="wide",
    menu_items=(
        {
            "Get help": "https://www.aaaa.com/help",
            "Report a bug": "https://bbbbbb.com/bug",
            "About": "# This is a header. This is an *extremely* cool app!",
        }
    ),
)

with st.container(border=True):
    st.title("Registration Form")
    col1, col2, col3 = st.columns(3)

    # col1
    with col1:
        col1.metric("Temperatur", "70F", "1.2F")
        sir_name = st.selectbox("", options=("Mr", "Miss", "Mrs"))

    with col2:
        col2.metric("Wind", "9 mph", "-8%")
        first_name = st.text_input("First Name")

    with col3:
        col3.metric("Humidity", "86%", "4%")
        last_name = st.text_input("Last name")

    job = st.selectbox(
        "Designation",
        options=(
            "Software",
            "Sr. Software",
            "Technical Lead",
            "Manager",
            "Sr. Manager",
            "Project Manager",
        ),
    )

    birth = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1, 0, 1))
    mybirth = datetime.combine(birth, time(1, 1, 1))
    now = datetime.now() - mybirth
    your_age = int(now.days / 365.0)

    gender = st.radio(
        "Select Gender", options=("Mail", "Female", "Prefered Not to Say")
    )

    age = st.slider("Age", 1, 100, value=your_age)

    submited = st.button("Submit", key="submit1")
    if submited:
        if age and gender and job and last_name and first_name and sir_name:
            name = f"{sir_name} {first_name} {last_name}"
            user_info = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Date of Birth": birth,
                "Designation": job,
            }
            st.success("Form Submitted Successfully")
            st.json(user_info)
        else:
            st.warning("All Forms are not filled.")
