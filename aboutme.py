import streamlit as st
import time
from PIL import Image

def tampilkan_tentang():
    st.title("About Me")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("assets/profile.jpg", width=150)  # Replace with your photo

    with col2:
        st.write("""
        **Who I Am**  
        Passionate about turning data into insights.  
        Skills: Python, TensorFlow, SQL, Streamlit.
        """)

    # Skills expander
    with st.expander("🔍 See my skills in detail"):
        st.progress(80, text="Python")
        st.progress(70, text="Machine Learning")
        st.progress(60, text="Data Visualization")

    # PDF Resume Viewer
    st.divider()
    st.subheader("📄 Resume")
    with open("assets/resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Your_Name_Resume.pdf",
            mime="application/pdf"
        )
        st.write("Or view inline:")
        st.pdf("assets/resume.pdf")  # Displays PDF in the app