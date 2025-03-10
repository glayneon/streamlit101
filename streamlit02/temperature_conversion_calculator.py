import streamlit as st


@st.cache_data
def cel_to_faren(num):
    return (9 / 5 * num) + 32


@st.cache_data
def faren_to_kelvin(num):
    return ((num - 32) * 5 / 9) + 273.15


@st.cache_data
def kelvin_to_faren(num):
    return (num - 273.15) * 9 / 5 + 32


@st.cache_data
def faren_to_cel(num):
    return (num - 32) * 5 / 9


def convert_cel():
    cel = st.session_state["celsius"]
    faren = cel_to_faren(cel)
    kelvin = faren_to_kelvin(faren)

    st.session_state["farenheit"] = faren
    st.session_state["kelvin"] = kelvin


def convert_far():
    faren = st.session_state["farenheit"]
    kelvin = faren_to_kelvin(faren)
    cel = faren_to_cel(faren)

    st.session_state["kelvin"] = kelvin
    st.session_state["celsius"] = cel


def convert_kel():
    kelvin = st.session_state["kelvin"]
    faren = kelvin_to_faren(kelvin)
    cel = kelvin - 273.15

    st.session_state["farenheit"] = faren
    st.session_state["celsius"] = cel


def add_celsius():
    if "add_cel" in st.session_state:
        celsius = st.session_state["celsius"]
        add_val = st.session_state["add_cel"]

        st.session_state["celsius"] = celsius + add_val
        convert_cel()


def zero_cel():
    if "freezing" in st.session_state:
        st.session_state["celsius"] = 0
        convert_cel()


def boiling():
    if "boiling" in st.session_state:
        st.session_state["celsius"] = 100
        convert_cel()


def abs_zero():
    if "abs_zero" in st.session_state:
        st.session_state["celsius"] = float(-273.15)
        convert_cel()


if __name__ == "__main__":
    st.set_page_config("Temperature Convsersion Calculator")

    st.title("Exercise: State Management")
    st.subheader("Templerature conversion")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.number_input(
            "Celsius", 0.00, 1000.0, key="celsius", on_change=convert_cel
        )
        st.number_input("Add to Celsius", 0, key="add_cel")

        st.button("Add", type="primary", on_click=add_celsius)

    with col2:
        farenheit = st.number_input(
            "Farenheit", 32.00, key="farenheit", on_change=convert_far
        )

    with col3:
        kelvin = st.number_input(
            "Kelvin", 273.15, key="kelvin", on_change=convert_kel
        )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button(
            "Freezing Point water",
            type="secondary",
            key="freezing",
            on_click=zero_cel,
        )

    with c2:
        st.button(
            "Boiling point of water",
            type="secondary",
            key="boiling",
            on_click=boiling,
        )

    with c3:
        st.button(
            "Absolute zero",
            type="secondary",
            key="abs_zero",
            on_click=abs_zero,
        )

    st.write(st.session_state)
