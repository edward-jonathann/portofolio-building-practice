import streamlit as st

def tampilkan():
    # Custom CSS for dropdown/buttons (white text on dark backgrounds)
    st.markdown("""
    <style>
        /* Dropdown text color */
        .stSelectbox label, .stSelectbox div[data-baseweb="select"] {
            color: white !important;
        }
        /* Button text color */
        .stButton>button {
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Project dropdown (list of projects)
    projects = {
        "Sales Forecast": {
            "description": "Time-series model to predict revenue using ARIMA and Python.",
            "skills": "Python, Pandas, Statsmodels",
            "link": "https://github.com/your-repo1"
        },
        "Image Classifier": {
            "description": "CNN model to classify CIFAR-10 images with TensorFlow.",
            "skills": "Python, TensorFlow, Computer Vision",
            "link": "https://github.com/your-repo2"
        },
        "Customer Segmentation": {
            "description": "Clustering analysis for marketing strategies using K-Means.",
            "skills": "Python, Scikit-learn, PCA",
            "link": "https://github.com/your-repo3"
        }
    }
    
    selected_project = st.selectbox(
        "Select a project to view details:",
        options=list(projects.keys()),
        format_func=lambda x: f"📌 {x}"  # Add icon to dropdown items
    )
    
    # Display selected project details
    with st.container(border=True):
        st.subheader(f"**{selected_project}**")
        st.markdown(f"**Description**: {projects[selected_project]['description']}")
        st.markdown(f"**Skills**: `{projects[selected_project]['skills']}`")
        
        # Interactive buttons (with white text)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("View Code ↗", key=f"code_{selected_project}"):
                st.markdown(f"[GitHub Link]({projects[selected_project]['link']})")
                st.balloons()
        with col2:
            if st.button("See Demo ↗", key=f"demo_{selected_project}"):
                st.write("Demo loading...")  # Replace with actual demo link

    # Overview of all projects (collapsible)
    with st.expander("📋 **Quick Overview of All Projects**", expanded=True):
        for project, details in projects.items():
            st.markdown(f"""
            - **{project}**: {details['description']}  
              *(Skills: {details['skills']})*
            """)