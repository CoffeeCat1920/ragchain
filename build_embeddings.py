import re
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

def clean_text(text):
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def main():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    with open("test.txt", "r") as f:
        cleaned_text = clean_text(f.read())
        green_lantern_chunks = splitter.split_text(text=cleaned_text)

    _ = Chroma.from_texts(
        texts=green_lantern_chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print(f"Stored {len(green_lantern_chunks)} chunks in chroma_db")

if __name__ == "__main__":
    main()
