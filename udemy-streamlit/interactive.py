import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

sample = pd.DataFrame(
    np.random.randint(10, 20, size=(5,3)), 
    columns=['A', 'B', 'C'],
    )



st.title('Interactive Visuals')
c1, c2, c3 = st.columns(3)

# bar_plot
with c1:
    st.bar_chart(sample, horizontal=True, stack=False)

# area_plot
with c2:
    st.area_chart(sample)

# line_plot
with c3:
    st.line_chart(sample)