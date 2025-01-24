import streamlit as st
st.title("Calculate the gross salary")
Basic = float(st.text_input("Enter the basic salary","10000.89"))

if st.button("Gross Salary") :
    HRA = (0.67*Basic) if Basic<10000 else (0.69*Basic) if Basic<=20000 else (0.73*Basic)
    DA = (0.73*Basic) if Basic<10000 else (0.76*Basic) if Basic<=20000 else (0.89*Basic)
    total= HRA+DA+Basic
    st.success(f"The Gross Salary is {total}")
    st.info(f"HRA : {HRA : .2f}")
    st.info(f"DA : {DA : .2f}")