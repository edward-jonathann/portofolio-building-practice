import streamlit as st

def tampilkan_kontak():
    st.title("Get in Touch")

    # Interactive contact form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        
        if submitted:
            st.success("Message sent! (Note: This is only a trial!)")
            st.balloons()

    # Social links
    st.markdown("""
    📧 Email: `edjonathannnnn@gmail.com`  
    🔗 [LinkedIn](https://www.linkedin.com/in/edward-jonathann/) | [GitHub](https://github.com/edward-jonathann)
    """)