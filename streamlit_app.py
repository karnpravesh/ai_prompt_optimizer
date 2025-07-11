import streamlit as st
from app.generator import generate_variations
from app.model_client import get_response
from app.evaluator import evaluate_response
from app.scorer import score_prompt
from app.rag_pipeline import build_index, query_index

st.title("🧠 AI Prompt Optimizer")

base_prompt = st.text_area("Enter your base prompt")
use_rag = st.checkbox("Use RAG Context")

if st.button("Optimize Prompt") and base_prompt:
    if use_rag:
        build_index()
        context = query_index(base_prompt)
        base_prompt = f"{context}\n\n{base_prompt}"

    variants = generate_variations(base_prompt)
    results = []
    with st.spinner("Generating responses..."):
        for var in variants:
            response = get_response(var)
            evaluation = evaluate_response(response)
            score = score_prompt(var, evaluation)
            results.append((var, score, response))

    st.subheader("📊 Ranked Prompt Variants")
    results.sort(key=lambda x: x[1], reverse=True)
    for i, (prompt, score, response) in enumerate(results, start=1):
        st.markdown(f"### {i}. Score: {score}")
        st.code(prompt, language='markdown')
        st.success(response)
