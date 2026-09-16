from abc import ABC, abstractmethod

class LLMBase(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def invoke(self, _ : str) -> str:
        pass
