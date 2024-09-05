import streamlit as st
import pandas as pd
import numpy as np

# plotly
import plotly.express as px

# load data
df = px.data.tips()

# Reference URL: https://plotly.com/python/plotly-express/
# 1. Draw histogram for total bill
# 2. Draw histogram for total bill and color by sex
# 3. Draw histogram for total bill and color by (sex, smoker, day, time)
# 4. Draw Scatter plot between total_bill and tips and color by 
#    ((sex, smoker, day, time)))
# 5. Sunburst Chart on features (sex, smoker, day, time))

st.subheader('1. Draw histogram for total bill')
fig1 = px.histogram(df, x='total_bill')
st.plotly_chart(fig1)

st.subheader('2. Draw histogram for total bill and color by categorical columns')
cat_cols = df.dtypes[df.dtypes == 'object'].index

selected_col1 = st.selectbox('Select Column', tuple(cat_cols), key='select1')

fig2 = px.histogram(df, x='total_bill', color=selected_col1)
st.plotly_chart(fig2)

st.subheader('3. Draw histogram for total bill and color by (sex, smoker, day, time)')

with st.expander('DataFrame Table'):
    st.dataframe(df.sort_values(by=selected_col1))

st.subheader("""
             4. Draw Scatter plot between total_bill and tips and color by ((sex, smoker, day, time))
""")
selected_col2 = st.selectbox('Select Column', tuple(cat_cols), key='select2')
fig3 = px.scatter(df, x='total_bill', y='tip', color=selected_col2)
st.plotly_chart(fig3)

st.subheader('5. Sunburst Chart on features (sex, smoker, day, time)')
path = st.multiselect('Select the categorical features path', tuple(cat_cols), key='multi1')
fig4 = px.sunburst(df, path=path)
st.plotly_chart(fig4)