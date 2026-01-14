import streamlit as st
import json
import pandas as pd
from src.fair_ranking import fair_rank

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="FairCart AI",
    layout="wide",
    page_icon="🛒"
)

# ---------------- Header ----------------
st.title("🛒 FairCart AI – Bias-Aware Product Ranking")

st.markdown(
    """
    <p style="font-size:18px; color:#E5E7EB;">
    Detecting and reducing demographic bias in e-commerce rankings.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        font-size:16px;
        color:#4ADE80;
        background-color:#052e1b;
        padding:12px;
        border-radius:8px;
        margin-bottom:20px;
    ">
    FairCart AI demonstrates how fairness-aware ranking algorithms reduce bias
    <b>without compromising relevance</b>.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- Fairness Utility ----------------
def compute_fairness(df):
    total = len(df)
    women = len(df[df["maincateg"] == "Women"])
    men = len(df[df["maincateg"] == "Men"])

    women_pct = round((women / total) * 100, 2) if total else 0
    men_pct = round((men / total) * 100, 2) if total else 0
    gap = round(abs(women_pct - men_pct), 2)

    return men_pct, women_pct, gap

# ---------------- Input ----------------
default_json = {
    "products": [
        {"title": "Women Casual Shoes", "maincateg": "Women", "baseline_score": 0.92},
        {"title": "Men Formal Shoes", "maincateg": "Men", "baseline_score": 0.95},
        {"title": "Women Sports Shoes", "maincateg": "Women", "baseline_score": 0.85},
        {"title": "Men Running Shoes", "maincateg": "Men", "baseline_score": 0.80}
    ]
}

st.subheader("📥 Input Products")

products_json = st.text_area(
    "Products JSON",
    value=json.dumps(default_json, indent=2),
    height=260
)

k = st.slider("Top-K Results", 1, 10, 3)

st.caption(
    "ℹ️ Paste product data in JSON format. FairCart AI compares the original ranking "
    "with a fairness-aware ranking."
)

# ---------------- Run Button ----------------
if st.button("🚀 Run Fair Ranking", use_container_width=True):

    products = json.loads(products_json)["products"]

    baseline = sorted(
        products,
        key=lambda x: x["baseline_score"],
        reverse=True
    )

    fair = fair_rank(products, k)

    baseline_df = pd.DataFrame(baseline[:k])
    fair_df = pd.DataFrame(fair[:k])

    # ---------------- Rankings ----------------
    st.divider()
    st.subheader("🔢 Ranking Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ❌ Baseline Ranking")
        st.dataframe(baseline_df, use_container_width=True)

    with col2:
        st.markdown("### ✅ Fair Ranking (FairCart AI)")
        st.dataframe(fair_df, use_container_width=True)

    # ---------------- Fairness Metrics ----------------
    st.divider()
    st.subheader("📊 Fairness Metrics")

    b_men, b_women, b_gap = compute_fairness(baseline_df)
    f_men, f_women, f_gap = compute_fairness(fair_df)

    spd = round(b_gap - f_gap, 2)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ❌ Baseline")
        st.metric("Men Representation (%)", f"{b_men}%")
        st.metric("Women Representation (%)", f"{b_women}%")
        st.metric("Fairness Gap (%)", f"{b_gap}%")

    with col2:
        st.markdown("### ✅ FairCart AI")
        st.metric("Men Representation (%)", f"{f_men}%")
        st.metric("Women Representation (%)", f"{f_women}%")
        st.metric("Fairness Gap (%)", f"{f_gap}%")

    # ---------------- Bias Reduction ----------------
    st.divider()
    st.subheader("📉 Bias Reduction Impact")

    st.metric(
        "Statistical Parity Difference (SPD)",
        spd,
        help="Positive value indicates bias reduction after fairness-aware ranking"
    )

    # ---------------- Chart ----------------
    st.subheader("📊 Fairness Gap Comparison")

    if b_gap == 0 and f_gap == 0:
        st.info(
            "✅ Baseline ranking is already fair. "
            "FairCart AI detects no bias and preserves the original ranking."
        )
    else:
        chart_df = pd.DataFrame({
            "Ranking": ["Baseline", "Fair"],
            "Fairness Gap (%)": [b_gap, f_gap]
        })

        st.bar_chart(chart_df.set_index("Ranking"))

    # ---------------- Final Verdict ----------------
    st.divider()

    if b_gap == 0:
        st.success(
            "🎯 No bias detected. FairCart AI correctly avoids unnecessary re-ranking."
        )
    elif f_gap < b_gap:
        st.success(
            "🎉 FairCart AI successfully reduces demographic bias while preserving relevance."
        )
    else:
        st.warning(
            "⚠️ Minor bias detected, but relevance constraints limited reordering."
        )
