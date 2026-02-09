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
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

def entrenar_modelo(df: pd.DataFrame):
    """
    Entrena un modelo de regresión lineal y devuelve métricas y predicciones.
    """
    X = df[["cantidad"]]
    y = df["total"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    df_metricas = pd.DataFrame({
        "Metrica": ["MAE", "R2 Score"],
        "Valor": [mae, r2]
    })

    df_predicciones = pd.DataFrame({
        "Valor_Real": y_test.values,
        "Prediccion": y_pred,
        "Diferencia": y_test.values - y_pred
    })

    return df_metricas, df_predicciones

import pandas as pd
from data_processing import cargar_y_limpiar_datos
from model import entrenar_modelo

RUTA_CSV = "data/ventas.csv"
RUTA_SALIDA = "output/Resultados_Modelo.xlsx"

def main():
    # Cargar y limpiar datos
    ventas = cargar_y_limpiar_datos(RUTA_CSV)

    # Análisis exploratorio básico
    ventas_por_producto = ventas.groupby("producto")["total"].sum()
    ventas_por_mes = ventas.groupby(ventas["fecha"].dt.month_name())["total"].sum()

    # Entrenar modelo
    df_metricas, df_predicciones = entrenar_modelo(ventas)

    # Exportar resultados
    with pd.ExcelWriter(RUTA_SALIDA) as writer:
        df_metricas.to_excel(writer, sheet_name="Metricas", index=False)
        df_predicciones.to_excel(writer, sheet_name="Predicciones", index=False)
        ventas_por_producto.to_excel(writer, sheet_name="Ventas_por_Producto")
        ventas_por_mes.to_excel(writer, sheet_name="Ventas_por_Mes")

    print("✅ Análisis completado. Archivo generado en:", RUTA_SALIDA)

if __name__ == "__main__":
    main()
# %%
