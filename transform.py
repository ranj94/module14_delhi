from pathlib import Path
import pandas as pd

def transform_data(delhi_df):
    delhi_df = delhi_df.copy()
    ## from looking at the data previously in jupyter notebook we know it's a csv format, so the fields don't need flattening or anything. 
    ## cleaning that needs to occur is only keeping data prior to 2022, as 2022 is missing 
    #change string data (date and numerical) to date, int, and float formats 
    delhi_df = delhi_df.drop(columns=delhi_df.columns[9])
    delhi_df["Date"] = pd.to_datetime(delhi_df["Date"], format="%d/%m/%y")
    delhi_df["AQI"] = delhi_df["AQI"].astype(int)
    delhi_df["PM2.5"] = delhi_df["PM2.5"].astype(float)
    delhi_df["PM10"] = delhi_df["PM10"].astype(float)
    delhi_df["NO2"] = delhi_df["NO2"].astype(float)
    delhi_df["SO2"] = delhi_df["SO2"].astype(float)
    delhi_df["CO"] = delhi_df["CO"].astype(float)
    delhi_df["O3"] = delhi_df["O3"].astype(float)

    #### to csv

    base_dir = Path(__file__).resolve().parent.parent
    out_dir = base_dir / "module14_delhi" / "data" / "processed"
    ##"C:\Users\ranji\OneDrive\Documents\module14_delhi\dehli_assessment.ipynb"
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "delhi_processed_data.csv"
    delhi_df.to_csv(csv_path, index=False)


    print(f"Processed data saved to: {csv_path}")
    return delhi_df



