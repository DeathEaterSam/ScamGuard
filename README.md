# ScamGuard
Enhancing Online Safety with Scam Detection and LLM-based Explanation Insights

## Problem Motivation
### Identified Problem: 
The rise in online scams across various communication channels, be it text or audio, poses significant risks to individuals, exploiting vulnerabilities with sophisticated deceit tactics. The digital landscape in Pakistan, like in many parts of the world, is increasingly marred by the prevalence of online scams. These scams exploit a wide range of communication channels, from social media platforms to SMS and emails, targeting unsuspecting individuals.This trend underlines an urgent need for innovative preventive measures and educating users about these scams.
### Relevance: 
As digital interactions become increasingly central to our daily lives, the prevalence of scams[1] threatens not only individual security but also undermines trust in digital communication platforms. With a rapidly growing internet user base, Pakistan faces unique challenges in digital literacy and cybersecurity awareness. The digital finance sector, e-commerce, and online marketplaces are booming, attracting not only genuine business but also fraudulent activities. The lack of widespread awareness and adequate protective measures leaves a significant portion of the population vulnerable to financial and personal exploitation[2][3].
### Potential Impact: 
Developing an effective solution to detect and explain scams can significantly enhance online safety. It can empower users with knowledge and tools to identify potential scams, reducing the risk of financial loss and personal harm. This is particularly critical for Pakistan’s diverse demographic, where varying levels of digital literacy exist. Implementing this solution can greatly enhance online safety, educating users about prevalent scams and equipping them with tools to avoid future threats, fostering a vigilant and informed digital community.

## Goal of the Project
### Objective: 
To develop a prototype tool that leverages Large Language Models (LLMs) for scam detection and provides users with comprehensive explanations of the analysis. This tool aims to improve online safety by enabling users to understand and identify scams efficiently.
Angles of Problem Tackled: The project focuses on the detection of scam content and the generation of explanations for the detections, covering both text and audio submissions.
Target Audience: General internet users who interact with digital content through emails, messaging apps, and online platforms.
### Distinctiveness: 
Unlike existing solutions, it goes beyond mere detection by educating users about the nature of scams identified. These explanations are designed to enhance user awareness, foster critical thinking, and empower individuals with the knowledge to recognize and avoid scams in the future. This educational component is central to our approach, making our tool not only a protective measure but also a platform for ongoing digital literacy and safety education.

## Proposed Solution
Our approach to enhancing online safety through scam detection and explanation involves the following steps:
Audio-to-Text Conversion: Utilizing an automatic speech recognition (ASR) system, particularly Whisper, we will convert audio submissions into text. This step ensures that both text and audio submissions undergo the same classification process, as the classification will be performed on text.
Scam Classification: The core of our solution involves classifying the converted text (or directly submitted text) to determine if it is a scam. This classification process will leverage the latest advancements in NLP  to accurately identify potential scams.
Explanation Generation: To aid users in understanding the rationale behind each classification, a Large Language Model (LLM) will be employed to generate clear and detailed explanations. This will not only inform users about the nature of the detected scam but also empower them to make informed decisions regarding their interaction with the content.
### Models and Techniques: 
The project will primarily use open-source model such as Whisper for ASR, NLP techniques  for scam detection, and LLM such as GPT for explanation generation. The concrete techniques (fine-tuning, prompt engineering etc.) will be decided during the research phase of project (Week1,2).
### Model Size Justification: 
The size of the models will be balanced between computational efficiency, cost and the need for high accuracy in detection and natural language understanding. T
Practicality and Usability: The tool will be designed with a focus on user-friendly interfaces and accessibility, ensuring that users without technical backgrounds can easily benefit from its features. The inclusion of detailed explanations for each detection aims to educate users, providing them with the knowledge to avoid scams independently.

## Tentative Timeline
### March
#### Week 1-2 (March 1-14): Project Initiation, Research and Planning
Set up and get familiar with Github.
Decide where to deploy(WebApp, Plugin, etc.)
Research on scam detection techniques, OpenAI API, and Whisper ASR system.
Finalize project specifications, dataset and design workflow.
#### Week 3 (March 15-21): Development Begins
Start development of the Audio-to-Text Conversion feature using Whisper.
Initiate the scam classifier development.
#### Week 4 (March 22-31): Prototype Development
Continue with the development of Scam Classifier..
Begin integration of LLM(GPT) for Explanation Generation.
### April
#### Week 1-2 (April 1-14): Testing and Refinement
Initial testing and refinement of scam detection algorithms based on test results.
Integrate Explanation Generation feature.
Comprehensive testing of the full system.
#### Week 3 (April 15-24): User Feedback and Adjustments
Conduct user testing with a small group and make necessary adjustments based on feedback.
Final Report

## References
[1] Atkins, Brandon, and Wilson Huang. "A study of social engineering in online frauds." Open Journal of Social Sciences 1.03 (2013): 23.
[2] Pervaiz, Fahad, et al. "An assessment of SMS fraud in Pakistan." Proceedings of the 2nd ACM SIGCAS Conference on Computing and Sustainable Societies. 2019.
[3] Ullah, Sultan, et al. "Pakistan and cyber crimes: Problems and preventions." 2015 First International Conference on Anti-Cybercrime (ICACC). IEEE, 2015.
