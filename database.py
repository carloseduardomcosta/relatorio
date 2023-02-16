import streamlit as st
st.write('Olá, bem-vindo KADU!!')
st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')