import streamlit as st
import pandas as pd
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title='Simple Line Chart')

p.line(x, y)

st.bokeh_chart(p)