import seaborn as sns

import matplotlib.pyplot as plt

# Example usage of seaborn
# Load an example dataset
data = sns.load_dataset("iris")

# Create a simple scatter plot
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")

# Show the plot
plt.show()