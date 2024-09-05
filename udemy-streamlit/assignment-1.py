import streamlit as st
from datetime import datetime, timedelta

with st.container(border=True):
    st.title('Registration Form')
    col1, col2, col3 = st.columns(3)
    
    #col1
    with col1:
        sir_name = st.selectbox('', options=('Mr', 'Miss', 'Mrs'))
    
    with col2:
        first_name = st.text_input('First Name')

    with col3:
        last_name = st.text_input('Last name')
    
    job = st.selectbox(
        "Designation",
        options = (
            "Software",
            'Sr. Software',
            'Technical Lead',
            'Manager',
            'Sr. Manager',
            'Project Manager',
        )
    )

    birth = st.date_input(
        'Date of Birth',
        min_value = datetime(1900, 1, 1, 0, 1)
    )

    gender = st.radio(
        'Select Gender',
        options = ('Mail', 'Female', 'Prefered Not to Say')
        )
    
    age = st.slider('Age', 1, 100, 20)

    submited = st.button('Submit', key='submit1')
    if submited:
        if age and gender and job and last_name and first_name and sir_name:
            name = f"{sir_name} {first_name} {last_name}"
            user_info = {
                'Name': name,
                'Age': age,
                'Gender': gender,
                'Date of Birth': birth,
                'Designation': job,
            }
            st.success('Form Submitted Successfully')
            st.json(user_info)
        else:
            st.warning('All Forms are not filled.')
