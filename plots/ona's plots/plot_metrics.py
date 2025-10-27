import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import re
import numpy as np
from matplotlib import rc
import seaborn as sns

# Set font to Computer Modern-like
rc('font', family='serif', serif=['CMU Serif'])

# Read dataset from TSV file
df = pd.read_csv('metrics.tsv', sep='\t')

# Extract and split dataset names
datasets = df['Metric'].tolist()
datasets_split = [dataset.strip() for entry in datasets for dataset in entry.split(',')]
dataset_counts = Counter(datasets_split)

# Filter out datasets mentioned only once and categorize them as 'other'
dataset_counts = {name: count for name, count in dataset_counts.items() if count > 1}
other_count = sum(count for name, count in Counter(datasets_split).items() if count == 1)
if other_count > 0:
    dataset_counts['other'] = other_count

# Sort datasets by frequency
dataset_names, dataset_frequencies = zip(*sorted(dataset_counts.items(), key=lambda x: x[1], reverse=True))

# Colors for the pie chart (using a colormap)
colors = sns.cubehelix_palette(as_cmap=True)(np.linspace(0, 1, len(dataset_names)))

# Create pie chart
#fig, ax = plt.subplots(figsize=(8, 8))
#wedges, texts, autotexts = ax.pie(dataset_frequencies, labels=dataset_names, autopct='%1.1f%%',
#                                   colors=colors, startangle=140, wedgeprops={'edgecolor': 'white'},
#                                   textprops={'fontsize': 12, 'weight': 'bold'})
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(dataset_names, dataset_frequencies, color=colors, edgecolor='white')

# Enhance plot aesthetics
#plt.setp(autotexts, size=10, weight='bold', color='white')
ax.set_title('Frequency of Dataset Usage in Surveyed Papers', fontsize=16, pad=20, weight='bold')

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Display the pie chart
plt.tight_layout()
plt.show()
# plt.savefig('metrics_pie_chart.pdf')
