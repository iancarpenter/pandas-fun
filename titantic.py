import pandas as pd
from pandas.core.algorithms import isin

titanic = pd.read_csv("data/titanic.csv")

#print(titanic.head(12))

#print(titanic.tail(8))

#print(titanic.dtypes)

# titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

#ages_sex = titanic[["Age", "Sex"]]

#print(ages_sex)

#above_35 = titanic[titanic["Age"] > 35]

#print(above_35)

#palsson
palssons = titanic[titanic["Name"].str.contains("Palsson")]

print(palssons)