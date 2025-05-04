#  Economic Data Analysis Dashboard

This is a Streamlit-based dashboard for economic data prediction using a pre-trained regression model. The model has been serialized as `model.pkl` and integrated into an interactive web app via `dashboard.py`.

---

##  Model Performance

- **Mean Squared Error (MSE):** `12.07`
- **R² Score:** `0.97`

---

##  Statistical Analysis

Before model training, detailed exploratory data analysis (EDA) and statistical evaluations were performed:

- **Descriptive Statistics:** Mean, Median, Standard Deviation, Min, Max, etc.
- **Correlation Matrix:** To check multicollinearity and feature relationships.
- **Distribution Plots:** For understanding data spread and skewness.
- **Pairplots & Heatmaps:** To visualize interactions between variables.
- **Outlier Detection & Treatment**
- **Feature Insights:** Identified most predictive features based on statistical significance.

These analyses are documented in the Jupyter notebook `statastical_analysis.ipynb`.

---

##  Technologies Used

- Python 
- Streamlit 
- scikit-learn 
- pandas & numpy 
- seaborn & matplotlib  (for EDA)

---

##  Files in the Repository

- `dashboard.py` → Streamlit web app
- `model.pkl` → Pre-trained regression model
- `statastical_analysis.ipynb` → Data exploration & EDA notebook
- `README.md`
- `demo video`
- `trained_and_save_model`
- `requirement.txt`
- 

---

## ▶ How to Run the Project

### 1. Clone this Repository

```bash
git clone https://github.com/your-username/economic-data-analysis.git
cd economic-data-analysis
streamlit run dashboard.py
