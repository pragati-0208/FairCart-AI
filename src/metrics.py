def women_representation(products):
    women = sum(1 for p in products if p["maincateg"] == "Women")
    return women / len(products) if products else 0


def compare_fairness(original, fair, k):
    def women_ratio(products):
        top_k = products[:k]
        if not top_k:
            return 0
        return sum(p["maincateg"] == "Women" for p in top_k) / len(top_k)

    return {
        "baseline_women_%": women_ratio(original),
        "fair_women_%": women_ratio(fair)
    }


def statistical_parity_difference(baseline_wr, fair_wr):
    return fair_wr - baseline_wr


def disparate_impact(baseline_wr, fair_wr):
    if baseline_wr == 0:
        return 0
    return fair_wr / baseline_wr
