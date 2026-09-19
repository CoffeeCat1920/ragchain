from .llm_model.llm_registry import LLMModelRegistry 
from .query_translator.query_translator import QueryTranslation
from ragchain.vector_store.vector_store import VectorStore

def main() -> None:
    llm_registry=LLMModelRegistry() 
    llm=llm_registry.current_text_model()
    vectorstore=VectorStore("chroma_db")
    # vectorstore.injust("/home/ok/Code/AI/new_thing/LangChain/assets/791.txt")
    query_translator=QueryTranslation()
    queries=query_translator.multi_query("What is Internet Protocol", 4)
    context=vectorstore.multiquery_retrieve(queries=queries, k=3) 
    answer=llm.invoke_context_query(query="What is Internet Protocol", context=context)
    print(answer)

if __name__ == "__main__":
    main()
