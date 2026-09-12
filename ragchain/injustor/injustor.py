from .type_check import TypeChecker, FileType 

class Injustor:
    def __init__(self):
        self.type_checker = TypeChecker() 

    def embed(self, path : str):
        data_type = self.type_checker.check(path) 

        if data_type == FileType.TEXT:
            pass
