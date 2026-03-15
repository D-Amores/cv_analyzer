from prompts.cv_prompts import create_system_prompts
from models.cv_model import AnalysisCV

from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()


def create_cv_evaluator():
    base_model = ChatDeepSeek(
        model_name="deepseek-chat",
        temperature=0.0,
        api_key=os.getenv("DEEPSEEK_API_KEY"),
    )

    structured_model = base_model.with_structured_output(AnalysisCV)
    chat_prompt = create_system_prompts()

    evaluation_chain = chat_prompt | structured_model

    return evaluation_chain


def evaluate_candidate(candidate_cv: str, job_description: str) -> AnalysisCV:
    try:
        evaluation_chain = create_cv_evaluator()
        result = evaluation_chain.invoke(
            {"candidate_cv": candidate_cv, "job_description": job_description}
        )

        return result

    except Exception as e:
        raise CVAnalysisError(f"Error al analizar CV: {str(e)}") from e

        # AnalysisCV(
        #     candidate_name="Error",
        #     experience_years=0,
        #     skills=["Erro al procesar el CV"],
        #     education="No se puede determinar",
        #     relevant_experience="Error durante el analisis",
        #     strengths=["Requiere revisión manual"],
        #     areas_for_improvement=["Verificar el formato y legibilidad del CV"],
        #     match_percentage=0,
        # )
