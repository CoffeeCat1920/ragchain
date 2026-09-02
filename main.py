from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def main():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    query = "What is a Green Lantern?"
    results = vectorstore.similarity_search(query=query, k=3)


    for result in results:
        print(result.page_content)
        print("---")

if __name__=="__main__":
    main()
