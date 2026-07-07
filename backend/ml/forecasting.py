import pandas as pd
from prophet import Prophet


def forecast_expenses(expenses):

    if len(expenses) < 30:
        return {
            "success": False,
            "message": "Need at least 30 expenses for forecasting."
        }

    df = pd.DataFrame(expenses)

    df["date"] = pd.to_datetime(df["date"])

    daily = df.groupby("date")["amount"].sum().reset_index()

    daily.columns = ["ds", "y"]

    model = Prophet(
        yearly_seasonality=False,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(daily)

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(30)

    return {
        "success": True,
        "forecast": [
            {
                "date": row.ds.strftime("%Y-%m-%d"),
                "predicted_expense": round(row.yhat, 2)
            }
            for _, row in result.iterrows()
        ]
    }