# _*_ encoding: utf-8 _*_

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
