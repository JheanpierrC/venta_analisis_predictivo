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
