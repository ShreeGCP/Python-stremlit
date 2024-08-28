import streamlit as st
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    #st.image("images/Shridhara.jpg",width=300)
    st.image("images/Shridhara.jpg")

with col2:
    st.title("Shridhara Devadiga")
    content = """ This is Shridhara Devadiga.I am a Python Developer. I have 8 years experiance in IT.
My Birth place is Maravanthe Kundapura Thaluk.
I am very much interested in Python Programming language \n
Never Ever Giveup....Good Things always takes time"""
    #st.write(content)
    st.info(content)
