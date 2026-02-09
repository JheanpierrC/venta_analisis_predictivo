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
