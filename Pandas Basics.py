#PANDAS!
import pandas as pd
#you can define a data frame from a dictionary
df_dict = {'a':[1,2,3],'b': ["red","blue","yellow"]}
df_dummy = pd.DataFrame.from_dict(df_dict)
print(df_dummy)
