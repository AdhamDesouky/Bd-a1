# eda.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def explore_data(data):
    # Visualize the distribution of the 'score'
    plt.figure(figsize=(8, 5))
    sns.histplot(data['score'], bins=5, kde=True)
    plt.title('Distribution of Scores')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.show()

    # Visualize a count plot of the 'appId'
    plt.figure(figsize=(12, 6))
    sns.countplot(data['appId'])
    plt.title('Count Plot of App IDs')
    plt.xlabel('App ID')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.show()

    # Display basic statistics of the 'score'
    score_stats = data['score'].describe()
    print("Basic Statistics of the 'score' column:")
    print(score_stats)

# Ensure the script is only executed when run directly, not when imported
if __name__ == "__main__":
    # Assuming preprocessed_data is passed as an argument to this script
    import sys
    if len(sys.argv) != 2:
        print("Usage: python eda.py <path_to_preprocessed_data>")
        sys.exit(1)

    # Load preprocessed data from file
    preprocessed_data = pd.read_csv(sys.argv[1])

    # Call the explore_data function with preprocessed_data as an argument
    explore_data(preprocessed_data)
