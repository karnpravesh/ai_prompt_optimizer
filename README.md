# AI Prompt Optimizer with RAG + Redis + Streamlit

This app takes a base prompt, generates multiple variations, sends them to a language model (e.g., GPT-4), evaluates their responses, and ranks them by performance.

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Redis:
```bash
docker-compose up -d
```

3. Run the UI:
```bash
streamlit run streamlit_app.py
```