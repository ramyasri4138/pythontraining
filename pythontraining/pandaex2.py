import pandas as pd
#Reading a csv file
df=pd.read_csv('customers-100.csv')
#writing to csv file
df.to_json('output.json',index=False) #it will be shown in the explorer
#selecting data from dataframe
print(df['Company'])
#print(df)
df[['Company','City']]
#print(df)

#To filter data based on condition
#filter rows where index>10
print(df[df['Index']>10])

#sort data
print(df.sort_values(by='Index',ascending=False))
print(df)
#grouping data
#use group by () method to group data and apply aggregation functions
print(df.groupby('City').count())
print(df.groupby('Country').sum('Index'))
#Handling missing data
#Pandas provide methods to handle missing data , such as 'fillna()' and 'dropna()'