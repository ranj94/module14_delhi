
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def forecast(model_name, start_date, end_date):
    date_range = pd.DataFrame({
    "Date": pd.date_range(start=start_date, end=end_date, freq="W")
    })

    future_forecast_aqi = pd.DataFrame(model_name.forecast(steps=(len(date_range) + 52))).reset_index()
    future_forecast_aqi = future_forecast_aqi.rename(columns={"index":"date", "predicted_mean":"predicted_aqi"})
    future_forecast_aqi = future_forecast_aqi.iloc[-(len(date_range)):]
    plt.figure(figsize=(15, 5))
    sns.lineplot(x="date", y= "predicted_aqi", data = future_forecast_aqi)
    plt.show()
    return future_forecast_aqi
##future_forecast_aqi[(future_forecast_aqi["date"] >= "2022-01-01") & (future_forecast_aqi["date"] < "2023-01-01")]