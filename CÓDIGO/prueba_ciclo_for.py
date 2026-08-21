contador= 0  

for contador in range(5,0,-1):
    print("El valor del contador es:", contador)
else:
    print("El ciclo for ha terminado")


lista = []
limite = 3
print (f"ingresa los elementos en la lista, ten en cuenta que el limite es {limite}")

for i in range(limite):
    valor= input(f"escribe los elementos de tu lista {i+1}:")
    lista.append(valor)

for elemento in lista:
    if elemento == "hola":
        print (f"se encontro el elemento {elemento} en la lista")
        break   