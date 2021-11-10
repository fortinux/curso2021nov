# ejemplo función lambda
# def multiplicar(x, y):
#    return x * y
#
# print(multiplicar(5,5))

multiplicar_lambda = lambda x, y: x * y
print(multiplicar_lambda(5,8))

print(f'{(lambda x: x*2)(5)}')