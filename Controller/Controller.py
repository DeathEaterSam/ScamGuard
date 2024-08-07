import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(__file__)

from Model.Whisper import transcribe_audio
from Model.LLMs import get_LLM_Results
from Model.gemini import classify_text as gemini_classify_text



def process_audio_file(audio_path):
    text = transcribe_audio(audio_path)
    
    results = get_LLM_Results(text)
    print("\n\nresults obtained\n\n")
    return text, gemini_classify_text(results)

    


def process_text_file(text):
    
    results = get_LLM_Results(text)
    print("\n\nresults obtained\n\n")
    return gemini_classify_text(results)



