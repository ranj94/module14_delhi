from extract import extract_data
from transform import transform_data
from load import load_data
from model import create_model

def main():
    df_delhi = extract_data()
    delhi_processed = transform_data(df_delhi)
    load_data(repo_url = "https://github.com/ranj94//module14_delhi.git")  # publishes processed dataset
    print("Pipeline completed successfully!")

def process_data():
    df_delhi = extract_data()
    delhi_processed = transform_data(df_delhi)
    return delhi_processed

if __name__ == "__main__":
    main()

print("delhi done")

data_for_model = process_data
print("process data")
##model_used = create_model(delhi_processed)