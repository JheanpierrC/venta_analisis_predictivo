# 📊 Análisis y Predicción de Ventas con Python

Proyecto de análisis de datos orientado a **negocios minoristas**, enfocado en transformar registros de ventas desordenados en información accionable para la toma de decisiones.

---

## 🚩 Problema
Muchas pequeñas y medianas empresas almacenan datos de ventas sin una estructura clara, lo que dificulta:
- Identificar productos más rentables.
- Analizar tendencias mensuales.
- Realizar proyecciones confiables de ingresos.

Esto genera decisiones basadas en intuición en lugar de datos.

---

## ✅ Solución
Se desarrolló un flujo automatizado en Python que:

- **Limpia datos erróneos**
  - Elimina registros con cantidades en cero.
  - Corrige precios negativos.
- **Estandariza fechas**
  - Permite análisis temporal mensual.
- **Genera métricas clave**
  - Ventas por producto.
  - Ventas por mes.
- **Aplica Machine Learning**
  - Modelo de regresión lineal para estimar ingresos futuros.

---

## 📈 Valor para el negocio
- 📦 **Mejor gestión de inventario**  
  Anticipa demanda para evitar quiebres de stock.
- 💰 **Optimización de precios**  
  Evalúa cómo el volumen impacta los ingresos.
- 📊 **Decisiones basadas en datos**  
  Se reemplazan suposiciones por métricas reales.

---

## 🧠 Resultados del modelo
> ⚠️ Nota técnica  
Un **R2 Score negativo** indica que la relación entre las variables actuales no es lineal o que se requieren más factores (temporadas, categorías, promociones).  
Esto demuestra pensamiento crítico y deja abierta la mejora del modelo.

---

## 🛠️ Tecnologías utilizadas
- Python
- Pandas
- NumPy
- Scikit-learn
- Excel (exportación de resultados)

---

## ▶️ Ejecución del proyecto

```bash
pip install -r requirements.txt
python src/main.py
