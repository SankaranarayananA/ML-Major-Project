import streamlit as st
import sklearn
import joblib
model = joblib.load('Sentia')
st.title('Sentiment Analysis')
ip = st.text_input("Enter the Review")
op = model.predict([ip])
if st.button('Work'):
    st.title(op[0])

    
