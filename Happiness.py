#Happiest Countries 2023

import pandas as pd

# Load your CSV dataset
csv_file_path = 'D:\Raz Adibah\Documents\Data Science\Data Analyst\WHR2023.csv'
df = pd.read_csv(csv_file_path)

# Sort the DataFrame by 'Ladder score' in descending order
sorted_df = df.sort_values(by='Ladder score', ascending=False)

# Get the top 10 happiest countries
top_10_happiest = sorted_df.head(10)

# Display the information
print("Top 10 Happiest Countries 2023:")
print(top_10_happiest[['Country name', 'Ladder score', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']])

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your CSV dataset
csv_file_path = 'D:\Raz Adibah\Documents\Data Science\Data Analyst\WHR2023.csv'
df = pd.read_csv(csv_file_path)

# Sort the DataFrame by 'Ladder score' in descending order
sorted_df = df.sort_values(by='Ladder score', ascending=False)

# Get the top 10 happiest countries
top_10_happiest = sorted_df.head(10)

# Create a gradient of colors from bottom to top
colors = plt.cm.plasma(np.linspace(0, 1, len(top_10_happiest)))

# Plot a bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(top_10_happiest['Country name'], top_10_happiest['Ladder score'], color=colors)

# Add a color bar to show the gradient
color_bar = plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.plasma), ax=plt.gca(), pad=0.01)
color_bar.set_label('Happiness Score Gradient')

# Customize the plot
plt.title('Top 10 Happiest Countries in 2023')
plt.xlabel('Countries')
plt.ylabel('Ladder Score')
plt.xticks(rotation=45, ha='right')  # Rotate country names for better readability

# Show the plot
plt.tight_layout()
plt.show()
