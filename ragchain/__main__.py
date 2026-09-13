from .injustor import injustor
from .vector_store.vector_store import VectorStore

def main():
    _injustor = injustor.Injustor()
    _vector_store = VectorStore("chroma_db")
    print(_injustor.embed("assets/green_lantern_lore.txt", vector_store=_vector_store))

if __name__ == "__main__":
    main()
