import pandas as pd
df=pd.read_csv("data/raw/SampleSuperstore.csv")


#remove duplicates
df=df.drop_duplicates()


#Standardize column names
df.columns=(
    df.columns
    .str.lower()
    .str.replace(" ","_")
    .str.replace("-","_")
)


#Validate business rules
print("Negatives quantities : ",(df['quantity']<0).sum())
print("Negatives sales : ",(df['sales']<0).sum())
print("Invalid discounts: ",((df["discount"]<0)|(df["discount"]>1)).sum())
print("Negative profit: ",(df["profit"]<0).sum())


#check remaining duplicates
print("Duplicates remaining: ",df.duplicated().sum())


#Save the cleaned dataset
output_path="data/raw/superstore_clean.csv"
df.to_csv(output_path,index=False)

print("Cleaned shape: ",df.shape)
print("Cleaned dataset saved successfully")