# This parser will extract the following information for every page.
import pandas as pd
import numpy as np
import csv
from scipy.spatial.distance import cdist

columns=['title','words','radius']

# read word embeddings downloaded from https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md
df=pd.read_csv('wiki.simple.vec', header=None, sep=' ', skiprows=1, quoting=csv.QUOTE_NONE, encoding='utf-8')
words=df[0].values
word2id=dict(zip(words,range(len(words))))
del df[0]
del df[301]
wordvec=df.values
del df

def parse(page):
    res=[]
    empty=True
    for rev in page:
        empty=False
        pass
    if empty:
        return res
    if rev.text is None:
        return res
    res.append(page.title)
    text=rev.text.lower()
    text=''.join([i if i.isalnum() else ' ' for i in text])
    y=np.array([wordvec[word2id[x.strip()]] for x in text.split() if x.strip() in word2id])
    res.append(len(y))
    centroid=np.mean(y,axis=0,keepdims=True)
    res.append(cdist(y,centroid).mean())
    return [res]
