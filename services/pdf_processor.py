import PyPDF2
import PyPDF2
from io import BytesIO


def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
        full_text = ""

        for num_page, page in enumerate(pdf_reader.pages, 1):
            page_text = page.extract_text()

            if page_text.strip():
                full_text += f"\n--- PAGINA {num_page} ---\n"
                full_text += page_text + "\n"

        full_text = full_text.strip()

        if not full_text:
            return "Error: El PDF parece estar vacio o contener solo imagenes"

        return full_text

    except Exception as e:
        raise ValueError(f"Error al extraer texto del PDF: {str(e)}")
