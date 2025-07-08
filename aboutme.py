import streamlit as st
import time
import base64

def tampilkan_tentang():
    st.title("About Edward Jonathan!")

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

    try:
        with open("assets/resume.pdf", "rb") as file:
            # Download Button
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="Your_Name_Resume.pdf",
                mime="application/pdf"
            )
        
        # Show PDF inline
        with open("assets/resume.pdf", "rb") as file:
            base64_pdf = base64.b64encode(file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
            st.markdown("Or view inline:")
            st.markdown(pdf_display, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("Error: Resume file not found at 'assets/resume.pdf'")
