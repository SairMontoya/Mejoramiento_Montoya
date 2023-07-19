#Lista de funciones que imprimen los números del 1 al 100, pero omiten los números que son divisibles por 3

def print_numbers(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue
        print(i)
print_numbers(100)

