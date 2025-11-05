#%%
import pandas as pd  #  type: ignore

df = pd.read_csv("../files/input/house_data.csv")

features = df[
    [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "waterfront",
        "condition",
    ]
]

target = df[["price"]]



# %%
features.bathrooms.value_counts().sort_index().plot(kind="bar")

# %%
features.sqft_living.plot(kind="hist", edgecolor="white", bins=20)

# %%
features.sqft_lot.plot(kind="hist", edgecolor="white", bins=10)

# %%