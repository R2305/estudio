import math

print("dame un numero")
numero1 = int(input())
print("dame otro numero")
numero2 = int(input())

print("\nelige una operacion")
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
print("5.raiz cuadrada")
print("6.potencia")
print("7.seno")
print("8.coseno")
print("9.tangente\n")

suma = numero1 + numero2

opcion = int(input())
if opcion == 1:
    print("la suma es: ", suma)
elif opcion == 2:
    print("la resta es: ", numero1 - numero2)
elif opcion == 3:
    print("la multiplicacion es: ", numero1 * numero2)
elif opcion == 4:
    if numero2 != 0:
        print("la division es: ", numero1 / numero2)
    else:
        print("no se puede dividir entre cero")
elif opcion == 5:
    print("la raiz cuadrada de ", numero1, " es: ", numero1 ** 0.5)
    print("la raiz cuadrada de ", numero2, " es: ", numero2 ** 0.5)
elif opcion == 6:
    print("la potencia de ", numero1, " es: ", math.pow(numero1, 2))
    print("la potencia de ", numero2, " es: ", math.pow(numero2, 2))
elif opcion == 7:
    print("el seno de ", numero1, " es: ", math.sin(numero1))
    print("el seno de ", numero2, " es: ", math.sin(numero2))

