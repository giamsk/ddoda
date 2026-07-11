import streamlit as st
st.title("카운트")

if 'count' not in st.session_state.count:
    st.session_state.count=0
if st.button("증가"):
    st.session_state.count+=1
st.markdown(f"## 현제숫자: '{st.session_state.count}'")













