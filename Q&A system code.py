import os
import urllib.request
import xml.etree.ElementTree as ET
from sentence_transformers import SentenceTransformer, util

# Fetch papers from ArXiv API
def fetch_papers():
    url = 'http://export.arxiv.org/api/query?search_query=ti:llama&start=0&max_results=70'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    root = ET.fromstring(data)

    papers_list = []

    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        paper_info = f"Title: {title}\nSummary: {summary}\n"
        papers_list.append(paper_info)

    return papers_list

# Generate embeddings using sentence-transformers
def generate_embeddings(texts, model):
    embeddings = model.encode(texts)
    return embeddings

# Answer questions based on embeddings
def answer_questions(embeddings, model, question):
    question_embedding = model.encode(question)
    similarities = util.pytorch_cos_sim(embeddings, question_embedding)

    # Get the index of the most similar paper
    most_similar_index = similarities.argmax().item()
    most_similar_paper = embeddings[most_similar_index]

    return most_similar_index

if __name__ == "__main__":
    # Fetch papers from ArXiv
    papers = fetch_papers()

    # Load sentence-transformers model
    model = SentenceTransformer('bert-base-nli-mean-tokens')

    # Generate embeddings for the papers using sentence-transformers
    embeddings = generate_embeddings(papers, model)

    # Answer sample questions
    sample_questions = [
        "For which tasks has Llama-2 already been used successfully? What are promising areas of application for Llama-2?",
        "Name at least 5 domain-specific LLMs that have been created by fine-tuning Llama-2.",
        "What can you find out about the model structure of Llama-2 (required memory, required computing capacity, number of parameters, available quantizations)?"
    ]

    for question in sample_questions:
        most_similar_index = answer_questions(embeddings, model, question)
        most_similar_paper_text = papers[most_similar_index]
        print(f"Question: {question}\nMost Similar Paper: {most_similar_paper_text}\n")
