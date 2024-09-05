import streamlit as st
import numpy as np
import pandas as pd

# title
st.title('This is Title')
st.caption('Using st.title() you can  display text and title format.')

# header
st.header('This is header')
st.caption('The text inside st.header() is in header formatting')

# sub header
st.subheader('This is subheader')
st.caption('The text insider st.subheader() is in subheader formatting.')

# code
st.markdown('---')
st.subheader('Display code in python')
body = """
import streamlit as st

st.write("# Hello World :sunglasses")
"""

st.code(body, language='python')

# Latex
st.subheader('Latex')
formula = """
a + ar + ar^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k
""" 
st.latex(formula)