#%%
import pandas as pd
import numpy as np


##Limpieza básica de datos.##

df=pd.read_csv(r"D:\Usuarios\Escritorio\ventas.csv")
df
# %%
    # Eliminar ventas con cantidad 0
df = df[df["cantidad"] != 0]
df

#%%    
# Convertir precios negativos a positivos
df["precio"] = df["precio"].abs()
df

#%%
    # Convertir fecha a formato datetime
df["fecha"] = pd.to_datetime(df["fecha"])
df

#%%
    # Crear columna total
df["total"] = df["cantidad"] * df["precio"]
df
# %%
