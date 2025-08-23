import pandas as pd

full_data = pd.read_csv("imdb_top_1000.csv")
print(full_data.head())

full_data = full_data[['Series_Title','Released_Year', 'Certificate', 'Runtime', 'IMDB_Rating']]

for index in range(len(full_data)):
    full_data.loc[index, "Runtime"] = full_data.loc[index, "Runtime"].replace(' min','')


data = full_data.values.tolist()