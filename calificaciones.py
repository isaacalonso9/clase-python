# Sistema de calificaciones para estudiantes
def obtener_calificaciones():
    """
    Solicita al usuario ingresar los nombres y calificaciones de los estudiantes.
    Devuelve un diccionario con los datos.
    """
    estudiantes = {}
    try:
        cantidad = int(input("¿Cuántos estudiantes desea ingresar?: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return obtener_calificaciones()
    for i in range(cantidad):
        nombre = input(f"\nIngrese el nombre del estudiante #{i+1}: ").strip()
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación de {nombre} (0-10): "))
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        estudiantes[nombre] = calificacion
    return estudiantes
def mostrar_resultados(estudiantes):
    """
    Muestra las calificaciones y si el estudiante aprobó o no.
    """
    print("\n----- Resultados de los estudiantes -----")
    for nombre, calificacion in estudiantes.items():
        estado = "✅ Aprobado" if calificacion >= 6.0 else "❌ Reprobado"
        print(f"{nombre}: {calificacion:.2f} - {estado}")
def calcular_promedio(estudiantes):
    """
    Calcula el promedio general del grupo.
    """
    if len(estudiantes) == 0:
        return 0
    total = sum(estudiantes.values())
    return total / len(estudiantes)
def main():
    """
    Función principal del programa.
    """
    print("=== Sistema de Calificaciones ===")
    estudiantes = obtener_calificaciones()
    mostrar_resultados(estudiantes)
    promedio = calcular_promedio(estudiantes)
    print(f"\n📊 Promedio general del grupo: {promedio:.2f}")
# Ejecutar el programa
if __name__ == "__main__":
    main()
  