#PANDAS!
import pandas as pd
import numpy as np
#you can define a data frame from a dictionary
#\ continues a long line, makes python read it like one line
df_dict = {'a':[1,2,3,4,5,6,7,8,9,10],'b': ["red","blue","yellow","purlple",'yellow','orange','green','black','white','teal'],\
           'c':[0,0,0,4,4,7,7,7,7,8], 'date' :pd.date_range('2015-02-24', periods=10, freq='D')}
df_dummy = pd.DataFrame.from_dict(df_dict)

#print the top few rows
print(df_dummy.head())
#print info about the table, columns, types, memory usage
print(df_dummy.info())
#show the shape of the dataframe RxC
print(df_dummy.shape)
#shows the mean median quartiles etc.
print(df_dummy.describe())
#returns list of columns
print(df_dummy.columns)
#returns index of data frame
print(df_dummy.index)

#sorting 
#inplace = True option changes dataframe, default is inplace = False
print(df_dummy.head())
df_dummy.sort_values(["c","b"],ascending = [True,False], inplace = True)
print(df_dummy.head())

#subsetting data sets
#one way is to create a np array of booleans, s
yellows = (df_dummy["b"] == "yellow")
print(yellows)
#to print all rows
print(df_dummy[yellows])
#you can do it with dates too
print(df_dummy[df_dummy["date"] > '2015-03-01'])

#two filters for date
print(df_dummy[(df_dummy["date"] > '2015-02-27')&(df_dummy["date"] <= '2015-03-02')])
#or you can do the same thing using np.logicaland, can use np.logical_or
print(df_dummy[np.logical_and(df_dummy["date"] > '2015-02-27', df_dummy["date"] <= '2015-03-02')])

#you can do more using loc and iloc, but will deal with that in the indexes section

