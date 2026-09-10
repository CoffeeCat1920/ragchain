from . import type_check

class Injustor:
    def __init__(self):
        self.type_checker = type_check.TypeChecker() 

    def _check_type(self, path : str):
        self.type_checker.type_check(path)
