# 🛡️ E-commerce Fraud Detection & Risk Analytics

Sistema integral de Machine Learning y analítica de datos para la detección de fraude en transacciones de comercio electrónico. El proyecto resuelve el problema del desbalance de clases y la detección de patrones de comportamiento sospechosos (como el "Return Fraud"), optimizando la relación entre detección de fraude y experiencia del cliente.

## 🎯 Objetivo del Proyecto
Desarrollar un modelo predictivo que identifique transacciones fraudulentas en tiempo real, minimizando los Falsos Positivos (fricción al cliente) y maximizando el ahorro financiero mediante la evaluación de umbrales de negocio.

## 🛠️ Stack Tecnológico
- **Análisis y Modelado:** Python, Pandas, Scikit-Learn, XGBoost, LightGBM, SHAP
- **Base de Datos:** SQLite (consultas SQL para EDA)
- **Despliegue:** Streamlit Cloud (Dashboard interactivo en vivo)

## 📊 Fases del Proyecto
1. **Análisis Exploratorio (SQL):** Identificación de patrones en métodos de pago, dispositivos tóxicos y fraude de devoluciones.
2. **Feature Engineering:** Creación de variables temporales (`tx_last_1h`, `hist_return_rate`) con prevención estricta de Data Leakage.
3. **Modelado Predictivo:** Comparativa de Random Forest, XGBoost y LightGBM, manejando el desbalance con `scale_pos_weight`.
4. **Evaluación de Negocio:** Matriz de costo-beneficio para definir el umbral de decisión óptimo (minimizando costo total operativo).
5. **Explicabilidad:** Uso de SHAP para justificar cada decisión del modelo ante auditorías.

## 💼 Conclusión de Negocio
El modelo completo (35 features) fue seleccionado para producción. Aunque requiere mantener más variables, reduce los Falsos Positivos de 746 a 87, ahorrando costos operativos significativos sin sacrificar ni un solo fraude detectado (Recall = 1.0). El umbral óptimo de 0.1 generó un **ahorro neto simulado de $21,371 USD** en el conjunto de prueba.

## 🌐 Dashboard Interactivo en Vivo
El proyecto incluye un panel de control ejecutivo desplegado en la nube para monitorear KPIs de fraude, tendencias y alertas tempranas.

🔗 **[Ver Dashboard en Streamlit Cloud](https://ecommercedemandprediction-4vrvv3zkznrbcgakbextde.streamlit.app/)** 
*(Nota: El nombre de la app de Streamlit mantiene el nombre antiguo, pero el contenido es el dashboard de fraude que construimos).*
