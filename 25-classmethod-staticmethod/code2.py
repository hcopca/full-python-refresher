class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    #Permite crear un libro con los mismos parametros
    def __repr__(self):
        return f"<Book{self.name}, {self.book_type}, {self.weight}g>"

    #Permite devolver un libro con nombre, y TYPES como primer y segundo argumento
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

#Se está agregando un libro a la funcion dentro de la clase Book, con los 3 parametros que solicitan
book = Book("Harry P", "hardcover", 1500)
print(book.name)

##Se IMPRIME EL LIBRO DOS, SACANDO LOS ARGUMENTOS DEL CLASSMETHOD CON HARDCOVER COMO TYPE
book2 = Book.hardcover("Harry Potter", 1500)
print(book2)

light = Book.paperback("Python", 1700)
print(light)