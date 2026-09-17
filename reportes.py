"""
Módulo de reportes - Funcionalidad agregada en la rama 'feature-reportes'
"""


def reporte_por_categoria(gastos):
    """Agrupa y muestra el total gastado por cada categoría."""
    resumen = {}
    for gasto in gastos:
        categoria = gasto["categoria"]
        resumen[categoria] = resumen.get(categoria, 0) + gasto["monto"]

    print("\n--- Reporte por Categoría ---")
    for categoria, total in resumen.items():
        print(f"{categoria}: ${total:.2f}")
    print()
