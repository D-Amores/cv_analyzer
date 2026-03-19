# 📄 AI CV Analyzer

## 📖 Overview

The AI CV Analyzer is an advanced, AI-powered tool designed to streamline the recruitment process. Leveraging the power of Large Language Models (LLMs) via LangChain, this application automatically extracts, analyzes, and evaluates candidate resumes (PDFs) against specific job descriptions.

It provides objective and professional insights, highlighting a candidate's strengths, areas for improvement, and an overall match percentage to help recruiters make data-driven hiring decisions.

## ✨ Features

- **Automated Resume Parsing**: Extracts structured text from multi-page PDF resumes.
- **AI-Powered Evaluation**: Analyzes the candidate's experience, technical skills, and educational background against the provided job description.
- **Objective Scoring System**: Provides a 0-100% match score based on a weighted evaluation criteria defined by expert HR standards.
- **Structured Insights**: Returns evaluation results in a clear, standardized format using **Pydantic** data models.
- **Interactive UI**: User-friendly web interface built with **Streamlit**.

## 🛠️ Technology Stack

- **Web Interface**: [Streamlit](https://streamlit.io/)
- **AI Engine**: [LangChain](https://python.langchain.com/) for LLM orchestration.
- **Data Validation**: [Pydantic](https://docs.pydantic.dev/) for robust, typed data models.
- **Document Processing**: `PyPDF2` for PDF text extraction.
- **Dependency Management**: [uv](https://github.com/astral-sh/uv) - An extremely fast Python package installer and resolver.

## 📂 Project Structure

```text
cv_analyzer/
├── models/
│   └── cv_model.py          # Pydantic data models for structured AI output
├── prompts/
│   └── cv_prompts.py        # LangChain prompts (System & Analysis instructions)
├── services/
│   ├── cv_evaluator.py      # Core AI evaluation logic using LangChain
│   └── pdf_processor.py     # PDF text extraction utilities
├── ui/
│   ├── streamlit_ui.py      # Main Streamlit application entry point
│   ├── components/          # Reusable UI components (input and results panels)
│   └── utils/               # UI helper functions
└── README.md                # Project documentation
```

## 🚀 Getting Started

### Prerequisites

Make sure you have [uv](https://github.com/astral-sh/uv) installed on your system.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository-url>
   cd cv_analyzer
   ```

2. Sync the project dependencies using `uv`:
   ```bash
   uv sync
   ```

### ⚙️ Configuration & LLM Setup

**Important Note:** Currently, the LLM Provider and API key must be configured manually within the codebase or via environment variables.

1. Create a `.env` file in the root directory and add your API Key (e.g., DeepSeek):
   ```env
   DEEPSEEK_API_KEY=your_api_key_here
   ```
2. **Changing the Model:** At this stage, the model is hardcoded in `services/cv_evaluator.py`. To use a different model or provider (like OpenAI, Anthropic, etc.), you must update the LLM initialization code in that file. _(Support for dynamic model and API configuration directly from the UI is planned for a future update)._

### 🖥️ Usage

Run the Streamlit application to start the interactive interactive dashboard:

```bash
uv run streamlit run ui/streamlit_ui.py
# Or, if the virtual environment is already activated:
streamlit run ui/streamlit_ui.py
```

1. Open the provided local URL in your web browser (usually `http://localhost:8501`).
2. Enter the **Job Description** in the designated text area.
3. Upload the **Candidate Resume (PDF)**.
4. Click the evaluate button to receive a comprehensive, AI-generated candidate assessment.

## 🔮 Future Enhancements

- [ ] **Dynamic UI Configuration**: Allow users to input their API keys and select their preferred LLM models (OpenAI, DeepSeek, Llama, etc.) globally directly via the web interface without modifying code.
- [ ] **Batch Processing**: Support for analyzing multiple resumes simultaneously against a single job description to rank candidates.
- [ ] **Export Options**: Export the evaluation results to PDF or CSV formats for easy sharing and reporting.
