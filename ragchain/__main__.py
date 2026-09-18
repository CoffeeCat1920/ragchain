from pydantic import BaseModel
from .llm_model.llm_registry import LLMModelRegistry 
from .query_translator.query_translator import QueryTranslation

def main() -> None:
    llm_registry=LLMModelRegistry() 
    text_llm=llm_registry.current_text_model()
    query_translator=QueryTranslation()
    answers=query_translator.multi_query("How to conduct a scienctific experiment and extrapulate results?", 4)
    print(*answers, sep="\n")

if __name__ == "__main__":
    main()
