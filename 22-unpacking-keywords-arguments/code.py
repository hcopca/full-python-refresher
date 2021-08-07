#Los asteriscos se usan para recibir un numero ilimitado de argumentos
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3, 5, name="Bob", age=35)