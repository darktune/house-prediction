# 📚 HOUSE PRICE PREDICTION - EXAM STUDY GUIDE
## Quick Reference for Cramming

**Time to read through:** 15 minutes  
**Best time to review:** Night before exam

---

## 🎯 ONE-SENTENCE DEFINITIONS (Memorize These)

| Term | Definition |
|------|-----------|
| **Regression** | Predicting continuous numbers (prices, temperatures, etc) |
| **Classification** | Predicting categories (yes/no, A/B/C, etc) |
| **Random Forest** | Multiple decision trees voting together |
| **Overfitting** | Model memorizes training data (fails on new data) |
| **Feature** | Input variable (one of the 6: quality, size, etc) |
| **Target** | Output variable (what we predict: price) |
| **MAE** | Average error amount in dollars |
| **RMSE** | Error accounting for large mistakes more |
| **R²** | Percentage of price variation the model explains |
| **Joblib** | Way to save/load trained models |

---

## 📊 THIS PROJECT IN 30 SECONDS

**What:** Predict house prices using machine learning  
**How:** Train Random Forest on 6 features, deploy to web  
**Why:** Demonstrate ML regression, data preprocessing, web deployment  
**Result:** ~85% accuracy (R² = 0.85)  

---

## 🔢 THE 6 FEATURES (Know These!)

```
1. OverallQual (1-10)        → Quality rating
2. GrLivArea (sq ft)         → Living space size
3. TotalBsmtSF (sq ft)       → Basement space
4. GarageCars (0-5)          → How many cars fit
5. YearBuilt (1872-2010)     → Age of house
6. FullBath (0-5)            → Full bathrooms
```

**Why these 6?**
- Highest correlation with price
- Least missing data
- Easy to measure and understand

---

## 🌳 RANDOM FOREST ALGORITHM (Exam Favorite!)

### How It Works:
```
1. Train 100 decision trees
2. Each tree makes a prediction
3. Average all predictions = final answer
```

### Why It's Good:
✅ Handles complex patterns  
✅ Doesn't need feature scaling  
✅ Resistant to outliers  
✅ Shows feature importance  

### Hyperparameters We Used:
```python
n_estimators=100      # 100 trees
max_depth=20          # Each tree max 20 levels
min_samples_split=5   # Need 5 samples to split node
random_state=42       # Same results every time
```

### Decision Tree Basics:
```
                [OverallQual > 7?]
                     /          \
                  YES            NO
                  /                \
        [Area > 2000?]      [YearBuilt > 2000?]
           /      \              /        \
         ...     ...            ...      ...
```

---

## 📈 FOUR METRICS YOU NEED TO KNOW

### 1. MAE (Mean Absolute Error)
```
Formula: MAE = Average of |actual - predicted|
Units: Dollars ($)
Example: MAE = $22,000 means average prediction off by $22k
Best For: Easy to understand
```

### 2. MSE (Mean Squared Error)
```
Formula: MSE = Average of (actual - predicted)²
Units: Dollars squared ($²)
Why Squared: Penalizes big errors more than small ones
Problem: Hard to interpret (wrong units)
```

### 3. RMSE (Root Mean Squared Error) ⭐
```
Formula: RMSE = √MSE
Units: Dollars ($) - same as target!
Example: RMSE = $30,000 is typical error
Why: Best of both worlds - penalizes big errors + easy to interpret
```

### 4. R² (Coefficient of Determination) ⭐⭐
```
Formula: R² = 1 - (SS_residual / SS_total)
Range: 0 to 1 (higher is better)
Example: R² = 0.85 means model explains 85% of price variation
Interpretation:
  - 0.85 = Good (explains 85%)
  - 0.50 = Mediocre (explains 50%)
  - 0.30 = Poor (explains 30%)
```

---

## 🔧 DATA PREPROCESSING STEPS (In Order)

```
1. LOAD DATA
   └─ Read CSV file

2. HANDLE MISSING VALUES
   └─ Fill with median (middle value)

3. SELECT FEATURES
   └─ Choose 6 most important

4. CHECK DATA TYPES
   └─ All should be numbers (int/float)

5. SPLIT DATA
   └─ 80% training, 20% testing

6. TRAIN MODEL
   └─ Fit Random Forest on training data

7. MAKE PREDICTIONS
   └─ Test on unseen test data

8. EVALUATE
   └─ Calculate MAE, MSE, RMSE, R²

9. SAVE MODEL
   └─ Use joblib.dump() to save
```

---

## 💾 JOBLIB - MODEL SAVING (For Deployment)

### Why Save Model?
- Don't retrain every time app starts
- 10 minute training becomes instant loading
- Model persists from training to deployment

### Saving (During Training):
```python
import joblib
joblib.dump(trained_model, 'house_price_model.pkl')
```

### Loading (In Web App):
```python
loaded_model = joblib.load('house_price_model.pkl')
prediction = loaded_model.predict(new_data)
```

### Why Joblib over Pickle?
```
Joblib:        Faster, smaller files, safer
Pickle:        Slower, larger files, older method
```

---

## 🚀 OVERFITTING VS UNDERFITTING (Common Exam Question)

| Issue | Training Acc | Test Acc | Cause | Solution |
|-------|-------------|----------|-------|----------|
| **Good** | 85% | 85% | Just right | ✓ Done! |
| **Overfit** | 99% | 70% | Too complex | Reduce depth, more data |
| **Underfit** | 60% | 60% | Too simple | Increase complexity |

### How to Spot Overfitting:
```
IF training_r2 >> test_r2
THEN model is overfitting
```

---

## 📋 TRAIN/TEST SPLIT EXPLAINED

