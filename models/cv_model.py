from pydantic import BaseModel, Field


class AnalysisCV(BaseModel):
    """
    This model is used to store the analysis of a candidate's CV.
    """

    candidate_name: str = Field(
        description="complete name of the candidate extracted from the cv"
    )
    experience_years: int = Field(
        description="total years of experience relevant to the job description"
    )
    skills: list[str] = Field(description="list of skills extracted from the cv")
    education: str = Field(
        description="education level and specialization of the candidate"
    )
    relevant_experience: str = Field(
        description="relevant experience of the candidate of the job description"
    )
    strength: str = Field(
        description="3-5 bullet points of the candidate's strengths related to the job description"
    )
    area_to_improve: list[str] = Field(
        description="3-5 bullet points of the candidate's weaknesses related to the job description"
    )
    porcentaje_match: int = Field(
        description="percentage of match between the candidate's cv and the job description",
        ge=0,
        le=100,
    )
