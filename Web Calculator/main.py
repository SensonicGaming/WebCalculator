import streamlit as st

st.set_page_config(page_title="Web Calculator", initial_sidebar_state="collapsed")
if __name__ == "__main__":
    st.markdown("<h2 style='text-align: center;'>Choose Any</h2>", unsafe_allow_html=True)
    st.page_link('pages/calc.py', label="Simple Calculator")