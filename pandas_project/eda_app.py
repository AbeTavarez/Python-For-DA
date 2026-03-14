import pandas as pd


df = pd.read_json('./cars.json')

# types of the dataframe
print(df.dtypes)

# info of the dataframe
print(df.info())

# stats of the dataframe
print(df.describe(include='all'))