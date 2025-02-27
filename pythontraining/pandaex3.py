'''
import pandas as pd
data={
    'Region':['North','North','South','South','East','East'],
    'State':['Delhi','punjab','TamilNadu','Karnataka','TG','Odissa'],
    'Year':[2021,2022,2021,2022,2021,2022],
    'Sales':[750000,850000,690000,720000,680000,710000],
    'Profit':[95000,102000,85000,77000,88000,90000]
}
df=pd.DataFrame(data)
df.set_index(['Region','State','Year'],inplace=True)
print(df)
'''
import pandas as pd

# Define the dictionary
file_data = {
    'product_id': [101, 102, 103, 104],
    'product_name': ['samsung','apple','oneplus','infinix'],
    'product_cost': [80000, 180000, 90000, 50000],
    'order_date': ['23-05-2005', '13-01-2000', '25-09-2020', '30-01-2015']
}

#textfile
# Create a DataFrame
df = pd.DataFrame(file_data)
# Save to CSV (without index)
df.to_csv("products.csv", index=False)  
print(df)
print("CSV file created successfully!")
df_from_csv=pd.read_csv("products.csv")
#display
print(df_from_csv)
#i=in ddf.sort_values automatic its converted to pandas 
print(df.sort_values(by='product_name',ascending=False))