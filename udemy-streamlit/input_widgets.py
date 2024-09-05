import streamlit as st
import pandas as pd
# import numpy as np
import os

# load the data
df = pd.read_csv('tips.csv')

def display_data_random(df):
    sample = df.sample(5)
    return sample

# sidebar
side_bar = st.sidebar
side_bar.title('Input widgets')
side_bar.caption('Show input widgets')

with side_bar.expander('All input widgets'):
    st.code("""
            st.button('Message')
            st.input_text('Message')
""", language='Python')

# button widget
# columns
ratio = (0.5, 0.5)
col1, col2 = st.columns(ratio)

with col1:
    # st.markdown('---')
    st.header('Random 5 rows', divider=True)
    st.caption('Click on the button below to display the rows randomly')

    button = st.button('Display random 5 rows')
    if button:
        sample = display_data_random(df)
        st.dataframe(sample)

    # reset button
    button = False

# checkbox
with col2:
    # st.markdown('---')
    st.header('st.checkbox', divider=True)
    agree = st.checkbox('I agree to terms and conditions') # return bool
    st.write(f"checkbox status : {agree}")

    # radio button
    st.header('st.radio', divider=True)
    radio_button = st.radio("What is your favorite color ?",
                            ('White', 'Black', 'Pink', 'Red', "Blue"))
    st.write(f"Your favorite color : {radio_button}")

    # multiple checkbox

with st.container(border=True):
    st.info('What technologies you know')

    python = st.checkbox('Python')
    data_science = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    android = st.checkbox('Android')
    react = st.checkbox('React JS')
    java = st.checkbox('Core Java')
    javascript = st.checkbox('Java Script')

    tech_button = st.button('Submit')
    if tech_button:
        tech_dict = {
            'Python':python,
            'Data Science':data_science,
            'AI/ML':ai_ml,
            'Android':android,
            'React JS':react,
            'Core Java':java,
            'Java Script':javascript,
        }
        st.json(tech_dict)
        # for key in tech_dict:
        #     if tech_dict[key]:
        #         st.write(f"{key} is Enabled.")

# select box
st.header('st.selectbox', divider=True)
select_box = st.selectbox(
    'What skill you want to learn most? ',
    ('Java', 'Python', 'C', 'Go', 'JavaScript', 'React'))

st.write(f"You selectd : {select_box}")

# multiple select box
st.header('st.multiselect', divider=True)
options = st.multiselect(
    'What kind of movies you like ?',
    ['Comedy', 'Action', 'Sci-fi', 'Drama', 'Sexual', 'BBC', ]
    )

st.json(options)

# slider
st.header('Slider', divider=True)
loan = st.slider('What is loan amount you  are looking for ?', 0, 100000, 1000)
st.write(f"You requested {loan}")

# text, number, text_area, date inputs
st.header('st.text_input, st.number_input, st.date_input', divider=True)

with st.container(border=True):
    name = st.text_input('Enter your name.')
    age = st.number_input('Enter your age', min_value=0, max_value=100, value=25, step=1)
    describe = st.text_area('Description',height=150)
    dob = st.date_input('Select date of birth')

    submit_button = st.button("Submit", key='submit1')

    if submit_button:
        info = {
            "Name": name,
            "Age": age,
            "Birth": dob,
            "Description": describe,
        }
        st.json(info)


# file uploader
st.header('st.file_uploader', divider=True)

uploaded_file = st.file_uploader('Choose a file.')
save_button = st.button('save file', key='save file')
if save_button and uploaded_file is not None:
    with open(os.path.join("./save_folder", uploaded_file.name), 'wb') as file:
        file.write(uploaded_file.getbuffer())

    st.success('File uploaded successfully')
else:
    st.warning('Please select the file you want to upload.')