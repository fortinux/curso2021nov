# Ejemplo break
# Verifica si un número es primo
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equivale a', x, '*', n//x)
            break
    else:
        # El bucle sigue sin encontrar un factor
        print(n, 'es un número primo')