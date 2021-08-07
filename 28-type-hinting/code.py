from typing import List

class Book:
    pass

#List es lo que debería devolver BookShelf, para evitar errores y sepa el código que debe devolver
class BookShelf :
    def __init__(self, books: List[Book]):
        self.books = books

    #str quiere decir que debería devolver una string
    def __str__(self) -> str:
        return f"BookShelf with{len(self.books)} books."