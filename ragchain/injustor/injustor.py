from .type_check import TypeChecker, FileType 
from ragchain.embedding_models.embedding_models_registry import EmbeddingRegistry 

class Injustor:
    def __init__(self):
        self.type_checker = TypeChecker() 
        self.embRegistry = EmbeddingRegistry()

    def embed(self, path : str):
        data_type = self.type_checker.check(path) 

        if data_type == FileType.TEXT:
            print("---- Embedding Text File ----")
            print("Path:", path)
