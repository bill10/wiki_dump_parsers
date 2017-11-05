# This parser will extract the following information for every edit.
import joblib
import logging, traceback, sys, re
from StringIO import StringIO

from diff_match_patch import diff_match_patch

from xml_simulator import RecordingFileWrapper
from wmf.dump.iterator import Iterator
import wmf

model_attack=joblib.load('models/attack_linear_char_oh_pipeline.pkl')
model_aggres=joblib.load('models/aggression_linear_char_oh_pipeline.pkl')

tf=model_attack.named_steps['tfidf']
tf._idf_diag=tf._idf_diag.todia()

tf=model_aggres.named_steps['tfidf']
tf._idf_diag=tf._idf_diag.todia()

columns=['attack','aggressive','title','time','user']

def parse(page):
    res=[]
    lastRev = None
    currRev = None
    for revision in page:
        tmp=[]

        if revision.text is not None:
            currRev = revision.text
        if lastRev is None:
            if currRev is not None:
                tmp.append(model_attack.predict_proba([currRev])[0][1])
                tmp.append(model_aggres.predict_proba([currRev])[0][1])
        else:
            # diff(currRev,lastRev)
            tmp.append(model_attack.predict_proba([currRev])[0][1])
            tmp.append(model_aggres.predict_proba([currRev])[0][1])
        lastRev = currRev

        if tmp:
            tmp.append(page.title)
            tmp.append(revision.timestamp)
            if (revision.user is not None):
                tmp.append(revision.user.text)
            else:
                tmp.append('')
            res.append(tmp)

    return res
