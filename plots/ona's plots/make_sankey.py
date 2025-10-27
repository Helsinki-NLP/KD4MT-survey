import tqdm
import pandas as pd
from iso639 import Lang
import matplotlib.pyplot as plt
from pysankey import sankey
import itertools

def handle_one(dataline):
	pairs = []
	for lp in filter(None, dataline.split(' ')):
		a, b = lp.split('-')
		if a == 'ns' or b == 'ns':
			continue
		if a == 'ajp': a = 'apc'
		if b == 'ajp': b = 'apc'
		pairs.append((Lang(a).name, Lang(b).name))
	return pairs

data = [] # this is an mmt

data_ = pd.read_csv('languages.tsv', sep='\t')

data.extend(data_[data_.Section != 'MMT'].langpair.dropna().to_list())
pairs = list(itertools.chain.from_iterable(map(handle_one, tqdm.tqdm(data))))
source, target = zip(*pairs)

thresh = 5

df = pd.DataFrame({'source': source, 'target': target})
df['source_size'] = df.groupby('source')['source'].transform('size')
df['target_size'] = df.groupby('target')['target'].transform('size')

# regroup less significant items
df.loc[ df['source_size'] <= thresh, 'source'] = 'Other'
df.loc[ df['target_size'] <= thresh, 'target'] = 'Other'

# recompute the tallies + add to labeös
df['source_size'] = df.groupby('source')['source'].transform('size')
df['target_size'] = df.groupby('target')['target'].transform('size')

df['source'] = df.apply(lambda row: f"{row['source']} ({row['source_size']})", axis=1)
df['target'] = df.apply(lambda row: f"{row['target']} ({row['target_size']})", axis=1)

src_labels = sorted([lg for lg in df.source.unique()], reverse=True)
src_labels = [lg for lg in src_labels if lg.startswith('Other')] + [lg for lg in src_labels if not lg.startswith('Other')] 
tgt_labels = sorted([lg for lg in df.target.unique()], reverse=True)
tgt_labels = [lg for lg in tgt_labels if lg.startswith('Other')] + [lg for lg in tgt_labels if not lg.startswith('Other')] 

print(df)

ax = sankey(
    df['source'], df['target'], aspect=20, #colorDict=colorDict,
    leftLabels=src_labels,
    rightLabels=tgt_labels,
    fontsize=6,
    color_gradient=True,
)
# plt.show() # to display
plt.savefig(f'lp_sankey_thresh{thresh}.pdf', bbox_inches='tight')
plt.clf()