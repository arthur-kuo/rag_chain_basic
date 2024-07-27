# -*- coding: utf-8 -*-
import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from prompt import prefix_prompt
from dependencies.detect_encoding import detect_encoding
from dependencies.format_docs import format_docs
from config import (
    openai_api_key,
    openai_organization
)


llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    openai_organization=openai_organization,
    model="gpt-4o",
    temperature=0.1
)

directory_path = './resumes'
file_paths = [os.path.join(directory_path, file_name) for file_name in os.listdir(directory_path)]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

model = OpenAIEmbeddings(
    openai_api_key=openai_api_key,
    openai_organization=openai_organization,
    model="text-embedding-3-large"  # recommend
)
embedding = model

all_docs = []

for file_path in file_paths:
    encoding = detect_encoding(file_path)
    loader = TextLoader(file_path=file_path, encoding=encoding)
    documents = loader.load()
    docs = text_splitter.split_documents(documents)
    all_docs.extend(docs)
    print(f"{file_path} embedded.")

db = Chroma.from_documents(docs, embedding)

retriever = db.as_retriever()

prompt = ChatPromptTemplate.from_template(prefix_prompt)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

req = input("How may I help you: ")
print("Response:", rag_chain.invoke(req))
