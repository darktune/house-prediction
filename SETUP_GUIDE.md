# SETUP & DEPLOYMENT GUIDE
## House Price Prediction System

**Complete step-by-step instructions for Ogah Victor**

---

## ⚡ QUICK START (5 minutes)

### What You Just Got:
✅ Complete project structure  
✅ Jupyter notebook for model training (Google Colab)  
✅ Streamlit web app ready to deploy  
✅ All dependencies configured  
✅ Comprehensive documentation for exam prep  

---

## 📋 STEP-BY-STEP DEPLOYMENT

### PHASE 1: TRAIN THE MODEL (Google Colab - 15 minutes)

1. **Open Google Colab**
   - Go to https://colab.research.google.com
   - Click "Upload" tab
   - Upload: `model/model_building.ipynb`

2. **Run All Cells**
   - Runtime → Run all
   - Wait for completion (should take 2-3 minutes)
   - Watch for green checkmarks

3. **Download Model File**
   - After training completes, you'll see:
     ```
     ✓ Model saved successfully at: /content/house_price_model.pkl
     ```
   - Download this file
   - Save to local folder: `model/house_price_model.pkl`

4. **Verify Model Works**
   - Last cell shows test results
   - You should see metrics like:
     ```
     Testing Set: R² = 0.85 (approximately)
     RMSE = ~$30,000
     ```

### PHASE 2: TEST LOCALLY (5 minutes)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run App**
   ```bash
   streamlit run app.py
   ```

3. **Test Features**
   - Open browser to `http://localhost:8501`
   - Fill in sample values:
     - Overall Quality: 7
     - Living Area: 2000 sq ft
     - Basement Area: 1000 sq ft
     - Garage Cars: 2
     - Year Built: 2000
     - Bathrooms: 2
   - Click "Predict Price"
   - Should get prediction like "$250,000"

### PHASE 3: GITHUB SETUP (5 minutes)

