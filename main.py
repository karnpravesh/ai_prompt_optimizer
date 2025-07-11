from app.generator import generate_variations
from app.model_client import get_response
from app.evaluator import evaluate_response
from app.scorer import score_prompt
from app.rag_pipeline import build_index, query_index

if __name__ == "__main__":
    base_prompt = input("Enter your base prompt: ")
    use_rag = input("Use RAG context? (y/n): ").lower() == 'y'

    if use_rag:
        build_index()
        context = query_index(base_prompt)
        base_prompt = f"{context}\n\n{base_prompt}"

    variants = generate_variations(base_prompt)
    results = []
    for var in variants:
        response = get_response(var)
        evaluation = evaluate_response(response)
        score = score_prompt(var, evaluation)
        results.append((var, score))

    results.sort(key=lambda x: x[1], reverse=True)
    for rank, (prompt, score) in enumerate(results, start=1):
        print(f"{rank}. {prompt} --> Score: {score}")
