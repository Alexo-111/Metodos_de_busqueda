# ---------------------------------------------------------------
# 1. BÚSQUEDA SECUENCIAL
# Recorre la lista elemento por elemento hasta encontrar el valor.
# No requiere que la lista esté ordenada. Complejidad: O(n)
# ---------------------------------------------------------------
def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        print(f"   Comparando posición {i}: {lista[i]}")
        if lista[i].lower() == objetivo.lower():
            return i
    return -1


def ejemplo_secuencial():
    print("\n=== BÚSQUEDA SECUENCIAL ===")
    alumnos = ["Ana", "Luis", "María", "Carlos", "Sofía", "Jorge", "Lucía"]
    print("Lista de alumnos:", alumnos)
    nombre = input("Escribe el nombre del alumno a buscar: ").strip()

    posicion = busqueda_secuencial(alumnos, nombre)
    if posicion != -1:
        print(f"\n✔ '{nombre}' fue encontrado en la posición {posicion}.")
    else:
        print(f"\n✘ '{nombre}' no se encuentra en la lista.")


# ---------------------------------------------------------------
# 2. BÚSQUEDA BINARIA
# Requiere lista ORDENADA. Divide la lista a la mitad en cada paso.
# Complejidad: O(log n)
# ---------------------------------------------------------------
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    paso = 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        print(f"   Paso {paso}: inicio={inicio}, fin={fin}, "
              f"medio={medio} -> valor {lista[medio]}")
        if lista[medio] == objetivo:
            return medio
        elif objetivo < lista[medio]:
            fin = medio - 1      # buscar en la mitad izquierda
        else:
            inicio = medio + 1   # buscar en la mitad derecha
        paso += 1
    return -1


def ejemplo_binaria():
    print("\n=== BÚSQUEDA BINARIA ===")
    matriculas = [1005, 1012, 1020, 1034, 1047, 1051, 1068, 1075, 1089, 1096]
    print("Matrículas (ordenadas):", matriculas)
    try:
        objetivo = int(input("Escribe la matrícula a buscar: "))
    except ValueError:
        print("✘ Debes escribir un número entero.")
        return

    posicion = busqueda_binaria(matriculas, objetivo)
    if posicion != -1:
        print(f"\n✔ La matrícula {objetivo} fue encontrada en la posición {posicion}.")
    else:
        print(f"\n✘ La matrícula {objetivo} no se encuentra en la lista.")


# ---------------------------------------------------------------
# 3. BÚSQUEDA HASH
# Se usa una función hash que convierte la clave en un índice de
# una tabla. Las colisiones se resuelven con encadenamiento
# (cada posición guarda una lista). Complejidad promedio: O(1)
# ---------------------------------------------------------------
class TablaHash:
    def __init__(self, tamano=7):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def funcion_hash(self, clave):
        # Suma de los códigos ASCII de la clave, módulo el tamaño
        return sum(ord(c) for c in clave) % self.tamano

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        for par in self.tabla[indice]:
            if par[0] == clave:
                par[1] = valor   # actualizar si ya existe
                return
        self.tabla[indice].append([clave, valor])

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        print(f"   hash('{clave}') = {indice}")
        for par in self.tabla[indice]:
            if par[0] == clave:
                return par[1]
        return None

    def mostrar(self):
        for i, cubeta in enumerate(self.tabla):
            print(f"   [{i}] -> {cubeta}")


def ejemplo_hash():
    print("\n=== BÚSQUEDA HASH ===")
    tabla = TablaHash(7)
    productos = {
        "manzana": 18.50,
        "leche": 25.00,
        "pan": 12.75,
        "huevo": 38.00,
        "arroz": 22.30,
        "frijol": 28.90,
        "queso": 95.00,
    }
    for producto, precio in productos.items():
        tabla.insertar(producto, precio)

    print("Tabla hash de productos:")
    tabla.mostrar()

    clave = input("\nEscribe el producto a buscar: ").strip().lower()
    precio = tabla.buscar(clave)
    if precio is not None:
        print(f"\n✔ '{clave}' cuesta ${precio:.2f}")
    else:
        print(f"\n✘ El producto '{clave}' no existe en la tabla.")


# ---------------------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------------------
def menu():
    while True:
        print("\n" + "=" * 40)
        print("      MÉTODOS DE BÚSQUEDA")
        print("=" * 40)
        print("1. Búsqueda secuencial")
        print("2. Búsqueda binaria")
        print("3. Búsqueda hash")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            ejemplo_secuencial()
        elif opcion == "2":
            ejemplo_binaria()
        elif opcion == "3":
            ejemplo_hash()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("✘ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
