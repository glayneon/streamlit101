import streamlit as st
import pandas as pd

if __name__ == "__main__":
    st.set_page_config(page_title="Stateful App", layout="centered")
    st.title("Stateful apps")

    st.write("Here is the session state: ")
    st.write(st.session_state)
    st.button("Update state")

    # set the value using the key-value syntanx
    if "key" not in st.session_state:
        st.session_state["key"] = "test01"

    # set the value using the attritube syntanx
    if "attribute" not in st.session_state:
        st.session_state.attribute = "test02"

    # Read value from session state
    if st.session_state["key"]:
        st.write(f"Reading with key-value {st.session_state['key']}")

    if st.session_state.attribute:
        st.write(
            f"Reading with the attribute syntax: {st.session_state.attribute}"
        )

    # Update values in state
    st.session_state["key"] = "new value"
    st.session_state.attribute = "updated value"

    # Delete item in state
    del st.session_state["key"]
    # del st.session_state.attribute
