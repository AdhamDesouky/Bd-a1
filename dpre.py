# dpre.py
import pandas as pd

def preprocess_data(data):
    # Drop rows with missing values
    data = data.dropna()

    # Get information about the data
    data_info = data.info()

    # Get descriptive statistics of the data
    data_description = data.describe()

    return data, data_info, data_description

# Load the dataset
dataset = pd.read_csv("reviews.csv")

# Preprocess the data
preprocessed_data, data_info, data_description = preprocess_data(dataset)

# Display or print information about the preprocessed data
print("Data preprocessing completed.")
print("Preprocessed Data:")
print(preprocessed_data.head())

print("\nData Information:")
print(data_info)

print("\nData Description:")
print(data_description)
