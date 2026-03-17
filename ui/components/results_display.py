from ui.utils.match_helpers import _get_match_level
from models.cv_model import AnalysisCV
import streamlit as st


def _show_match_metric(result: AnalysisCV):
    color, level, message = _get_match_level(result.porcentaje_match)
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.metric(
            label="Porcentaje de Ajuste al Puesto",
            value=f"{result.porcentaje_match}%",
            delta=f"{color} {level}",
        )
        st.markdown(f"**{message}**")


def _show_candidate_profile(result: AnalysisCV):
    st.subheader("👤 Perfil del Candidato")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**👨‍💼 Nombre:** {result.candidate_name}")
        st.info(f"**⏱️ Experiencia:** {result.experience_years} años")
    with col2:
        st.info(f"**🎓 Educación:** {result.education}")

    st.subheader("💼 Experiencia Relevante")
    st.info(f"📋 **Resumen de experiencia:**\n\n{result.relevant_experience}")


def _show_skills(result: AnalysisCV):
    st.subheader("🛠️ Habilidades Técnicas Clave")
    if not result.skills:
        st.warning("No se identificaron habilidades técnicas específicas")
        return
    cols = st.columns(min(len(result.skills), 4))
    for i, skill in enumerate(result.skills):
        with cols[i % 4]:
            st.success(f"✅ {skill}")


def _show_strengths_and_improvements(result: AnalysisCV):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💪 Fortalezas Principales")
        if result.strength:
            for i, fortaleza in enumerate(result.strength, 1):
                st.markdown(f"**{i}.** {fortaleza}")
        else:
            st.info("No se identificaron fortalezas específicas")

    with col2:
        st.subheader("📈 Áreas de Desarrollo")
        if result.area_to_improve:
            for i, area in enumerate(result.area_to_improve, 1):
                st.markdown(f"**{i}.** {area}")
        else:
            st.info("No se identificaron áreas de mejora")


def _show_recommendation(porcentaje: int):
    st.subheader("📋 Recomendación Final")
    if porcentaje >= 70:
        st.success(
            "✅ **CANDIDATO RECOMENDADO**\n\nEl perfil está bien alineado con el puesto. Se recomienda proceder con el proceso de selección."
        )
    elif porcentaje >= 50:
        st.warning(
            "⚠️ **CANDIDATO CON POTENCIAL**\n\nRequiere evaluación adicional. Se recomienda una entrevista técnica para validar competencias."
        )
    else:
        st.error(
            "❌ **CANDIDATO NO RECOMENDADO**\n\nEl perfil no se alinea suficientemente con los requisitos del puesto."
        )


def show_results(result: AnalysisCV):
    """Show the results of the analysis in a structured and professional manner"""

    st.subheader("🎯 Evaluación Principal")
    _show_match_metric(result)
    st.divider()

    _show_candidate_profile(result)
    st.divider()

    _show_skills(result)
    st.divider()

    _show_strengths_and_improvements(result)
    st.divider()

    _show_recommendation(result.porcentaje_match)
