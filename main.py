import streamlit as st

# # Custom CSS for white/grey theme
# st.markdown("""
# <style>
#     /* Main background */
#     [data-testid="stAppViewContainer"] {
#         background-color: #f8f9fa;
#     }
    
#     /* All text to dark */
#     body, h1, h2, h3, h4, h5, h6, p, div, span {
#         color: #212529 !important;
#     }
    
#     /* Containers (cards) */
#     .stContainer {
#         background-color: white;
#         border-radius: 10px;
#         padding: 15px;
#         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
#         margin-bottom: 20px;
#     }
    
#     /* Buttons */
#     .stButton>button {
#         background-color: #e9ecef !important;
#         color: #212529 !important;
#         border: 1px solid #dee2e6 !important;
#     }
#     .stButton>button:hover {
#         background-color: #dee2e6 !important;
#     }
    
#     /* Sidebar */
#     [data-testid="stSidebar"] {
#         background-color: #f1f3f5 !important;
#     }
            
#     /* Dropdown text color */
#     .stSelectbox label, .stSelectbox div[data-baseweb="select"] {
#         color: white !important;
#     }
#     /* Button text color */
#     .stButton>button {
#         color: white !important;
#     }
# </style>
# """, unsafe_allow_html=True)

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