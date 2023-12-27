                                                                  Llama-2 QA System Documentation
Overview
This document provides a concise guide for the Llama-2 Question-Answering (QA) System, developed to facilitate team knowledge building through scientific publications. The system uses Meta's Llama-2 technology and is designed to answer questions based on relevant research papers.

Usage

1. Installation: 
pip install -r requirements.txt

2. Running the System:
python Q&A system code.py

Input:
The system prompts the user to enter a question related to Llama-2.

Output:
The system provides information about the most relevant paper from the ArXiv database based on the input question.

Requirements
Ensure the following libraries are installed:

urllib3
xmltodict
sentence-transformers

Code Structure
main.py: Entry point for running the QA system.
fetch_papers.py: Fetches papers from ArXiv using the provided code snippet.
embeddings.py: Generates embeddings using OpenAI Sentence Transformers.
qa_system.py: Implements the question-answering mechanism.

Sample Questions
The system has been tested with sample questions such as:
"For which tasks has Llama-2 already been used successfully? What are promising areas of application for Llama-2?"
"Name at least 5 domain-specific LLMs that have been created by fine-tuning Llama-2."
"What can you find out about the model structure of Llama-2 (required memory, required computing capacity, number of parameters, available quantizations)?"

Testing
The system has been tested against sample questions to ensure accurate and relevant answers.
