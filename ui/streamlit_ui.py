import streamlit as st
from ui.components.input_panel import process_data
from ui.components.results_panel import show_area_results


def main():
    """Function that defines the main user interface of Streamlit"""

    st.set_page_config(
        page_title="Sistema de Evaluación de CVs",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("📄 Sistema de Evaluación de CVs con IA")
    st.markdown(
        """
    **Analiza currículums y evalúa candidatos de manera objetiva usando IA**
    
    Este sistema utiliza inteligencia artificial para:
    - Extraer información clave de currículums en PDF
    - Analizar la experiencia y habilidades del candidato
    - Evaluar el ajuste al puesto específico
    - Proporcionar recomendaciones objetivas de contratación
    """
    )

    st.divider()

    col_entrada, col_resultado = st.columns([1, 1], gap="large")

    with col_entrada:
        process_data()

    with col_resultado:
        show_area_results()
