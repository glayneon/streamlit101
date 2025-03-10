import streamlit as st
from datetime import datetime, timedelta
import seaborn as sns

st.set_page_config("Assignment01")

with st.sidebar:
    st.write("# Udemy Assignment")
    "[My Git Repo](https://github.com/glayneon/streamlit101.git)"

# main
today = datetime.now().date()
now = datetime.now().time()
max_day = datetime.now() + timedelta(14)

st.header("Menu", divider=True)

with st.form("form1"):
    st.write("What would you like to order ?")
    appetizer = st.selectbox(
        "Appetizers",
        options=("choice1", "choice2", "choice3"),
        key="select_box1",
    )
    main_course = st.selectbox(
        "Main Course",
        options=("choice1", "choice2", "choice3"),
        key="select_box2",
    )
    dessert = st.selectbox(
        "Dessert",
        options=("Vanila", "Choco", "Berry"),
        key="select_box3",
    )
    wine = st.checkbox("Are you bringing your own wine?")

    book_date = st.date_input("When are you comming", today, today, max_day)
    book_time = st.time_input(
        "At what time are you comming?",
        now,
    )

    check_allergies = st.text_area("Any allergies?", max_chars=300)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.json(
            {
                "Appetizer": appetizer,
                "Main": main_course,
                "Dessert": dessert,
                "Bring Your Wine": "yes" if wine else "no",
                "Booking Date": book_date,
                "Booking Time": book_time,
                "Allergies": check_allergies,
            }
        )


df = sns.load_dataset("tips")

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Dataframe"])

with tab1:
    st.write("Line Chart")
    st.line_chart(df, x="day", y=("tip",), x_label="Dollar", y_label="Day")

with tab2:
    st.write("Bar Chart")
    st.bar_chart(df, x="day", y=("sex", "smoker", "time"))

with tab3:
    st.write("DataSet for Graph")
    st.dataframe(df.sort_values(by="total_bill", ascending=False))

with st.expander("Click to expand for st.tabs"):
    st.code(
        """
tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Dataframe"])

with tab1:
    st.write("Line Chart")
    st.line_chart(df, x="day", y=("tip",), x_label="Dollar", y_label="Day")

with tab2:
    st.write("Bar Chart")
    st.bar_chart(df, x="day", y=("sex", "smoker", "time"))

with tab3:
    st.write("DataSet for Graph")
    st.dataframe(df.sort_values(by="total_bill", ascending=False))

""",
        language="python",
    )
