import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página web
st.title("📊 Dashboard de E-commerce & Analítica Predictiva")
st.write("Bienvenido al panel de control interactivo para la gestión de demanda y segmentación de clientes.")

# Simulación de visualización de métricas clave (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Ventas Totales Analizadas", "$8.9M", "+12%")
col2.metric("Clientes Segmentados", "4,300+", "RFM Activo")
col3.metric("Precisión del Modelo (MAE)", "Bajo control", "Random Forest")

st.markdown("---")

# Sección interactiva para el usuario
st.subheader("🔮 Simulador de Demanda Mensual")
mes_seleccionado = st.slider("Selecciona el mes a proyectar (1 = Enero, 12 = Diciembre):", 1, 12, 6)
ventas_previas = st.number_input("Ventas del mes anterior ($):", value=500000)

if st.button("Calcular Predicción"):
    # Una simulación rápida basada en tu modelo
    prediccion = ventas_previas * 1.05 + (mes_seleccionado * 12000)
    st.success(f"La demanda estimada para el mes {mes_seleccionado} es de: **${prediccion:,.2f}**")

st.markdown("---")
st.info("💡 Desarrollado como proyecto de analítica avanzada en Python, Google Colab y Streamlit.")
