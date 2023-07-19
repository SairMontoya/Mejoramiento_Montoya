# 1. Imprime los números del 1 al 10.

i = 1
while i <= 10:
    print(i)
    i += 1


#2. Imprime los números del 10 al 1.

i = 10
while i >= 1:
    print(i)
    i -= 1


#3. Escriba los números del 1 al 100, pero omita los números que son divisibles por 3.

i = 1
while i <= 100:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1