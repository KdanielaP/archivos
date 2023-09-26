import json

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = {"titulo": titulo, "descripcion": descripcion}
    tareas_pendientes.append(tarea)
    print("Tarea agregada con éxito!")

def listar_tareas():
    if len(tareas_pendientes) == 0:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas_pendientes):
            print(f"Tarea {i+1}:")
            print(f"Título: {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
        
def marcar_completada():
    if len(tareas_pendientes) == 0:
        print("No hay tareas pendientes para marcar como completadas.")
    else:
        listar_tareas()
        index = int(input("Ingrese el número de la tarea para marcar como completada: "))
        if index >= 1 and index <= len(tareas_pendientes):
            tarea_completada = tareas_pendientes.pop(index-1)
            tareas_completadas.append(tarea_completada)
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
            
def guardar_datos():
    with open("tareas_pendientes.txt", "w") as file:
        json.dump(tareas_pendientes, file)
    with open("tareas_completadas.txt", "w") as file:
        json.dump(tareas_completadas, file)
    print("Datos guardados correctamente.")
    
def cargar_datos():
    global tareas_pendientes
    global tareas_completadas
    try:
        with open("tareas_pendientes.txt", "r") as file:
            tareas_pendientes = json.load(file)
    except FileNotFoundError:
        tareas_pendientes = []
    try:
        with open("tareas_completadas.txt", "r") as file:
            tareas_completadas = json.load(file)
    except FileNotFoundError:
        tareas_completadas = []
            
def menu():
    print("----- MENÚ -----")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Guardar datos")
    print("5. Cargar datos")
    print("6. Salir")
    opcion = int(input("Ingrese el número de la opción deseada: "))
    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        listar_tareas()
    elif opcion == 3:
        marcar_completada()
    elif opcion == 4:
        guardar_datos()
    elif opcion == 5:
        cargar_datos()
    elif opcion == 6:
        salir()
    else:
        print("Opción inválida.")
    menu()

def salir():
    guardar_datos()
    print("Hasta luego!")
    
tareas_pendientes = []
tareas_completadas = []

cargar_datos()
menu()
