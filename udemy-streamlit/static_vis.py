import streamlit as st
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns


# load data
tips = pd.read_csv('tips.csv')
categories = tips.dtypes
cat_cols = tuple(categories[categories == 'object'].index)
sample_df = pd.DataFrame({
    'A': [3, 5, 3, 9, 7],
    'B': [0, 1, 3, 9, 7],
    'C': [8, 7, 8, 1, 7],
})

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
    days = tips[selected].value_counts()
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
        # st.bar_chart(sample_df)
    
    with st.expander('Click here to display value counts.'):
    # button = st.button('Counting', key='value1')
    # if button:
    #     st.success(f"Button is {button}")
    #     st.dataframe(tips.head())
        st.dataframe(tips.head())
        # st.write(tips.dtypes)


## 2. Find distribution of Male and Female spent (boxplot or kdeplot)
st.markdown('---')

with st.container(border=True):
    st.write('#### 2. Find distribution of Male and Female spent (boxplot or kdeplot)')
    # box, violin, kdeplot, histgram
    chart = ('box', 'violin', 'kdeplot', 'histogram')
    chart_choice = st.selectbox('Select the chart type', options=chart)
    fig, ax = plt.subplots()

    if chart_choice == 'box':
        sns.boxplot(x='sex', y='total_bill', data=tips, hue='time', palette='winter')
    elif chart_choice == 'violin':
        sns.violinplot(x='sex', y='total_bill', data=tips, ax=ax, hue='time')
    elif chart_choice =='kdeplot':
        sns.kdeplot(x=tips['total_bill'], hue=tips['sex'], ax=ax, shade=True)
    elif chart_choice =='histogram':
        sns.histplot(x='total_bill', hue='sex', data=tips, ax=ax)

    st.pyplot(fig)


## 3. Find distribution of average total_bill across each day by male and female
# bar, area, line
st.markdown('---')
features_to_groupby = ['day', 'sex']
feature = ['total_bill']
select_cols = feature + features_to_groupby
avg_total_bill = tips[select_cols].groupby(features_to_groupby).mean()
avg_total_bill = avg_total_bill.unstack()

with st.container(border=True):
    st.write('#### 3. Find distribution of average total_bill across each day bo male and female')
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind='bar', ax=ax)
    # ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    # ax.bar(avg_total_bill.index, avg_total_bill)
    st.pyplot(fig)

## 4. Find the relation between total_bill and tip on time (scatter plot)
# 1. include all categorical features (multiselect)
# 2. bar, area, line (selectbox)
# 3. stacked (radio)
with st.container():
    c1, c2, c3 = st.columns(3)

    with c1:
        group_cols = st.multiselect('Select columns', cat_cols, default='day')
        features_to_groupby = group_cols
        n_features = len(features_to_groupby)

    with c2:
        chart_type = st.selectbox('Select Chart type',
                                  ('bar', 'area', 'line'))

    with c3:
        stack_option = st.radio('Stacked', ('Yes', 'No'))
        if stack_option == 'Yes':
            stacked = True
        else:
            stacked = False

    feature = ['total_bill']
    select_cols = feature + features_to_groupby
    avg_total_bill = tips[select_cols].groupby(features_to_groupby).mean()

    if n_features > 1:
        for i in range(n_features-1):
            avg_total_bill = avg_total_bill.unstack()
    
    avg_total_bill.fillna(0, inplace=True)

    # visual
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type, ax=ax, stacked=stacked)
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.set_ylabel('Avg Total Bill')
    # ax.bar(avg_total_bill.index, avg_total_bill)
    st.pyplot(fig)

with st.expander('Click here to display values'):
    st.dataframe(avg_total_bill)