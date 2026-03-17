def _get_match_level(porcentaje: int) -> tuple[str, str, str]:
    if porcentaje >= 80:
        return "🟢", "EXCELENTE", "Candidato altamente recomendado"
    elif porcentaje >= 60:
        return "🟡", "BUENO", "Candidato recomendado con reservas"
    elif porcentaje >= 40:
        return "🟠", "REGULAR", "Candidato requiere evaluación adicional"
    return "🔴", "BAJO", "Candidato no recomendado"
