# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("../data/dados_consolidado.csv")
df.head()
# %%
df = df.drop(columns="Data de carga")
# %%
df.head()
# %%
df_ba = (df.query("UF == 'BA'")
        .groupby(["Ano de eleição","Partido"])["Quantitativo de filiados"]
        .sum()
        .reset_index())
df_ba
# %%
df_ba["Partido"] = df_ba["Partido"].replace({
    "DEM": "DEM/UNIÃO",
    "UNIÃO":"DEM/UNIÃO"
})
# %%
top_5 = (df_ba.groupby("Partido")["Quantitativo de filiados"]
         .sum()
         .nlargest(5)
         .index)
# %%
df_grafico = df_ba[df_ba["Partido"].isin(top_5)]

# %%
plt.title("Número de Filiados - Bahia (2010 - 2024)")
sns.lineplot(df_ba.query("`Partido` == ['DEM/UNIÃO','MDB','PP','PSDB','PT']"),
             x="Ano de eleição",
             y="Quantitativo de filiados",hue="Partido",
             palette="tab10",
             marker="o",
             ci=None)
plt.legend(bbox_to_anchor=(1.05,1),loc="upper left")

# %%
df_pivot = (df_ba.query("Partido == ['DEM/UNIÃO','MDB','PP','PT','PSDB']")
            .pivot_table(index="Ano de eleição",
                        columns="Partido",
                        values="Quantitativo de filiados")
)
# %%
df_crescimento = df_pivot.pct_change() * 100
# %%
print("Taxa de crescimento de Filiados entre Eleicões (%):")
print(df_crescimento.round(2))
# %%
