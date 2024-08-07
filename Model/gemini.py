import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure your API key
genai.configure(api_key=GOOGLE_API_KEY)

def classify_text(text):
    """
    Classify the given text as 'scam' or 'not scam' using Gemini AI's service.
    Args:
        text (str): The text to classify.

    Returns:
        str: The classification result ('scam' or 'not scam').
        str: Explanation for the classification.
    """
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(f"""I want you to act as a scam detector to determine whether a given text is a scam or a legitimate. Your analysis should be thorough and evidence-based. 
                                            Scams often impersonate legitimate brands and use social engineering techniques to deceive users. These techniques include, but are not limited to: fake rewards, fake warnings about account problems, and creating a sense of urgency or interest. 
                                            The following is a dictionary of LLMs alongside their 
                                            classification of some text as 'scam' or 'not scam'. Your job is to calculate 
                                            the percentage of 'scam' classifications and give a consolidated summary of the
                                            results. Make sure the summary includes all the important observations made across the LLMs.
                                            If for example x LLMs classify the text as scam and y classify the text as not scam, then the
                                            percentage is calculated as x/(x+y)*100%.: {str(text)}

                                            Use the following format:
                                            1. [LLM Name]: [LLM Classification]
                                            
                                            2. [LLM Name]: [LLM Classification]
                                            3. [LLM Name]: [LLM Classification]
                                            .
                                            .
                                            Final Accuracy: [Percentage of 'scam' classifications]%
                                            Explanation: [Consolidated Explanation for the classification]
                                            Analyze the text by following these steps:
                                            1. Identify any impersonation of well-known brands.
                                            2. For emails, examine the email header for spoofing signs, such as discrepancies in the sender name or email address. 
                                            3. Evaluate the text for typical scamming characteristics (e.g., urgency, promise of reward). 
                                            4. Analyze the text for social engineering tactics designed to induce clicks on hyperlinks or phone numbers. Inspect URLs to determine if they are misleading or lead to suspicious websites.
                                            5. Provide a comprehensive yet concise evaluation of the text, highlighting specific elements that support your conclusion. Include a detailed explanation of any scam or legitimacy indicators found in the text.
                                            6. Summarize your findings concisely and provide your final verdict on the legitimacy of the text, supported by the evidence you gathered.
                                            You also have results from scam prediction of 5 other LLMS and the input text respectively
                                            <Output of other LLMS as an input to Prompt>
                                            <Input Text>""")
    classification = response.text


    return classification

# Example usage
# text_to_classify = "Congratulations!! You have won a Ferrari LaFerrari! Click to Claim NOW"
# classification = classify_text(text_to_classify)
# print(f"Classification: {classification}")
