from .vector_store.vector_store import VectorStore 

def main() -> None:
    _vector_store = VectorStore("chroma_db")
    print(_vector_store.injust("assets/green_lantern_lore.txt"))
    results = _vector_store.retrieve("What is an green lantern?", 3)
    for result in results:
        print(result.page_content)
        print("-----------------")
    

if __name__ == "__main__":
    main()
