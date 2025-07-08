import streamlit as st
import time

def tampilkan():
    st.title("Hi, I'm Edward Jonathan")
    st.subheader("Data Scientist | ML Engineer")

    # Interactive button
    if st.button("👉 Click for a fun fact!"):
        with st.spinner("Generating..."):
            time.sleep(1)
            st.success("Ironically, the fear of long words is called Hippopotomonstrosesquippedaliophobia. The 36-letter word was first used in the first century BCE to criticise writers with an unreasonable penchant for long words.")

    st.markdown("""
    Welcome to my portfolio! Here’s what you’ll find:
    - **About Me**: My background and skills.
    - **Projects**: My work in ML/data science.
    - **Contact**: Let’s connect!
    """)