# %%
import pandas as pd
import os

def read_file(file_name:str):
    df = (pd.read_csv(f"./data/{file_name}.csv")
            .rename(columns={"valor":file_name})
            .set_index(["Ano de eleição"]))
    
    return df

# %%
file_names = os.listdir("./data/")

dfs = []
for i in file_names:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))


df_full = (pd.concat(dfs)
             .reset_index()
             .sort_values(["Ano de eleição"]))

df_full.to_csv("dados_consolidado.csv", index=False)