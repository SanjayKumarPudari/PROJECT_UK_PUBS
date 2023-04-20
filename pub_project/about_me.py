import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("Personal info")

st.header('Sanjay Kumar Pudari')
st.subheader('**:blue[Data Science Intern:sunglasses:]**')
st.subheader(":red[Innomatics Research labs]")

btn_click = st.button("To know more details about me...click here")
if btn_click == True:
    st.subheader("wow! I'm glad that.. you wanna know about me :heart_eyes:")
    st.caption('**I am a recent master graduate and data enthusiastic who loves to explore data and do statistical problems and interested in Data Science**')
    
    st.subheader('Find my linkedin and Github profiles here :point_down:')
   

    st.markdown('**Linkedin : www.linkedin.com/in/sanjay-kumar-318464210**')
    st.markdown('**GitHub: https://github.com/SanjayKumarPudari**')

    

