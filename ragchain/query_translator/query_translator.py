from ragchain.llm_model.llm_registry import LLMModelRegistry 
from pydantic import BaseModel

class Queries(BaseModel):
    queries: list[str]

class QueryTranslation():
    def __init__(self) -> None:
        self.llm_registry = LLMModelRegistry() 
        self.llm = self.llm_registry.current_text_model()
    
    def multi_query(self,  query: str, n: int) -> list[str]:
        full_query = f"Create {n} number of step back prompts for the following query: \n {query}" 
        print(full_query)
        queries = Queries.model_validate(self.llm.invoke_json(full_query, Queries))
        return queries.queries
