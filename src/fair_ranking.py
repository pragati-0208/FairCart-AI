import pandas as pd

from collections import Counter

def fair_rank(products, k):
    category_count = Counter(p["maincateg"] for p in products)
    total = len(products)

    ranked = []
    for p in products:
        category_ratio = category_count[p["maincateg"]] / total
        fairness_boost = 1 - category_ratio

        final_score = p["baseline_score"] + 0.2 * fairness_boost

        ranked.append({
            "title": p["title"],
            "maincateg": p["maincateg"],
            "baseline_score": p["baseline_score"],
            "fair_score": round(final_score, 3)
        })

    ranked.sort(key=lambda x: x["fair_score"], reverse=True)
    return ranked[:k]
