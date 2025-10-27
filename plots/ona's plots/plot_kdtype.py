import matplotlib.pyplot as plt
from collections import Counter
import re
import numpy as np
from matplotlib import rc
import seaborn as sns
import pandas as pd

# Set font to Computer Modern-like
rc('font', family='serif', serif=['CMU Serif'])

# Read dataset from TSV file
kd_types = pd.read_csv('kdtype.tsv', sep='\t')['Type'].tolist()

# Extract and count types
kd_types_split = [kd.strip() for entry in kd_types for kd in re.split(r',|;', entry)]
kd_counts = Counter(kd_types_split)
print(kd_counts)
# Sort KD types by frequency
kd_names, kd_frequencies = zip(*sorted(kd_counts.items(), key=lambda x: x[1], reverse=True))

# Colors for the bar plot (using a colormap)
colors = sns.cubehelix_palette(len(kd_names), start=2.8, rot=0, dark=0.4, light=0.7, reverse=False)

# Create bar plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(kd_names, kd_frequencies, color=colors, edgecolor='white')

# Enhance plot aesthetics
ax.set_xlabel('Knowledge Distillation Types', fontsize=14, labelpad=10)
ax.set_ylabel('Number of Mentions', fontsize=14, labelpad=10)
ax.set_title('Frequency of Knowledge Distillation Types Used', fontsize=16, pad=20, weight='bold')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=12)

# Tight layout for better spacing
plt.tight_layout()

# Display the bar plot
plt.show()
# plt.savefig('kd_types_histogram.pdf')