from pydantic import BaseModel

from .llm_model.llm_registry import LLMModelRegistry 

class Format(BaseModel):
    answers: list[str] 

def main() -> None:
    llm_registry = LLMModelRegistry() 
    text_llm = llm_registry.current_text_model()
    answers=Format.model_validate(text_llm.invoke_json("Generate 3 stepback queries for the following question: How to train cat not to pee everywhere all the time??", Format))
    print(*answers.answers, sep="\n")

if __name__ == "__main__":
    main()
