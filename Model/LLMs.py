import os
from together import Together
from dotenv import load_dotenv
load_dotenv()

TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')

client = Together(api_key=TOGETHER_API_KEY)
models = ["mistralai/Mixtral-8x22B-Instruct-v0.1", "meta-llama/Llama-3-70b-chat-hf","microsoft/phi-2", "togethercomputer/StripedHyena-Nous-7B","allenai/OLMo-7B-Instruct","google/gemma-7b-it"]

def classify_text(text, Model):
    
    """
    Classify the given text as 'scam' or 'not scam' using Together AI's service.
    Args:
    text (str): The text to classify.

    Returns:
    str: The classification result ('scam' or 'not scam').
    str: Explanation for the classification.
    """
    response = client.chat.completions.create(
        model= Model,
        messages=[
        {"role": "system", "content": 'Classify the following text as "scam" or "not scam". If it is a scam, provide a reason why it is a scam. If it is not a scam, provide a reason why it is not a scam. The email might be given in English or Roman Urdu / Hindi.'},
        {"role": "user", "content": text},
    ],
    )
    result = response.choices[0].message.content

    # Split the result into classification and explanation
    print(f"LLM {Model} result obtained")
    return result

from joblib import Parallel, delayed

def get_LLM_Results(text):
    results = Parallel(n_jobs=-1)(delayed(classify_text)(text, model) for model in models)
    return {model: result for model, result in zip(models, results)}



