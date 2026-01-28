"""
HOUSE PRICE PREDICTION WEB GUI
===============================
Student: Ogah Victor (22CG031902)
Algorithm: Random Forest Regressor
Framework: Streamlit
Model Persistence: Joblib
"""

import streamlit as st
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .header {
        color: white;
        text-align: center;
        padding: 2rem;
        border-radius: 10px;
        background: rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }
    .prediction-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        margin: 2rem 0;
    }
    .info-box {
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD MODEL
# ============================================================================
@st.cache_resource
def load_model():
    """Load the trained Random Forest model from disk"""
    try:
        # Try loading from model directory
        model_path = Path("model/house_price_model.pkl")
        if not model_path.exists():
            # Fallback paths
            model_path = Path("house_price_model.pkl")
        
        if model_path.exists():
            model = joblib.load(model_path)
            return model, True
        else:
            return None, False
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, False

# ============================================================================
# FEATURE INFORMATION FOR EXAM PREP
# ============================================================================
FEATURE_INFO = {
    'OverallQual': {
        'description': 'Overall Quality Rating (1-10)',
        'range': (1, 10),
        'type': 'integer',
        'exam_note': 'Rating scale where 10 is excellent quality'
    },
    'GrLivArea': {
        'description': 'Above Ground Living Area (sq ft)',
        'range': (300, 5000),
        'type': 'integer',
        'exam_note': 'Larger homes typically cost more'
    },
    'TotalBsmtSF': {
        'description': 'Total Basement Area (sq ft)',
        'range': (0, 6000),
        'type': 'integer',
        'exam_note': 'Basement space adds value'
    },
    'GarageCars': {
        'description': 'Number of Cars Garage Can Hold',
        'range': (0, 5),
        'type': 'integer',
        'exam_note': 'More garage space correlates with house size'
    },
    'YearBuilt': {
        'description': 'Year House Was Built',
        'range': (1872, 2010),
        'type': 'integer',
        'exam_note': 'Newer homes tend to be more expensive'
    },
    'FullBath': {
        'description': 'Number of Full Bathrooms',
        'range': (0, 5),
        'type': 'integer',
        'exam_note': 'More bathrooms increase property value'
    }
}

# ============================================================================
# MAIN APPLICATION
# ============================================================================
def main():
    # Title and Description
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title("🏠 House Price Prediction System")
    st.markdown("**Powered by Random Forest Machine Learning Model**")
    st.markdown("""
        <p style="color: white; text-align: center; margin-top: 1rem;">
        Predict house prices based on 6 key features using an advanced ML algorithm
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Load model
    model, model_loaded = load_model()
    
    if not model_loaded:
        st.error("⚠️ ERROR: Model file not found. Please ensure 'house_price_model.pkl' is in the model directory.")
        st.info("""
        Steps to fix:
        1. Run the model_building.ipynb notebook first
        2. Ensure house_price_model.pkl is saved in the model/ folder
        3. Redeploy the app
        """)
        return
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    # ========================================================================
    # LEFT COLUMN: INPUT FORM
    # ========================================================================
    with col1:
        st.subheader("📊 Enter House Features")
        st.markdown('<div class="info-box">Fill in the details below to get a price prediction</div>', unsafe_allow_html=True)
        
        # Create input fields
        inputs = {}
        
        # Row 1: Quality and Living Area
        col_a, col_b = st.columns(2)
        with col_a:
            inputs['OverallQual'] = st.slider(
                label="Overall Quality (1-10)",
                min_value=1,
                max_value=10,
                value=7,
                step=1,
                help=FEATURE_INFO['OverallQual']['exam_note']
            )
        with col_b:
            inputs['GrLivArea'] = st.number_input(
                label="Above Ground Living Area (sq ft)",
                min_value=300,
                max_value=5000,
                value=2000,
                step=100,
                help=FEATURE_INFO['GrLivArea']['exam_note']
            )
        
        # Row 2: Basement and Garage
        col_c, col_d = st.columns(2)
        with col_c:
            inputs['TotalBsmtSF'] = st.number_input(
                label="Total Basement Area (sq ft)",
                min_value=0,
                max_value=6000,
                value=1000,
                step=100,
                help=FEATURE_INFO['TotalBsmtSF']['exam_note']
            )
        with col_d:
            inputs['GarageCars'] = st.slider(
                label="Garage Capacity (cars)",
                min_value=0,
                max_value=5,
                value=2,
                step=1,
                help=FEATURE_INFO['GarageCars']['exam_note']
            )
        
        # Row 3: Year Built and Bathrooms
        col_e, col_f = st.columns(2)
        with col_e:
            inputs['YearBuilt'] = st.slider(
                label="Year Built",
                min_value=1872,
                max_value=2010,
                value=2000,
                step=1,
                help=FEATURE_INFO['YearBuilt']['exam_note']
            )
        with col_f:
            inputs['FullBath'] = st.slider(
                label="Full Bathrooms",
                min_value=0,
                max_value=5,
                value=2,
                step=1,
                help=FEATURE_INFO['FullBath']['exam_note']
            )
        
        # Prediction Button
        st.markdown("")
        predict_button = st.button(
            "🎯 Predict Price",
            use_container_width=True,
            type="primary"
        )
        
        # ====================================================================
        # MAKE PREDICTION
        # ====================================================================
        if predict_button:
            try:
                # Prepare input data
                feature_order = ['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'GarageCars', 'YearBuilt', 'FullBath']
                X_input = np.array([[inputs[feature] for feature in feature_order]])
                
                # Make prediction
                predicted_price = model.predict(X_input)[0]
                
                # Display prediction with styling
                st.markdown(f'<div class="prediction-box">💰 ${predicted_price:,.2f}</div>', unsafe_allow_html=True)
                
                # Display detailed breakdown
                st.success("✓ Prediction Generated Successfully!")
                
            except Exception as e:
                st.error(f"Error making prediction: {e}")
    
    # ========================================================================
    # RIGHT COLUMN: INFO & GUIDE
    # ========================================================================
    with col2:
        # Model Information
        st.subheader("📚 Model Information")
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Algorithm:** Random Forest Regressor
        
        **Features Used:** 6 out of 9 recommended
        
        **Model Type:** Regression
        
        **Persistence:** Joblib (.pkl)
        
        **Performance:** ~85% R² on test data
        
        **Training Samples:** 1460
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quick Tips
        st.subheader("💡 Quick Tips")
        st.markdown("""
        - **Quality**: Scale 1-10, affects price significantly
        - **Living Area**: Larger homes command higher prices
        - **Year Built**: Newer homes tend to be more expensive
        - **Bathrooms**: Additional bathrooms increase value
        """)
        
        # About Section
        st.subheader("👤 About")
        st.markdown("""
        **Student:** Ogah Victor  
        **Matric No:** 22CG031902  
        **Course:** CSC 415  
        **Institution:** Covenant University
        """)

# ============================================================================
# FOOTER WITH EXAM NOTES
# ============================================================================
def show_footer():
    st.markdown("""
    ---
    **📝 EXAM PREPARATION NOTES:**
    
    **Random Forest Key Concepts:**
    - Ensemble method combining multiple decision trees
    - Reduces overfitting through averaging predictions
    - Feature importance shows which inputs matter most
    - Hyperparameters: n_estimators, max_depth, min_samples_split
    
    **Regression Metrics Explained:**
    - **MAE**: Average absolute prediction error (easy to interpret)
    - **RMSE**: Penalizes large errors more than MAE
    - **R² Score**: Proportion of variance explained (0-1 scale)
    
    **Model Persistence:**
    - Joblib serializes scikit-learn models efficiently
    - Can load trained model without retraining
    - Faster and more reliable than pickle for NumPy arrays
    """)

# ============================================================================
# RUN APPLICATION
# ============================================================================
if __name__ == "__main__":
    main()
    show_footer()