1. **Create GitHub Account** (if you don't have one)
   - Go to https://github.com
   - Sign up with email

2. **Create Repository**
   - Click "New repository"
   - Name: `HousePrice_Project_OgahVictor_22CG031902`
   - Make it Public
   - Initialize with README
   - Create repository

3. **Clone to Your Computer**
   ```bash
   git clone https://github.com/YOUR_USERNAME/HousePrice_Project_OgahVictor_22CG031902.git
   ```

4. **Copy Project Files**
   - Copy all your project files into the cloned folder
   - Should have:
     ```
     app.py
     requirements.txt
     README.md
     HousePrice_hosted_webGUI_link.txt
     /model/
       ├── model_building.ipynb
       └── house_price_model.pkl
     /templates/
     /static/
     ```

5. **Push to GitHub**
   ```bash
   cd HousePrice_Project_OgahVictor_22CG031902
   git add .
   git commit -m "Initial project submission"
   git push origin main
   ```

### PHASE 4: DEPLOY ON RENDER (10 minutes)

1. **Sign Up on Render**
   - Go to https://render.com
   - Click "Sign up"
   - Use GitHub account for easy authentication

2. **Create Web Service**
   - Dashboard → New → Web Service
   - Connect your GitHub repository
   - Select: `HousePrice_Project_OgahVictor_22CG031902`

3. **Configure Service**
   ```
   Name: house-price-predictor
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run app.py --server.port=10000
   Instance Type: Free (sufficient for this project)
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (3-5 minutes)
   - Render will show live URL like:
     ```
     https://house-price-predictor.onrender.com
     ```

5. **Test Live Application**
   - Visit the URL
   - Fill in test values
   - Click "Predict Price"
   - Should work exactly like local version

### PHASE 5: FINAL SUBMISSION (5 minutes)

1. **Update Submission File**
   - Edit: `HousePrice_hosted_webGUI_link.txt`
   - Fill in:
     ```
     Name: Ogah Victor
     Matric Number: 22CG031902
     Machine Learning Algorithm Used: Random Forest Regressor
     Model Persistence Method: Joblib (.pkl)
     Live URL: https://house-price-predictor.onrender.com
     GitHub Link: https://github.com/YOUR_USERNAME/HousePrice_Project_OgahVictor_22CG031902
     ```

2. **Create Submission Package**
   - Ensure folder contains:
     ```
     /HousePrice_Project_OgahVictor_22CG031902/
     ├── app.py
     ├── requirements.txt
     ├── HousePrice_hosted_webGUI_link.txt
     ├── README.md
     ├── /model/
     │   ├── model_building.ipynb
     │   └── house_price_model.pkl
     ├── /templates/
     └── /static/
     ```

3. **Upload to Scorac**
   - Go to your course submission portal
   - Upload the complete folder
   - Submit before deadline: **January 22, 2026, 11:59 PM**

---

## ✅ VERIFICATION CHECKLIST

Before final submission, verify:

- [ ] Model file exists: `model/house_price_model.pkl`
- [ ] Local app runs: `streamlit run app.py`
- [ ] Live URL works: Can access in browser
- [ ] Predictions work: Get numerical output
- [ ] GitHub has all files
- [ ] Submission file updated with correct URLs
- [ ] README.md explains everything
- [ ] requirements.txt has all dependencies

---

## 🔧 TROUBLESHOOTING

### Problem: "ModuleNotFoundError"
```bash
pip install pandas numpy scikit-learn joblib streamlit
```

### Problem: Model not loading on Render
- Verify `house_price_model.pkl` is in repository
- Check file size (should be ~10-20MB)
- Redeploy from Render dashboard

### Problem: Predictions give error
- Check all 6 input fields are filled
- Verify input ranges are reasonable
- Check browser console for error messages

### Problem: Git push fails
- Ensure you're in correct directory
- Use: `git status` to check changes
- Add large files with Git LFS if needed

---

## 🎓 EXAM PREPARATION SUMMARY

### Topics Covered in This Project:
1. **Regression** - Predicting continuous values (prices)
2. **Random Forest** - Ensemble of decision trees
3. **Model Evaluation** - MAE, MSE, RMSE, R² metrics
4. **Data Preprocessing** - Handling missing values, feature selection
5. **Model Persistence** - Saving/loading with joblib
6. **Web Deployment** - Using Streamlit and cloud platforms

### Key Formulas to Memorize:
```
MAE = (1/n) × Σ|actual - predicted|
RMSE = √[MSE] = √[(1/n) × Σ(actual - predicted)²]
R² = 1 - (SS_residual / SS_total)
```

### Vocabulary:
- **Features (X):** Input variables (the 6 selected)
- **Target (y):** Output variable (SalePrice)
- **Train/Test Split:** Evaluate on unseen data
- **Overfitting:** Model memorizes data (bad)
- **Joblib:** Serialization for scikit-learn models

---

## 📞 QUICK REFERENCE

**Key Files:**
- `app.py` - Web interface (230 lines, well-commented)
- `model_building.ipynb` - Training pipeline (12 cells)
- `requirements.txt` - 5 dependencies

**Commands:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run app locally
streamlit run app.py

# Test model in Python
python -c "import joblib; m = joblib.load('model/house_price_model.pkl')"

# Check requirements installed
pip list | grep -E "pandas|numpy|scikit-learn|joblib|streamlit"
```

**URLs to Remember:**
- Google Colab: https://colab.research.google.com
- GitHub: https://github.com
- Render: https://render.com
- Streamlit Docs: https://docs.streamlit.io

---

## ⏰ TIMELINE

- **Now - 1 hour:** Train model on Google Colab
- **1-2 hours:** Test locally, push to GitHub
- **2-3 hours:** Deploy on Render
- **3-3.5 hours:** Update submission file, submit on Scorac

**Total Time:** ~3.5 hours for complete deployment

---

## 📝 NOTES FOR FUTURE REFERENCE

- Keep `house_price_model.pkl` in repository (needed for deployment)
- Update `HousePrice_hosted_webGUI_link.txt` with final URLs
- Save this guide for exam studying
- Review random forest and regression metrics before exam

---

**Good luck with your submission and exam!** 🎓

---
Generated on: January 22, 2026
For: Ogah Victor (22CG031902)
Course: CSC 415 - Covenant University
