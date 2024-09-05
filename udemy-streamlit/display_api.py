import streamlit as st
import pandas as pd
import numpy as np

# display almost anything
# st.write
st.write('# Hello World, :sunglasses:')

st.write('Welcome to Streamlit App APIs')

st.write(1234)

df = pd.DataFrame(
    {'first_columns': [1,2,3,4,],
     'second_columns': [10, 20, 30, 40,],
     }
)

st.write(df)

## display numpy array

st.write(np.random.rand(1,7))
st.write(np.array([1,2,3,4]))

## ------------------------------ MAGIC -------------------------------- ##
st.write("Magic Commands")

df1 = pd.DataFrame({
    'col1': [1,2,3,4,],
})

df1
a = "A is my best :sunglasses"
a

## ----- Text elements -----

st.code('''
        st.markdown
        st.title
        st.header
        st.subheader
        st.text
        st.caption
        st.code
        st.latex        
''', language='python')

