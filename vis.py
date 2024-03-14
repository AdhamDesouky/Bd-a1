import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(data):
    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Scatter plot
    sns.scatterplot(x='score', y='thumbsUpCount', data=data, ax=axes[0])
    axes[0].set_title('Scatter Plot between Score and Thumbs Up Count')
    axes[0].set_xlabel('Score')
    axes[0].set_ylabel('Thumbs Up Count')

    # Bar plot
    sns.barplot(x='appId', y='score', data=data, ax=axes[1], errorbar=None)
    axes[1].set_title('Distribution of Scores Across Different App IDs')
    axes[1].set_xlabel('App ID')
    axes[1].set_ylabel('Average Score')
    axes[1].tick_params(axis='x', rotation=45, ha='right')

    plt.tight_layout()
    plt.show()
