
# coding: utf-8

# In[44]:

from pandas import read_csv
from pandas import DataFrame
from pandas import ExcelWriter
from os import listdir


# In[10]:

root_dirs = listdir('../../')


# In[13]:

data_dirs = [s for s in root_dirs if s.isdigit()]


# In[42]:

for repos in data_dirs:
    data_tables = listdir('../../'+repos)
    excl_writer = ExcelWriter('../../'+repos+'.xlsx')
    for table in data_tables:
        print table
        read_csv('../../'+repos+'/'+table, sep='\t', encoding='utf8').to_excel(excl_writer, sheet_name=table, encoding='utf8')
    excl_writer.save()


# In[ ]:



