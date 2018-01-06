
# coding: utf-8

# In[24]:

import pandas as pd
name_index_file=pd.read_csv('https://github.com/ma-ji/RICF/raw/master/index/name_index.tsv', sep='\t')

def ricf_nm2id(fund_nm):
    re_id_set=set(name_index_file[name_index_file.ba_cn==fund_nm]['ricf_oid'])
    if len(re_id_set)==1:
        return list(re_id_set)[0]
    elif len(re_id_set)>1:
        return list(re_id_set)
    elif len(re_id_set)<1:
        return 'NA'

def ricf_id2nm(oid):
    re_nm_set=set(name_index_file[name_index_file.ricf_oid==int(oid)]['ba_cn'])
    if len(re_nm_set)==1:
        return list(re_nm_set)[0]
    elif len(re_nm_set)>1:
        return list(re_nm_set)
    elif len(re_nm_set)<1:
        return 'NA'


# In[ ]:



