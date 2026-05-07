import pandas as pd

df1=pd.read_csv("data/daily_sales_data_0.csv")
df2=pd.read_csv("data/daily_sales_data_1.csv")
df3=pd.read_csv("data/daily_sales_data_2.csv")

df=pd.concat([df1,df2,df3],ignore_index=True)

df=df[df["product"]=="pink morsel"]
df['price']=df["price"].replace(r"[/$]","", regex=True).astype(float)

df["Sales"]=df["price"]*df["quantity"]

final_df=df[["Sales","date","region"]]

final_df.columns=["Sales","Date","Region"]

final_df.to_csv("formatted_sales_data.csv",index=False)