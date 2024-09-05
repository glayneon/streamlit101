import streamlit as st
import pandas as pd
import time

tips = pd.read_csv('tips.csv')
columns = tuple(tips.columns)

# sidebar
side_bar = st.sidebar
side_bar.write('# Hello World :sunglasses:')
side_bar.header('This is sidebar', divider=True)
side_bar.caption('elements that added in sidebar are pined to left')

# create widget selectbox
select_columns = side_bar.selectbox(
    "Select the column you want to display",
    columns
)

side_bar.success('You selected the column_name : {}'.format(select_columns))

## main
# st.write(columns)
st.header('Tips Dataframe', divider=True)
st.write(tips)

st.subheader('Value counts for Selected column')
# st.dataframe(tips.sort_values(by=select_columns, ascending=False))
st.dataframe(tips[select_columns].value_counts(ascending=False))

# layout columns
st.header('Columns: st.columns')
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('column-1')
    st.image('media/image.jpg')

with col2:
    st.subheader('column-2')
    st.dataframe(tips)

with col3:
    st.subheader('column-3')
    st.video('media/waterfalls.mp4')

# expander
st.header('Expander: st.expander')
with st.expander('Some explanation'):
    st.write("""
            This is the message in Expander
            OK. 
""")
    st.code("""
            # you create python code
            import streamlit as st
            st.expander(label='')
            st.write('something')
""", language='python')

# container
st.header('Container: st.container')
with st.container(height=500, border=True):
    st.write('You are inside the container')
    st.code("""
            # you create python code
            import streamlit as st
            st.expander(label='')
            st.write('something')
""", language='python')


# empty
st.header('Empty: st.empty')
placeholder = st.empty()
for i in range(1, 10):
    placeholder.write(f"### This message will disappear in {10-i} :sunglasses:")
    time.sleep(1)

placeholder.empty()