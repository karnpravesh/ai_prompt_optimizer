import openai
from config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"ERROR: {str(e)}"
