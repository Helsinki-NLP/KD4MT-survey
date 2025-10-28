import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import re
import seaborn as sns
import numpy as np
from matplotlib import rc

HORIZONTAL=False

# Set font to Computer Modern-like
rc('font', family='serif', serif=['CMU Serif'])

# Read dataset from TSV file
df = pd.read_csv('datasets.tsv', sep='\t')

# Extract and split dataset names
datasets = df['Dataset'].tolist()
datasets_split = [dataset.strip() for entry in datasets for dataset in entry.split(',')]
dataset_counts = Counter(datasets_split)

# Filter out datasets mentioned less than twice
dataset_counts = {name: count for name, count in dataset_counts.items() if count > 1}

# Sort datasets by frequency
dataset_names, dataset_frequencies = zip(*sorted(dataset_counts.items(), key=lambda x: x[1], reverse=True))

# Set style for aesthetic plotting
sns.set_theme(style="whitegrid")

# Assign different shades of a single color by counts
unique_frequencies = sorted(set(dataset_frequencies), reverse=True)
color_palette = sns.cubehelix_palette(len(unique_frequencies), start=2.8, rot=0, dark=0.4, light=0.7, reverse=False)
frequency_to_color = {freq: color_palette[i] for i, freq in enumerate(unique_frequencies)}
colors = [frequency_to_color[freq] for freq in dataset_frequencies]

# Data for plotting
if HORIZONTAL:
	fig, ax = plt.subplots(figsize=(8, 6))
	ax = sns.barplot(y=list(dataset_names), x=list(dataset_frequencies), palette=colors)
	# We change the fontsize of minor ticks label 
	ax.tick_params(axis='both', which='major', labelsize=14)
	ax.tick_params(axis='both', which='minor', labelsize=14)# Enhance plot aesthetics
else:
	fig, ax = plt.subplots(figsize=(8, 4))
	ax = sns.barplot(x=list(dataset_names), y=list(dataset_frequencies), palette=colors)
	#plt.xticks(rotation='vertical')
	ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, ha="right")
	# We change the fontsize of minor ticks label 
	ax.tick_params(axis='both', which='major', labelsize=10)
	ax.tick_params(axis='both', which='minor', labelsize=10)# Enhance plot aesthetics


#ax.set_xlabel('Number of Mentions', fontsize=14, labelpad=10)
#ax.set_ylabel('Datasets', fontsize=14, labelpad=10)
#ax.set_title('Frequency of Dataset Usage in Surveyed Papers', fontsize=18, pad=20)
#ax.bar_label(ax.containers[0], label_type='edge', fontsize=12, padding=3)

# Remove unnecessary borders
sns.despine(left=True, bottom=True)
plt.tight_layout()

if HORIZONTAL:
	plt.savefig('datasets_v1.pdf')
else:
	plt.savefig('datasets_v1_vert.pdf')
