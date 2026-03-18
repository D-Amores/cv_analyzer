import streamlit as st


def process_data():
    """Handles the input of data from the user"""

    st.header("📋 Datos de Entrada")

    cv_file = st.file_uploader(
        "**1. Sube el CV del candidato (PDF)**",
        type=["pdf"],
        help="Selecciona un archivo PDF con el currículum. Asegúrate de que el texto sea legible.",
    )

    if cv_file:
        st.success(f"✅ {cv_file.name} — {cv_file.size:,} bytes")

    st.divider()

    job_description = st.text_area(
        "**2. Descripción del puesto de trabajo**",
        height=250,
        placeholder="""Ejemplo:

        **Puesto:** Desarrollador Frontend Senior

        **Requisitos obligatorios:**
        - 3+ años de experiencia en desarrollo frontend
        - Dominio de React.js y JavaScript/TypeScript

        **Requisitos deseables:**
        - Experiencia con Next.js
        - Inglés intermedio-avanzado

        **Responsabilidades:**
        - Desarrollo de interfaces responsivas
        - Colaboración con equipos de diseño y backend""",
        help="Sé específico sobre requisitos técnicos, experiencia y responsabilidades.",
    )

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        analyze = st.button(
            "🔍 Analizar Candidato", type="primary", use_container_width=True
        )
    with col2:
        if st.button("🗑️ Limpiar", use_container_width=True):
            st.rerun()

    st.session_state.update(
        {
            "cv_file": cv_file,
            "job_description": job_description,
            "analyze": analyze,
        }
    )
