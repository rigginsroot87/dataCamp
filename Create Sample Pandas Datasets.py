#Create sample data sets to show off what you learned in data camp!
import pandas as pd
import numpy as np

np.random.seed(0)
# create an array of 5000 dates starting at '2015-02-24', one per minute
rng = pd.date_range('2015-02-24', periods=5000, freq='T')
df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng)) })
print(df.head(13))