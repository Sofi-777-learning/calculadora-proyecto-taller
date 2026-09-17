"""
Calculadora de Gastos Personales
Proyecto de práctica para el taller de Git y GitHub.
"""

gastos = []


def agregar_gasto():
    descripcion = input("Descripción del gasto: ")
    monto = float(input("Monto ($): "))
    categoria = input("Categoría (ej: comida, transporte, ocio): ")
    gastos.append({
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria
    })
    print(f"Gasto '{descripcion}' agregado correctamente.\n")


def listar_gastos():
    if not gastos:
        print("No hay gastos registrados todavía.\n")
        return
    print("\n--- Lista de Gastos ---")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. {gasto['descripcion']} - ${gasto['monto']:.2f} "
              f"({gasto['categoria']})")
    print()


def calcular_total():
    total = sum(gasto["monto"] for gasto in gastos)
    print(f"Total gastado: ${total:.2f}\n")


def menu():
    while True:
        print("=== Calculadora de Gastos Personales ===")
        print("1. Agregar gasto")
        print("2. Ver lista de gastos")
        print("3. Ver total gastado")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_gasto()
        elif opcion == "2":
            listar_gastos()
        elif opcion == "3":
            calcular_total()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")


if __name__ == "__main__":
    menu()
