import streamlit as st
import pandas as pd
name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father name: ")
adr = st.text_area("Enter your text")
classdata = st.selectbox("Enter Your Class: ",(1,2,3,4,5,6,7,8,9,10))

button = st.button("Done")
if button :
    st.markdown(f"""
    name:{name}
    Father name :{fname}
    address :{adr}
    class ={classdata}""")