import streamlit as st
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns


# load data
penguins = sns.load_dataset('penguins')
categories = penguins.dtypes
cat_cols = tuple(categories[categories == 'object'].index)

# side bar
side_bar = st.sidebar
side_bar.title('Graphics in Streamlit')

side_bar.header('Matplotlib', divider=True)

# Questions
# 1. Find number of Mail and Female distribution (pie and bar)
# 2. Find distribution of Male and Female spent (boxplot or kdeplot)
# 3. Find distribution of average total_bill across each day bo male and female
# 4. Find the relation between total_bill and tip on time (scatter plot)

# with col1:
with st.container(border=True):
    # st.header('Pie and Bar', divider=True)
    st.write('1. Find number of Mail and Female distribution (pie and bar)')
    selected = st.selectbox('Select Columns', options=cat_cols, index=1, key='selected1')
    days = penguins[selected].value_counts()
    # columns
    col1, col2 = st.columns(2)
    
    # draw pie chart
    with col1:
        st.subheader('Pie Chart', divider=True)
        fig, ax = plt.subplots()
        ax.pie(days, autopct='%0.2f%%', labels=days.index)
        st.pyplot(fig)

    # draw bar chart
    with col2:
        st.subheader('Bar Chart', divider=True)
        fig, ax = plt.subplots()
        ax.bar(days.index, days)
        st.pyplot(fig)
    
    with st.expander('Click here to display value counts.'):
    # button = st.button('Counting', key='value1')
    # if button:
    #     st.success(f"Button is {button}")
    #     st.dataframe(tips.head())
        st.dataframe(penguins.head())
        # st.write(tips.dtypes)
