import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(expenses):
    """
    Detect anomalous expenses using Isolation Forest.
    """

    if len(expenses) < 20:
        return {
            "success": False,
            "message": "At least 20 expenses are required for anomaly detection."
        }

    df = pd.DataFrame(expenses)

    df["amount"] = df["amount"].astype(float)

    model = IsolationForest(
        contamination=0.02,
        random_state=42
    )

    df["prediction"] = model.fit_predict(df[["amount"]])

    anomalies = df[df["prediction"] == -1].copy()

    average = df["amount"].mean()

    results = []

    for _, row in anomalies.iterrows():

        ratio = row["amount"] / average

        if ratio > 8:
            risk = "Critical"
        elif ratio > 4:
            risk = "High"
        else:
            risk = "Medium"

        recommendation = ""

        if row["category"] == "Cloud Infrastructure":
            recommendation = "Review AWS/GCP resource usage and autoscaling."

        elif row["category"] == "AI Infrastructure":
            recommendation = "Inspect API usage, token consumption and model requests."

        elif row["category"] == "Marketing":
            recommendation = "Verify campaign budget approvals."

        elif row["category"] == "Hardware":
            recommendation = "Large capital expenditure detected."

        elif row["category"] == "Payroll":
            recommendation = "Verify payroll processing."

        elif row["category"] == "Office":
            recommendation = "Check lease or operational expenses."

        else:
            recommendation = "Review this transaction."

        results.append({

            "title": row["title"],

            "category": row["category"],

            "amount": float(row["amount"]),

            "date": row["date"],

            "risk": risk,

            "reason": f"{ratio:.1f}x higher than average spending.",

            "recommendation": recommendation

        })

    return {
        "success": True,
        "total_expenses": len(df),
        "average_expense": round(average, 2),
        "anomaly_count": len(results),
        "anomalies": results
    }