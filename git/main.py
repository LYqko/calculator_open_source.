from sumar import sumar
from resta import restar
from dividir import dividir
from multiplicacion import  multiplicar
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Sumar N números")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print(f"Resultado: {sumar(a, b)}")

        elif opcion == '2':
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print(f"Resultado: {restar(a, b)}")

        elif opcion == '3':
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print(f"Resultado: {(a, b)}")

        elif opcion == '4':
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            try:
                print(f"Resultado: {dividir(a, b)}")
            except ValueError as e:
                print(e)

        elif opcion == '5':
            nums = input("Introduce los números separados por espacios: ")
            lista = list(map(float, nums.split()))
            print(f"Resultado: {suma_avanzada(*lista)}")

        elif opcion == '6':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()