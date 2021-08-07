def add( x, y):
    print(x+y)

add( 5,5)


#Es posible agrega un valor por defecto, en este caso b=0 pero puede sustituirse con el parametro cuando se llame a la función
def add( a, b=0):
    print(a+b)

add( 5)

##########
#Tambien es posible pasar una variable como valor predeterminado en el parametro de la función
default_y = 40

def add(f, y=default_y):
    sum = f + y
    print(sum)

add(10)