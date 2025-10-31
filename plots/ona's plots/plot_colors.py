import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np
import colorsys
import matplotlib.colors as mcolors
import seaborn as sns
from matplotlib import rc

# -------- settings --------
HORIZONTAL = False
INPUT_TSV = "datasets_new.tsv"
BASE_HEX = "#C9DAF8"  # base color for the grading scale

# optional: Computer Modern-like serif
plt.rcParams.update({
    "font.size": 20,          # base font size
    "axes.titlesize": 16,     # title size
    "axes.labelsize": 14,     # x/y label size
    "xtick.labelsize": 12,    # tick labels
    "ytick.labelsize": 12,
    "legend.fontsize": 12,
})
rc('font', family='serif', serif=['CMU Serif'])

# -------- helpers --------
def single_hue_gradient(hex_color, n, l_min=0.35, l_max=0.90):
    """
    Return n shades of one hue (hex_color), varying lightness only (dark -> light).
    l_min/l_max in [0,1]; lower l_min => darker darkest; lower l_max => darker lightest.
    """
    r, g, b = mcolors.to_rgb(hex_color)
    h, l_base, s = colorsys.rgb_to_hls(r, g, b)
    Ls = np.linspace(l_min, l_max, max(n, 1))
    return [mcolors.to_hex(colorsys.hls_to_rgb(h, float(L), s)) for L in Ls]

# -------- data prep --------
df = pd.read_csv(INPUT_TSV, sep="\t")

# Extract and split dataset names
datasets = df["Dataset"].astype(str).tolist()
datasets_split = [d.strip() for entry in datasets for d in entry.split(",")]
dataset_counts = Counter(datasets_split)

# Keep datasets mentioned at least twice
dataset_counts = {name: cnt for name, cnt in dataset_counts.items() if cnt > 2}

# Sort by frequency (desc)
dataset_names, dataset_frequencies = zip(*sorted(dataset_counts.items(),
                                                 key=lambda x: x[1],
                                                 reverse=True)) if dataset_counts else ([], [])

# -------- colors (single-hue grading from BASE_HEX) --------
unique_frequencies = sorted(set(dataset_frequencies), reverse=True) if dataset_frequencies else []
palette = single_hue_gradient(BASE_HEX, len(unique_frequencies), l_min=0.35, l_max=0.90)
freq_to_color = {freq: palette[i] for i, freq in enumerate(unique_frequencies)}
colors = [freq_to_color[freq] for freq in dataset_frequencies] if dataset_frequencies else []


# -------- plotting --------
sns.set_theme(style="whitegrid")
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "font.size": 20,          # base font size
    "axes.titlesize": 16,     # title size
    "axes.labelsize": 16,     # x/y label size
    "xtick.labelsize": 14,    # tick labels
    "ytick.labelsize": 14,
    "legend.fontsize": 12,
})
fig, ax = plt.subplots(figsize=(10, 5))
ax = sns.barplot(x=list(dataset_names), y=list(dataset_frequencies), palette=colors)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.tick_params(axis='both', which='major')
ax.tick_params(axis='both', which='minor')
ax.set_xlabel('Dataset', labelpad=8)
ax.set_ylabel('Number of Mentions', labelpad=8)
outname = "datasets_v2_vert_bigfont.pdf"

sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.savefig(outname, bbox_inches="tight")
plt.show()

