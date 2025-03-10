import streamlit as st
import math
st.set_page_config(page_title="Simple Calculator")

if 'currentValue' not in st.session_state:
    st.session_state.currentValue = ""

def updateValue(value):
    if "Error" in st.session_state.currentValue:
        resetValue()
    st.session_state.currentValue += value
    return value

def resetValue():
    st.session_state.currentValue = ""

def eraseValue():
    st.session_state.currentValue = str(st.session_state.currentValue)[0:-1]

def calculate():
    try:
        if "√" in st.session_state.currentValue:
            st.session_state.currentValue = str(st.session_state.currentValue).replace("√","math.sqrt(")+")"
            print(str(st.session_state.currentValue))
        st.session_state.currentValue = str(eval(st.session_state.currentValue))
    except Exception as e:
        print(str(e))
        st.session_state.currentValue = "Error"

if __name__ == '__main__':
    st.text_input("Current Input", value=st.session_state.currentValue, key="display", disabled=True)
    clear, sqrt, eq, backsp = st.columns(4)
    clear.button("C", on_click=resetValue)
    sqrt.button("√", on_click=updateValue, args=("√",))
    eq.button("=", on_click=calculate)
    backsp.button("⌫", on_click=eraseValue)

    col1, col2, col3, add = st.columns(4)
    add.button("\\+ ", on_click=updateValue, args=("+",))
    col1.button("1", on_click=updateValue, args=("1",))
    col2.button("2", on_click=updateValue, args=("2",))
    col3.button("3", on_click=updateValue, args=("3",))
    #====
    col4, col5, col6, sub = st.columns(4)
    col4.button("4", on_click=updateValue, args=("4",))
    col5.button("5", on_click=updateValue, args=("5",))
    col6.button("6", on_click=updateValue, args=("6",))
    sub.button("\\- ", on_click=updateValue, args=("-",))
    #=====
    col7, col8, col9, mult = st.columns(4)
    col7.button("7", on_click=updateValue, args=("7",))
    col8.button("8", on_click=updateValue, args=("8",))
    col9.button("9", on_click=updateValue, args=("9",))
    mult.button("x", on_click=updateValue, args=("*",))
    #=====
    blank1, col0, blank2, div = st.columns(4)
    col0.button("0", on_click=updateValue, args=("0",))
    div.button("÷", on_click=updateValue, args=("/",))
