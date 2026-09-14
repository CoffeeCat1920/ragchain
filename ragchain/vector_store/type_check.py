from enum import Enum, auto
import mimetypes

class FileType(Enum):
    TEXT = auto() 
    IMG = auto()
    OTHER = auto()

class TypeChecker():
    Text_list = {"txt", "org", "md"} 
    Img_list = {"png", "jpg"}

    def __init__(self) -> None:
        pass

    def check(self, path : str) -> FileType:
        mime, _ = mimetypes.guess_type(path)

        if mime is None:
            return FileType.OTHER
        
        if mime.startswith("text/"):
            return FileType.TEXT  

        if mime.startswith("image/"):
            return FileType.IMG

        return FileType.OTHER
