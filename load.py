# load.py

import pandas as pd
from load import load_data
from dpre import data_preprocessing
from eda import explore_data
from vis import create_visualizations
from model import run_kmeans

# Load and preprocess the data
def load_and_preprocess_data():
    # Load data
    dataset = load_data()  # Assuming you have a function to load data


    # Perform Data Preprocessing (if needed)
    preprocessed_data = data_preprocessing(dataset)  # Call the data preprocessing function from dpre.py

    # Perform Exploratory Data Analysis
    explore_data(preprocessed_data)  # Call the EDA function from eda.py

    # Create visualizations
    create_visualizations(preprocessed_data)  # Call the visualization function from vis.py

    # Run K-means clustering
    run_kmeans(preprocessed_data)  # Call the K-means function from model.py

# Main function
if __name__ == "__main__":
    load_and_preprocess_data()  # Execute the main pipeline
