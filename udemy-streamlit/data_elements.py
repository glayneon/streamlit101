import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('./tips.csv')

# st.dataframe to display
st.header('st.dataframe')
st.caption('Display a dataframe as an interactive table')

st.dataframe(data=df.head(10), width=1000)

# st.markdown('---')
# st.header('st.write(df)')
# st.caption('Display a dataframe as an interactive table')
# st.write(df)

# st.static
st.header('st.table')
st.caption('Display as a static table')
st.table(data=df.head(10))

# st.json
st.header('st.json')
st.caption('Display object or string as a pretty-printed JSON string')

json_values = df.head(3).to_dict()
st.json(json_values)