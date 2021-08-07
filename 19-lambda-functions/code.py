#Lambda se compone por el nombre que va a recibir en la variable, lambda, parametros, :, y el retorno
add = lambda x, y: x + y
print(add(8,9))

#Esta es otra forma de hacerlo pero no se recomienda debido a que es confuso
print((lambda a, b: a*b)(10, 5))

##
# def double (x):
#     return x * 2

# sequence = [1, 3, 5, 9]

# double = [double(x) for x in sequence]
# double = map(double, sequence)

##LAMBDA EN MAP

sequence = [1, 3, 5, 9]
double = [(lambda x: x * 2(x) for x in sequence)]
double = list(map(lambda x: x*2, sequence))
print(double)