from .llm_model.llm_registry import LLMModelRegistry 

def main() -> None:
    llm_registry = LLMModelRegistry() 
    text_llm = llm_registry.current_text_model()
    print(text_llm.invoke("How to write hi in chinese?"))
    

if __name__ == "__main__":
    main()
