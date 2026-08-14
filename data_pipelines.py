from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    df_delhi = extract_data()
    delhi_processed = transform_data(df_delhi)
    load_data(repo_url = "https://github.com/ranj94//module14_delhi.git")  # publishes processed dataset
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()

print("delhi done")