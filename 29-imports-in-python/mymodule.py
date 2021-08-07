#__name__ cambia segun el archivo en el que se encuentre
#es util porque identifica el archivo que ejecuta y el que importa

def divide (dividend, divisor):
    return dividend / divisor

print("mymodule.py: ", __name__)