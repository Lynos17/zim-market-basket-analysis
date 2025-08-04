# 🛒 Zimbabwean Market Basket Analysis (FMCG Shop)

This project simulates and analyzes customer transactions from a typical FMCG shop in Zimbabwe.
It uses the Apriori algorithm to identify strong item combinations frequently purchased together, unlocking actionable 
insights for bundling, promotions, and shelf arrangement.


## 🔧 Tools Used

- Python
- Jupyter Notebook
- Libraries: pandas, mlxtend, seaborn, matplotlib
- Association Rule Mining (Apriori algorithm)


## 📊 Key Features

- Simulated dataset of 1,000 transactions
- Top-selling item analysis
- Frequent itemset generation with support thresholds
- Association rule mining using lift and confidence
- Bar chart visualizations of top rules
- Mini recommendation engine (e.g. “What goes with Mealie Meal?”)


## 💡 Insights

- Body Cream, Roll On, and Toilet Paper are often bought together — suggesting hygiene bundles
- Mealie Meal is linked to grooming products — indicating family/bulk shopper behavior
- Chocolate appears with personal care items — likely emotional or comfort purchases
- These patterns can be used for combo offers, shelf placement, or WhatsApp-based promotions


## 📁 Project Structure

/data
fmcg_shop_data.csv
/scripts
simulation_data.py
/notebooks
eda_fmcg_market_basket.ipynb
README.md
requirements.txt


## 🚀 How to Run

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Open the notebook inside /notebooks
4. Run all cells