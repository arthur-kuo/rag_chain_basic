# :call_me_hand: RAG Chain -- Basic 
 
A very basic RAG application, using Langchain and Chroma. It can be used in many different circumstance like work-report agent for your company, or a chat bot of a online shop. 
For the demonstration, I use it to manage the resumes of the candidates. You can ask any question about any candidate to find the one who fits the role (e.g., senior full stack engineer) most.

![screenshot](https://github.com/arthur-kuo/rag_chain_basic/blob/main/images/outcome.png)

## To Install

You can clone this repository and use `pip install -r requirements.txt` to get the required modules

## To Use
Use python to run 'main.py' file in your CLI(Command-line interface)

## Specification

- Chat Model: GPT-4o  # Recommand
- Embedding Model: text-embedding-3-large  # Recommand
- Vector DB: Chroma==0.5.2
- Python Version: >=3.11
