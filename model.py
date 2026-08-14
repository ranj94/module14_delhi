import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

def create_model(data):
    ##parse_dates = ["Date"]
    ##data = pd.read_csv("C:/Users/RanjitJagdev/Documents/Apprenticeship_stuff/Apprenticeship_stuff/Module_14_raw/Materials for Learners/data/processed/delhi_processed_data.csv", parse_dates=parse_dates)

    print("Load Data")
    data["Week"] = data["Date"].dt.isocalendar()["week"]
    data["Year"] = data["Date"].dt.isocalendar()["year"]

    data["Week"] = data["Week"].astype(str)
    data["Year"] = data["Year"].astype(str)
    data["Sunday"] = data["Date"] + pd.offsets.Week(n=1, weekday=6)

    data_weekly = data.groupby(["Sunday"]).agg(
        AQI = ("AQI", "mean"),	
        PM25 = ("PM2.5", "mean"),	
        PM10 = ("PM10", "mean"),	
        NO2 = ("NO2","mean"),
        SO2 = ("SO2", "mean"),	
        CO = ("CO","mean"),	
        O3 = ("O3","mean")
    )
    data_weekly = data_weekly.reset_index()
    print("Clean and weekly grouping for model")


    test = data_weekly[(data_weekly["Sunday"] >= "2021-01-01") & (data_weekly["Sunday"] < "2022-01-01")]
    test = test.set_index("Sunday")
    train = data_weekly[data_weekly["Sunday"] < "2021-01-01"]
    train = train.set_index("Sunday")
    y = train["AQI"]

    print("Train Test split")
    model=SARIMAX(y,order=(2,1,0),seasonal_order=(2,0,1,52))
    predicted=model.fit()
    print("Load model with pre detirmined parameters")

    predicted_train = model.fit().predict();predicted

    test_forecast = predicted.forecast(steps=len(test))

    print("Test Data")
    train["aqi_pred"] = pd.DataFrame(predicted_train)
    test["aqi_pred"] = pd.DataFrame(test_forecast)

    plt.figure(figsize=(15, 5))
    sns.lineplot(x="Sunday", y= "AQI", data = train)
    sns.lineplot(x="Sunday", y= "aqi_pred", data = train)
    ####################
    sns.lineplot(x="Sunday", y= "AQI", data = test)
    sns.lineplot(x="Sunday", y= "aqi_pred", data = test)
    ##sns.lineplot(x="date", y= "predicted_aqi", data = future_forecast_aqi)
    plt.show()
    return predicted
    print("Done")