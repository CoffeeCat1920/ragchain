from abc import ABC, abstractmethod
from pydantic import BaseModel

class LLMBase(ABC):
    def __init__(self, model_name : str):
        pass
    
    @abstractmethod
    def invoke(self, query : str) -> str | None:
        pass

    @abstractmethod
    def invoke_json(self, query: str, format: type[BaseModel]):
        pass