```
Total Data: 1460 samples

80% TRAINING (1168 samples)
   ├─ Model learns patterns
   ├─ Can see answers
   └─ Typically has high accuracy

20% TESTING (292 samples)
   ├─ Model has never seen
   ├─ Can't cheat (doesn't know answers)
   └─ Shows real-world performance

Why 80/20?
- Enough training data to learn
- Enough test data to evaluate fairly
```

---

## 🧠 EXAM QUESTIONS & ANSWERS

### Q1: What type of problem is house price prediction?
**A:** Regression (predicting continuous numerical values)

### Q2: Why Random Forest instead of Linear Regression?
**A:** House prices have complex non-linear relationships (area, quality interact in complex ways). Random Forest captures these better.

### Q3: Why 6 features, not all 79?
**A:** 
- More features = more complexity = easier to overfit
- These 6 have highest correlation with price
- Simpler models are easier to understand and deploy

### Q4: What does R² = 0.85 mean?
**A:** The model explains 85% of the variation in house prices. The remaining 15% is due to factors we didn't measure.

### Q5: How do you save a model so you don't retrain?
**A:** Use `joblib.dump(model, 'filename.pkl')`. Load later with `joblib.load('filename.pkl')`.

### Q6: What's the difference between MAE and RMSE?
**A:** 
- MAE = average error (simple)
- RMSE = penalizes large errors more (better for detecting outliers)

### Q7: Explain the Random Forest algorithm in 2 sentences
**A:** It trains multiple decision trees on random subsets of data. Final prediction is the average of all trees' predictions.

### Q8: What's overfitting and how do you detect it?
**A:** Overfitting is when a model memorizes training data instead of learning patterns. You detect it when training accuracy >> test accuracy.

### Q9: Why is feature scaling not needed for Random Forest?
**A:** Random Forest uses decision rules (e.g., "if area > 2000"), not distances. So scale doesn't matter.

### Q10: What preprocessing steps did you do?
**A:** 
1. Handled missing values (filled with median)
2. Selected 6 best features
3. Split into 80% train / 20% test

---

## 🔑 KEY NUMBERS TO REMEMBER

```
Project Numbers:
- Dataset: 1460 houses, 79 features
- Selected Features: 6
- Train/Test Split: 80/20
- Random Forest Trees: 100
- Expected R²: ~0.85
- Expected RMSE: ~$30,000

Algorithm Numbers:
- Max Tree Depth: 20
- Min Samples Split: 5
- Min Samples Leaf: 2
```

---

## 📝 COMPLETE PIPELINE (Flow)

```
┌─────────────────┐
│   Raw Dataset   │
│   (1460, 79)    │
└────────┬────────┘
         │ Select 6 features
         ↓
┌─────────────────┐
│   Clean Data    │
│   (1460, 6)     │
└────────┬────────┘
         │ Fill missing values
         ↓
┌─────────────────┐
│   Split Data    │ 80/20
│  Train: 1168    │
│  Test: 292      │
└────────┬────────┘
         │ Train Random Forest
         ↓
┌─────────────────┐
│   Trained Model │
│  (100 trees)    │
└────────┬────────┘
         │ Predict on test data
         ↓
┌──────────────────────────┐
│   Evaluate Metrics       │
│  MAE, MSE, RMSE, R²      │
│  R² ≈ 0.85               │
└──────────────────────────┘
         │ Save with joblib
         ↓
┌──────────────────────────┐
│  Deploy Web App          │
│  Load model              │
│  Accept user input       │
│  Make predictions        │
└──────────────────────────┘
```

---

## ⚠️ COMMON MISTAKES (Avoid These!)

❌ **Mistake 1:** Testing on training data
✅ **Correct:** Always test on new unseen data

❌ **Mistake 2:** Not handling missing values
✅ **Correct:** Fill with median or mean

❌ **Mistake 3:** Using all 79 features
✅ **Correct:** Select best 6 features

❌ **Mistake 4:** Not saving the model
✅ **Correct:** Save with joblib for reuse

❌ **Mistake 5:** Forgetting to split data
✅ **Correct:** Always use 80/20 split

---

## 💡 QUICK TRICKS FOR EXAM DAY

1. **Remember R²?** Think "R-squared = proportion explained (0-1)"
2. **MAE vs RMSE?** "MAE is average, RMSE penalizes big errors"
3. **Random Forest?** "Multiple trees voting = Random Forest"
4. **Joblib?** "Save model once, load many times"
5. **Overfitting?** "Training > Testing = model memorized"

---

## 📱 CHEAT SHEET

**Quick Formula Reference:**
```
                    ΣD
             MAE = ───  (D = differences)
                    n

             RMSE = √MSE

                     SS_residual
             R² = 1 - ───────────
                      SS_total
```

**One-Line Explanations:**
- **Regression:** Predict numbers
- **Random Forest:** Many trees voting
- **MAE:** Average error in dollars
- **RMSE:** Error penalizing big mistakes
- **R²:** Percentage of variation explained
- **Joblib:** Save/load ML models
- **Overfitting:** Memorizes instead of learns
- **Train/Test:** Learn from 80%, evaluate on 20%

---

## ⏱️ STUDY TIPS

**For 15-minute cramming:**
1. Read this entire guide (12 min)
2. Answer the 10 exam questions (3 min)
3. Review the one-sentence definitions (2 min)

**For 1-hour study:**
1. Read this guide carefully (20 min)
2. Review model_building.ipynb (20 min)
3. Try running the code yourself (20 min)

**For exam day:**
- Skim the one-sentence definitions before exam
- Mentally walk through the pipeline
- Remember: R² ≈ 0.85 (good but not perfect)

---

**Good luck! You've got this! 🎓**

---
*Created: January 22, 2026*  
*For: Ogah Victor (22CG031902)*  
*Course: CSC 415 - Covenant University*
