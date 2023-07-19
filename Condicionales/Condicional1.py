#Programa que pide al usuario que digite dos numeros

x=input('ingrese numero')
y=input('ingrese numero')

#Usaremos las condicionales if, elif y else

if x==y:
    print('son iguales')
#Si se cumple quiere decir que los numeros son Descendente     

elif x>y:
    print('descendente')

#Si no se cumple quiere decir que los numeros son Ascendentes

else:
    print('ascendente')