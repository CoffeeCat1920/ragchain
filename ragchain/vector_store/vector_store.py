from .type_check import TypeChecker, FileType 
from ragchain.embedding_models.embedding_models_registry import EmbeddingRegistry
from langchain_core.documents import Document
from ragchain.injustor.injustor import Injustor 

class VectorStore():
    def __init__(self, path : str) -> None:
        self._path = path 
        self._typeChecker = TypeChecker()
        self._embeddingRegistry = EmbeddingRegistry() 
        self._text_injustor = self._load_text_injustor(path) 

    def _load_text_injustor(self, path: str):
        embModel=self._embeddingRegistry.get_current_text_model()
        if embModel == None:
            raise ValueError(f"Invalid current text embedding model")
        return Injustor(path, embModel)

    def injust(self, path : str) -> None:
        dataType = self._typeChecker.check(path)

        if dataType == FileType.TEXT:
            self._text_injustor.injust(path)

    def retrieve(self, query : str, k : int) -> list[Document]: 
        results = self._text_injustor._vectorstore.similarity_search(query=query, k=k)
        return results

    def multiquery_retrieve(self, queries : list[str], k : int) -> list[Document]:
        results : list[Document] = [] 
        for query in queries:
            new_result = self._text_injustor._vectorstore.similarity_search(query, k)
            results.extend(new_result)
        results = self._remove_duplicates(results)
        return results 
    
    def _remove_duplicates(self, documents: list[Document]) -> list[Document]:
        unique_documents = list({doc.page_content: doc for doc in documents}.values())
        return unique_documents
