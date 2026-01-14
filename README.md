# 🛒 FairCart AI – Bias-Aware Product Ranking

FairCart AI is a fairness-aware product ranking system that detects and reduces demographic bias
in e-commerce recommendations while preserving ranking relevance.

This project demonstrates how algorithmic fairness techniques can be applied to real-world
ranking systems such as online marketplaces.

---

## 🚀 Features

- 📊 Compares baseline ranking vs fairness-aware ranking
- ⚖️ Detects demographic bias (Men vs Women representation)
- 📉 Computes fairness gap and bias reduction
- 🧠 Preserves relevance when no bias is detected
- 🖥️ Interactive Streamlit UI
- 🔄 Accepts dynamic JSON product input

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit
- **Backend Logic:** Python
- **Data Handling:** Pandas
- **Fairness Metrics:** Statistical Parity Difference
- **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

```
faircart-ai/
│
├── src/
│ ├── fair_ranking.py # Fairness-aware ranking logic
│ ├── metrics.py # Fairness metrics
│
├── data/ # Sample datasets
├── notebooks/ # Data exploration notebooks
├── outputs/ # Saved outputs (JSON)
│
├── streamlit_app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── README.md # Project documentation

```


---

```

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


🧪 Sample Input (JSON)
{
  "products": [
    {"title": "Women Casual Shoes", "maincateg": "Women", "baseline_score": 0.92},
    {"title": "Men Formal Shoes", "maincateg": "Men", "baseline_score": 0.95},
    {"title": "Women Sports Shoes", "maincateg": "Women", "baseline_score": 0.85}
  ]
}

```

---

```
📊 Fairness Metrics Explained

Fairness Gap (%)
Absolute difference between men and women representation

Statistical Parity Difference (SPD)
Measures bias reduction after applying fair ranking

Lower values indicate better fairness.

```
---
```

👩‍💻 Author

Pragati
Mathematics & Computing Student
Project built for learning and showcasing fairness-aware AI systems.
```
---
```
⭐ Future Improvements

Support for multiple protected attributes

Real-world datasets integration

Advanced fairness constraints

Model-based ranking
```
---
```

📜 License

This project is open-source and free to use for learning and research.
