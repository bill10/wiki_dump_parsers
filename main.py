# This is a template to parse wikipedia dumps. Plug in different parsers to extract different information.
import mwxml
import io
import pandas as pd
import numpy as np
import sys
import edit_info_parser as parser
MAIN_SPACE=0
TALK_SPACE=1


namespace=MAIN_SPACE
title_file='social_issue_titles.txt'

filename=sys.argv[1]
infile=filename[:-3]
outfile=filename[:-3]+'.tsv'

# read titles
titles=set()
with io.open(title_file,'r',encoding='utf8') as f:
    for l in f:
        titles.add(l.strip('\n').replace(' ','').lower())

print("Load {} titles".format(len(titles)))

# clean titles
cleantitles=set()
dump = mwxml.Dump.from_file(open(infile))
for page in dump:
    if int(page.namespace) != namespace:
        continue
    if page.title.replace(' ','').lower() in titles:
        if page.redirect is None:
            cleantitles.add(page.title)
        else:
            cleantitles.add(page.redirect)

print("Found {} titles".format(len(cleantitles)))

# Parse the dump page by page
res=[]
dump = mwxml.Dump.from_file(open(infile))
for page in dump:
    if int(page.namespace) != namespace:
        continue
    if page.title in cleantitles:
        tmp=parser.parse(page)
        res.extend(tmp)

print("{} pages are assessed".format(len(res)))

df  = pd.DataFrame.from_records(res, columns=parser.columns)
df.to_csv(outfile, sep='\t', index=False, encoding='utf8')
