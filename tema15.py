import pandas as pd

lst = ["6 ore", "1-2 ore", "8-9 ore"]

df = pd.DataFrame(lst,index=["Timp petrecut la scola","Timp petrecut la calculator","Timp acordat somnului"], columns=['Ore'])

print(df)





