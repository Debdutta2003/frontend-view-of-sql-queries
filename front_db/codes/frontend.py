import streamlit as st # type: ignore
import w
import oracledb

s=st.text_input('enter sql query here')


if st.button('click me'):
     
     Lst=w.select_operation(s)

     for i in Lst:
         st.markdown(i)