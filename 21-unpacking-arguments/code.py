def multiply (*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    
    return total

print (multiply(1, 3, 5))


def apply (*args, operator):
    if operator == "*":
        return multiply (args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operators"

print(apply(1,2,3,4,5, operator="+"))
