# This parser will extract the following information for every page.
import pandas as pd
import numpy as np

columns=['title','policy_count','policy_mentioned']

# read policies
df=pd.read_csv('wiki_policies.tsv',sep='\t')
policy=df['Redirects'].tolist()
policy=[j.strip() for i in policy for j in i.split(',')]
policy=np.array(list(set(policy)))

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
    indx=np.array(list(map(lambda x: x in rev.text, policy)), dtype=bool)
    res.append(sum(indx))
    res.append(','.join(policy[indx]))
    return [res]
