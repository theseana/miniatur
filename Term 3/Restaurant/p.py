import pandas as pd


foods = [ 
    ["peperoni", 5, 1],
    ["garlic", 4, 5],
    ["sushi", 6, 0],
    ["cheesburger", 3.5,  2],
    ["water", 1, 2]
]
cols = ["food", "quantity", "price"]
df = pd.DataFrame(foods, columns=cols)
df['total'] = df["quantity"] * df["price"]
print(df)
print(df['total'].sum())