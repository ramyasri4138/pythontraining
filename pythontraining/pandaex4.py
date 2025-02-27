import pandas as pd
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG','Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000,77000,88000]
}
#this data will go to dataFRame
df=pd.DataFrame(data)
df.set_index(['Region','State','Year'],inplace=True)
#print(df)
#selecting sales data for tamil nadu in 2021
df1=df.loc[('South','Tamil Nadu',2021),'Sales']
#print(df1)

df_sales=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal'],
'Sales':[1570000,1410000,1380000]})
df_profit=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal'],
'Profit':[185000,165000,155000]})
print(df_sales)
print(df_profit)

#merging data
df_merged=pd.merge(df_sales,df_profit,on='State',how='inner')
print(df_merged)

df1_merged=pd.merge(df_sales,df_profit,on='State',how='left')
print(df1_merged)