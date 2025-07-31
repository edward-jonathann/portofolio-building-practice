import streamlit as st

st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title("Welcome to My Website!")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Main Page",
                        ["Overview", "About Me", "Projects", "Contact"])


if page == "Contact":
    import contact
    contact.tampilkan_kontak()
elif page == "About Me":
    import aboutme
    aboutme.tampilkan_tentang()
elif page == "Projects":
    import projects
    projects.tampilkan()
elif page == "Overview":
    import overview
    overview.tampilkan()