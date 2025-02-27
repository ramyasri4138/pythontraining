import pandas as pd
data={
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,30,35,40],
    'City':['New York','Los Angeles','Chicago','Houston']
}


df=pd.DataFrame(data)
print(df)
#Displaying 
df.head()
#selecting data from dataframe
df['Name']
df[['Name','City']]

