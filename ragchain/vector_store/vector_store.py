class VectorStore():
    def __init__(self, path : str) -> None:
        self._path = path 

    def get_path(self):
        return self._path
