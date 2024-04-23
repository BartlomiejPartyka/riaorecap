import streamlit as st

st.title("Quizy")
st.subheader("  ")

pages_names = ['Część 1', 'Część 2']
page = st.radio('Wybierz zakres materiału', pages_names, index=None)

if page == 'Część 1':
    st.write("Pierwszaa")
elif page == 'Część 2':
    st.write("drugaaa")
