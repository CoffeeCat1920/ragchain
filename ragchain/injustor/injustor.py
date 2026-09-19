from .text_clean import clean_text
from langchain_core.embeddings import Embeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

class Injustor():
    def __init__(self, path : str, embModel : Embeddings):
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 100,
            ) 
        self._vectorstore = Chroma(
            persist_directory=path,
            embedding_function=embModel,
            ) 

    def injust(self, path : str):
        with open(path, "r") as f:
            cleaned_text=clean_text(f.read())
            splits=self._text_splitter.split_text(cleaned_text) 
            self._vectorstore.add_texts(splits)

