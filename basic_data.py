import streamlit as st
import pandas as pd

if "attendance" not in st.session_state:
    st.session_state.attendance = set()


def take_attendance():
    if st.session_state.name in st.session_state.attendance:
        st.info(f"{st.session_state.name} has already been counted.")
    else:
        st.session_state.attendance.add(st.session_state.name)
        st.info(f"{st.session_state.name} Is here.")
        st.info(f"{st.session_state.attendance} are here")


with st.form(key="my_form"):
    st.text_input("Name", key="name")
    st.form_submit_button("I'm here!", on_click=take_attendance)
data = pd.read_csv("maddennfl24fullplayerratings.csv")
st.write(data)