# EcommerceDemandPrediction
# 📈 Modelo de Predicción de Demanda para E-commerce

## 🎯 Objetivo del Proyecto
Desarrollar un modelo de Machine Learning basado en Python para predecir las ventas mensuales futuras de un e-commerce, ayudando a optimizar la gestión de inventarios.

## 🛠️ Tecnologías y Librerías Utilizadas
* **Entorno:** Google Colab (Cloud, iPad Pro)
* **Manipulación de Datos:** Pandas, NumPy
* **Visualización:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)

## 📊 Fases del Proyecto
1. **Limpieza de Datos:** Depuración de registros de transacciones reales (eliminación de nulos y valores negativos).
2. **Análisis Exploratorio (EDA):** Identificación visual de los productos de mayor rotación e ingresos.
3. **Ingeniería de Características:** Creación de variables temporales y de desfase (*Lag features*).
4. **Modelado y Evaluación:** Entrenamiento de un algoritmo de *Random Forest* y medición del rendimiento con MAE.

## 📑Análisis RFM
Ademas de la predicción de demanda, el proyecto incluye una segmentación de clientes mediante ANÁLISIS RFM (Recencia, Frecuencia, Monetario) para identificar perfiles VIP y clientes en riesgo de abandono, permitiendo optimizar estrategias de retención comercial.

## 🌐Web App Interactiva (Streamlit)
**¿Que hacer en la App?**
* **Visualizador KPIs clave:** Métricas generales de ventas y segmentación de clientes.
* **Simulador de demanda:** Una herramienta interactiva donde puedes ajustar el mes y las ventas previas para ver la predicción de la IA en tiempo real.
**Enlace a la aplicación en vivo:** https://ecommercedemandprediction-4vrvv3zkznrbcgakbextde.streamlit.app/ 
