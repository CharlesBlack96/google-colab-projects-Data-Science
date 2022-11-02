import pandas as pd
#build my class of type DataFrame
#df hold a DataFrame object
#when i create a new object and save it to a variable 
#i say that i have instantited that object
df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})

if '__name__' == '__main__':

#variables that form part of an object are called 'attributes'
#we will access these variables by using dot notation
    print(df.shape)
    print(df.index)
    print(df.columns)
    print(df.dtypes) 

#functions that form part of an "object" are called methods

print(df.head())
print(df.describe())
print(df.isnull().sum())
print(df['a'].value_counts())





