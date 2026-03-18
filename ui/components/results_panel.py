from .results_display import show_results
from services.pdf_processor import extract_text_from_pdf
from services.cv_evaluator import evaluate_candidate
import streamlit as st


def show_area_results():
    """Show the results area of the analysis"""

    st.header("📊 Resultado del Análisis")

    if not st.session_state.get("analyze", False):
        st.info(
            """
        👆 **Instrucciones:**
        1. Sube un CV en formato PDF en la columna izquierda
        2. Describe detalladamente el puesto de trabajo
        3. Haz clic en "Analizar Candidato"
        4. Aquí aparecerá el análisis completo

        **Consejos para mejores resultados:**
        - Usa CVs con texto seleccionable (no imágenes escaneadas)
        - Sé específico en la descripción del puesto
        - Incluye requisitos obligatorios y deseables
        """
        )
        return

    cv_file = st.session_state.get("cv_file")
    job_description = st.session_state.get("job_description", "").strip()

    if not cv_file:
        st.error("⚠️ Por favor sube un archivo PDF con el currículum")
        return

    if not job_description:
        st.error("⚠️ Por favor proporciona una descripción detallada del puesto")
        return

    process_analysis(cv_file, job_description)


def process_analysis(cv_file, job_description):
    """Process the analysis of the CV"""

    steps = [
        (25, "📄 Extrayendo texto del PDF..."),
        (50, "🤖 Preparando análisis con IA..."),
        (75, "📊 Analizando candidato..."),
        (100, "✅ Análisis completado"),
    ]

    with st.spinner("🔄 Procesando currículum..."):
        progress_bar = st.progress(0)
        status_text = st.empty()

        for progress, message in steps[:2]:
            status_text.text(message)
            progress_bar.progress(progress)

        cv_text = extract_text_from_pdf(cv_file)

        if cv_text.startswith("Error"):
            st.error(f"❌ {cv_text}")
            return

        for progress, message in steps[2:]:
            status_text.text(message)
            progress_bar.progress(progress)

        resultado = evaluate_candidate(cv_text, job_description)

        progress_bar.empty()
        status_text.empty()

    show_results(resultado)
