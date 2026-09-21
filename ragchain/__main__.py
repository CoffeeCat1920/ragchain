from .llm_model.llm_registry import LLMModelRegistry 
from .query_translator.query_translator import QueryTranslation
from ragchain.vector_store.vector_store import VectorStore

def main() -> None:
    llm_registry=LLMModelRegistry() 
    llm=llm_registry.current_text_model()
    vectorstore=VectorStore("chroma_db")
    vectorstore.injust("/home/ok/Code/AI/new_thing/LangChain/assets/tingumingu.txt")
    query_translator=QueryTranslation()
    queries=query_translator.multi_query("What is Internet Protocol", 4)
    context=vectorstore.multiquery_retrieve(queries=queries, k=3)
    print(*context, "\n")
    answer=llm.invoke_context_query(query="If Tingu and Mingu were both placed in an environment with direct sunlight, prolonged water exposure, and a strong magnetic field, which properties of each object would become relevant, and what trade-offs would there be when choosing between them?", context=context)
    print(answer)

if __name__ == "__main__":
    main()
