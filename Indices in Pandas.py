import pandas as pd
import numpy as np

df_dict = {'a':[1,2,3,4,5,6,7,8,9,10],'b': ["red","blue","yellow","purlple",'yellow','orange','green','black','white','teal'],\
           'c':[0,0,0,4,4,7,7,7,7,8], 'date' :pd.date_range('2015-02-24', periods=10, freq='D')}
df_dummy = pd.DataFrame.from_dict(df_dict)


print(df_dummy)
df_dummy_date_ind = df_dummy.set_index('date')
print(df_dummy_date_ind)