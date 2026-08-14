from pathlib import Path
import pandas as pd
import requests 
import codecs
import io
import csv
import json

def extract_data():
    """
    Read API csv for Delhi air quality data
    """

    #Get project root
    base_dir = Path(__file__).resolve().parent.parent

    #Fetch air quality data from GitHub User link
    response = requests.get("https://raw.githubusercontent.com/cp099/India-Air-Quality-Dataset/refs/heads/main/Delhi_AQI_Dataset.csv")
    response.raise_for_status()
    decoded_data=codecs.decode(response.text.encode(), 'utf-8')
    csv_data_string = decoded_data
    f = io.StringIO(csv_data_string.strip())
    reader = csv.DictReader(f)
    data_list = list(reader)
    json_data = json.dumps(data_list, indent=4)
    json_data = json.loads(json_data)
    delhi_df = pd.DataFrame(json_data)

    return delhi_df