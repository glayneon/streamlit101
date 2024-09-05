import streamlit as st

st.title("Streamlit101-Day11")

col1, col2 = st.columns(2)

# columns 1

col1.header('st.multiselecor', divider=True)

col1.write('# Today - Multiselector 😊')
col1.slider('Range', 0, 10, 5)

options = col1.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

col1.write(options)

# columns 2

col2.header('st.checkbox', divider=True)

col2.write('What would you like to order?')

icecream = col2.checkbox('Ice Cream')
coffee = col2.checkbox('Coffee')
cola = col2.checkbox('Cola')

if icecream:
    col2.write("Great! Here's some more 🍨")
elif coffee:
    col2.write("Okay, here's some coffee ☕")
elif cola:
    col2.write("Here you go 🥤")