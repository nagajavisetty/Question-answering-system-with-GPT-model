# Llama-2 QA System Documentation

This document provides comprehensive documentation for the Llama-2 Question-Answering (QA) System, a tool designed to facilitate team knowledge building through scientific publications. The system utilizes Meta's Llama-2 technology and is tailored to answer questions based on relevant research papers.

## Usage

### Installation
```bash
pip install -r requirements.txt
```

### Running the System
```bash
python main.py
```

#### Input
The system prompts the user to enter a question related to Llama-2.

#### Output
The system provides information about the most relevant paper from the ArXiv database based on the input question.

## Requirements
Ensure the following libraries are installed:

- `urllib3`
- `xmltodict`
- `sentence-transformers`

## Code Structure
- **main.py**: Entry point for running the QA system.
- **fetch_papers.py**: Fetches papers from ArXiv using the provided code snippet.
- **embeddings.py**: Generates embeddings using OpenAI Sentence Transformers.
- **qa_system.py**: Implements the question-answering mechanism.

## Sample Questions
The system has been tested with sample questions such as:
1. "For which tasks has Llama-2 already been used successfully? What are promising areas of application for Llama-2?"
2. "Name at least 5 domain-specific LLMs that have been created by fine-tuning Llama-2."
3. "What can you find out about the model structure of Llama-2 (required memory, required computing capacity, number of parameters, available quantizations)?"

## Testing
The system has undergone rigorous testing against sample questions to ensure accurate and relevant answers.

## Updated Code Explanation

The code provided includes functionalities to fetch papers from ArXiv, generate embeddings using OpenAI Sentence Transformers, and answer questions based on the embeddings. Sample questions are provided for testing, and the system's accuracy is demonstrated.

To run the system, follow the installation and execution instructions provided above. Ensure that the required libraries are installed before running the code. For any issues or inquiries, refer to the documentation or contact the developers.

Happy questioning and exploring with Llama-2 QA System! 📚🦙
