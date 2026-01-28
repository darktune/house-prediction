# House Price Prediction System

**Student:** Ogah Victor (22CG031902)  
**Course:** CSC 415 - AI/ML Project  
**Institution:** Covenant University  
**Submission Deadline:** January 22, 2026

## 🎯 Project Overview

A machine learning system that predicts house prices using Random Forest regression on 6 key features from the House Prices dataset.

## 📋 Project Components

### Part A: Model Development
- **File:** `model/model_building.ipynb`
- **Language:** Python (Google Colab)
- **Algorithm:** Random Forest Regressor
- **Features Used:** 6 out of 9 recommended
  1. OverallQual (Overall quality 1-10)
  2. GrLivArea (Above ground living area)
  3. TotalBsmtSF (Total basement area)
  4. GarageCars (Garage capacity)
  5. YearBuilt (Year built)
  6. FullBath (Number of bathrooms)

**What's Included:**
- Data preprocessing (missing values, feature selection)
- Train/test split (80/20)
- Model training and evaluation
- Regression metrics: MAE, MSE, RMSE, R²
- Model persistence using joblib
- Feature importance analysis

### Part B: Web GUI Application
- **File:** `app.py`
- **Framework:** Streamlit
- **Features:**
  - User-friendly input form
  - Real-time price predictions
  - Feature information and exam notes
  - Model performance metrics display

### Part C: GitHub Submission
```
/HousePrice_Project_OgahVictor_22CG031902/
├── app.py
├── requirements.txt
├── HousePrice_hosted_webGUI_link.txt
├── README.md
├── /model/
│   ├── model_building.ipynb
│   └── house_price_model.pkl (generated after running notebook)
├── /templates/
└── /static/
```

### Part D: Deployment
- **Platform:** Render.com
- **Framework:** Streamlit
- **Model Storage:** joblib (.pkl format)

## 🚀 How to Use

### Step 1: Train Model in Google Colab

1. Open `model/model_building.ipynb`
2. Upload to Google Colab
3. Run all cells sequentially
4. Download `house_price_model.pkl` and place in `model/` folder

### Step 2: Run Web Application Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

App will open at `http://localhost:8501`

### Step 3: Deploy to Render

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Render:**
   - Visit https://render.com
   - Create new Web Service
   - Connect your GitHub repository
   - Set Build Command: `pip install -r requirements.txt`
   - Set Start Command: `streamlit run app.py --server.port=10000`
   - Deploy!

3. **Update Submission File:**
   - Copy live URL from Render
   - Update `HousePrice_hosted_webGUI_link.txt`

## 📊 Model Performance

**Test Set Metrics:**
- MAE (Mean Absolute Error): ~$22,000
- RMSE (Root Mean Squared Error): ~$30,000
- R² Score: ~0.85 (explains 85% of price variance)

## 🎓 Key Concepts for Exam

### Random Forest Algorithm
- **Ensemble method** combining multiple decision trees
- Each tree makes a prediction, final result is the average
- **Advantages:** Handles non-linear relationships, resistant to outliers
- **Hyperparameters:** n_estimators (100), max_depth (20)

### Regression Metrics
- **MAE:** Average absolute error, easy to interpret
- **MSE:** Mean squared error, penalizes large errors
- **RMSE:** Square root of MSE, in same units as target
- **R²:** Proportion of variance explained (0-1 scale)

### Model Persistence
- **Joblib:** Serializes scikit-learn models efficiently
- **Advantages over pickle:** Faster, better compression
- **Usage:** `joblib.dump()` to save, `joblib.load()` to load

### Data Preprocessing Steps
1. **Handle missing values:** Fill with median
2. **Feature selection:** Choose 6 most predictive features
3. **Encoding:** Not needed (all features are numerical)
4. **Scaling:** Not required for Random Forest

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Streamlit web application |
| `requirements.txt` | Python dependencies |
| `model_building.ipynb` | Training notebook for Google Colab |
| `house_price_model.pkl` | Saved trained model |
| `HousePrice_hosted_webGUI_link.txt` | Submission information |

## 🔧 Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- joblib
- streamlit

## ⚠️ Troubleshooting

**Issue:** Model file not found
- **Solution:** Ensure you've run the notebook and downloaded the .pkl file

**Issue:** Streamlit not found
- **Solution:** `pip install streamlit`

**Issue:** Prediction returns error
- **Solution:** Check that all 6 input fields are filled

## 📚 Study Guide for Exam

### Must Know:
1. **What is Random Forest?** Ensemble of decision trees
2. **Why 6 features?** High correlation with price, minimal missing data
3. **What is R²?** Shows how much variance the model explains
4. **How to save model?** Using joblib.dump()
5. **How to load model?** Using joblib.load()

### Common Exam Questions:
- Q: What type of problem is this? A: Regression (predicting continuous values)
- Q: Why not use linear regression? A: House prices have non-linear relationships
- Q: What's overfitting? A: Model memorizes training data instead of generalizing
- Q: What does feature importance show? A: Which inputs affect predictions most

## 📄 License

Academic project for Covenant University CSC 415 course.

---

**Last Updated:** January 22, 2026  
**Status:** Ready for Submission & Deployment
