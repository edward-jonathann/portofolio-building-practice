import streamlit as st

def tampilkan():
    # Custom CSS for dropdown/buttons (white text on dark backgrounds)
    st.markdown("""
    <style>
        .stSelectbox label, .stSelectbox div[data-baseweb="select"] {
            color: white !important;
        }
        .stButton>button {
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Project data
    projects = {
        "Customer Segmentation": {
            "description": "A Customer Segmentation analysis using RFM methodology to group customers based on their behavior.",
            "skills": "Python, Pandas, PowerBI",
            "link": "https://github.com/edward-jonathann/shoppingstore",
            "demo": None
        },
        "Customer Clustering": {
            "description": "K-means clustering with PCA and t-SNE to identify customer segments.",
            "skills": "Python, K-means, PCA, t-SNE",
            "link": "https://github.com/your-repo2",
            "demo": None
        },
        "Churn Analysis": {
            "description": """This project analyzes customer churn for Speedy Telco, a fictional telecommunications company that provides home phone and internet services to
            7,043 customers in California (Q3 data). The goal is to identify patterns and drivers
            behind customer attrition and provide actionable recommendations to improve
            retention.""",
            "skills": "Python, Pandas, PowerBI, Seaborn, Matplotlib",
            "link": "https://github.com/edward-jonathann/telco-churn-prediction",
            "demo": None
        },
        "Flight Price Prediction": {
            "description": """The goal of this project was to see if flight ticket prices could be predicted accurately using data and machine learning. 
            The dataset contained over 300,000 flight booking records from India's top six metro cities. 
            After cleaning and feature engineering, four ML models were tested Random Forest performed best with 98.2% accuracy and 12% MAPE. 
            This method can be applied beyond flights, e.g., in retail pricing or logistics planning.""",
            "skills": "Python, Scikit-learn, XGBoost, CatBoost",
            "link": "https://github.com/edward-jonathann/flight-price-prediction",
            "demo": "https://flight-price-predictionv2-edwardjonathan.streamlit.app/"
        },
        "Surge Pricing Classification Prediction": {
            "description": """This project focuses on building a Machine Learning model to predict surge pricing in ride-hailing services. Surge pricing happens when demand for rides exceeds supply, leading to fare increases 
            but for customers it often feels unpredictable.
            By analyzing historical ride data, the goal is to develop a predictive system that identifies when surge is likely to occur. This helps businesses optimize dynamic pricing while also giving riders more transparency.""",
            "skills": "Python, Scikit-learn, RandomForest Classifier, GradientBoosting Classifier, KNN",
            "link": "https://github.com/edward-jonathann/price-surge-classification",
            "demo": "https://price-surge-classification-edwardjonathanv2.streamlit.app/"
        }
    }

    # Overview of all projects (TOP)
    with st.expander("📋 Quick Overview of All Projects", expanded=True):
        for project, details in projects.items():
            st.markdown(f"- **{project}**: {details['description']} *(Skills: {details['skills']})*")

    # Dropdown selection
    selected_project = st.selectbox(
        "Select a project to view details:",
        options=list(projects.keys()),
        format_func=lambda x: f"📌 {x}"
    )
    
    # Project details
    st.subheader(selected_project)
    st.markdown(f"**Description:** {projects[selected_project]['description']}")
    st.markdown(f"**Skills:** `{projects[selected_project]['skills']}`")
    
    # Buttons for Code and Demo
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("View Code ↗", projects[selected_project]['link'])
    with col2:
        demo_url = projects[selected_project].get("demo")
        if demo_url:
            st.link_button("See Demo ↗", demo_url)
        else:
            st.warning("No Demo available yet!")

# Run function
if __name__ == "__main__":
    tampilkan()
