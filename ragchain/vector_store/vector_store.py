from .type_check import TypeChecker, FileType 
from .text_clean import clean_text
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ragchain.embedding_models.embedding_models_registry import EmbeddingRegistry
from langchain_core.documents import Document

class VectorStore():
    def __init__(self, path : str) -> None:
        self._path = path 
        self._typeChecker = TypeChecker()
        self._embeddingRegistry = EmbeddingRegistry() 
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 100,
            ) 
        self._vectorstore = Chroma(
            persist_directory=self._path,
            embedding_function=self._embeddingRegistry.get_current_text_model(),
        )
    
    def injust(self, path : str) -> None:
        dataType = self._typeChecker.check(path)

        if dataType == FileType.TEXT:
            with open(path, "r") as f:
                cleaned_text = clean_text(f.read())
                splits = self._text_splitter.split_text(text=cleaned_text) 
                self._vectorstore.add_texts(splits)


    def retrieve(self, query : str, k : int) -> list[Document]: 
        results = self._vectorstore.similarity_search(query=query, k=k)
        return results
