from .type_check import TypeChecker, FileType 
from .text_clean import clean_text 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from ragchain.embedding_models.embedding_models_registry import EmbeddingRegistry 
from ragchain.vector_store.vector_store import VectorStore 


class Injustor:
    def __init__(self):
        self.type_checker = TypeChecker() 
        self.embRegistry = EmbeddingRegistry()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 100,
                ) 

    def embed(self, path : str, vector_store : VectorStore):
        data_type = self.type_checker.check(path) 
        if data_type == FileType.TEXT:
            with open(path, "r") as f:
                cleaned_text=clean_text(f.read())
                splits = self.text_splitter.split_text(text=cleaned_text)
                _ = Chroma.from_texts(
                        texts=splits,
                        embedding=self.embRegistry.get_current_text_model(),
                        persist_directory=vector_store.get_path())

                
