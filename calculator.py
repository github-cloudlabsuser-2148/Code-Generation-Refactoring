def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def mostrar_menu():
    print("\nCalculadora Básica")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def obtener_operacion(opcion):
    operaciones = {
        "1": ("Suma", sumar),
        "2": ("Resta", restar),
        "3": ("Multiplicación", multiplicar),
        "4": ("División", dividir)
    }
    return operaciones.get(opcion, (None, None))

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación: ").strip()
        if opcion == "5":
            print("Saliendo de la calculadora.")
            break

        nombre_op, funcion = obtener_operacion(opcion)
        if funcion is None:
            print("Opción no válida. Intente de nuevo.")
            continue

        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor ingrese números.")
            continue

        resultado = funcion(a, b)
        print(f"Resultado de la {nombre_op.lower()}: {resultado}")

if __name__ == "__main__":
    main()