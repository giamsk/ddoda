import streamlit as st
st.title("카운트")
count = 0
if st.button("증가"):
    count = count+1
st.markdown(f"## 현제숫자: '(count)'")













