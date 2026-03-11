# ============================================================
# CONTEXTO DEL EJERCICIO
# ============================================================
# Eres un profesor de desarrollo de software, experto en Python,
# con más de 5 años de experiencia en Python y análisis de datos.
# Ahora soy un estudiante de programación que está aprendiendo
# programación en Python, quiero que seas mi profesor y me ayudes
# a hacer el siguiente ejercicio, no quiero que me des todo,
# vamos a hacerlo juntos porque quiero aprender y quiero entender
# muy bien el ejercicio, ya que lo debo presentar.
# Si hay conceptos nuevos quiero que me expliques.
#
# CONTEXTO:
# Una empresa de servicios públicos quiere un prototipo en Python
# para gestionar lecturas numéricas y datos básicos de usuarios.
# El objetivo del taller es practicar listas, diccionarios,
# métodos de listas y funciones (def), junto con un flujo simple
# de registro/login con intentos limitados.
#
# OBJETIVO DE APRENDIZAJE:
# Al finalizar, el estudiante será capaz de:
# - Construir soluciones con funciones y flujo de control.
# - Gestionar listas con métodos: append, insert, remove, pop, sort.
# - Trabajar con lista de diccionarios (mínimo 10 registros).
# - Implementar un login/registro con control de intentos.
# - Generar y procesar un volumen de datos (500 registros numéricos).
#
# REQUISITOS:
# 1) Registro y Login (con 3 intentos)
#    - Registro: correo, password, guardar en lista de diccionarios
#    - Login: máximo 3 intentos, mensaje de intentos restantes,
#      "Cuenta bloqueada temporalmente" si se agotan los intentos
# 2) Lista usuarios_servicio con 10 diccionarios:
#    - id, nombre, documento, estrato, consumoEnergetico (30 valores), estado
#    - Menú para ordenar usuarios por consumo de menor a mayor
# ============================================================

import random

# ============================================================
# LISTAS GLOBALES
# ============================================================
usuarios = []  # lista para almacenar usuarios registrados

usuarios_servicio = []  # lista para almacenar usuarios del servicio
for i in range(1, 11):  # creamos 10 usuarios
    usuario = {
        "id": i,
        "nombre": f"Usuario {i}",
        "documento": f"{100000000 + i}",
        "estrato": random.randint(1, 6),
        "consumoEnergetico": [random.randint(50, 500) for _ in range(30)],  # 30 consumos en KWH
        "estado": random.choice(["ACTIVO", "SUSPENDIDO"])
    }
    usuarios_servicio.append(usuario)  # agregamos el usuario a la lista

# ============================================================
# FUNCIONES DE AUTENTICACIÓN
# ============================================================
def registro_usuario():
    correo = input("Ingrese su correo electrónico: ")
    for usuario in usuarios:
        if usuario["correo"] == correo:
            print("El correo ya está registrado. Intente con otro.")
            return
    password = input("Ingrese su contraseña: ")
    usuario = {"correo": correo, "password": password}
    usuarios.append(usuario)
    print("Usuario registrado exitosamente.")

def login_usuario():
    intentos = 3
    while intentos > 0:
        correo = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                print("Inicio de sesión exitoso.")
                return True
        intentos -= 1
        print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
    print("Cuenta bloqueada temporalmente.")
    return False

# ============================================================
# FUNCIONES DE GESTIÓN DE USUARIOS DEL SERVICIO
# ============================================================
def mostrar_usuarios():
    print("\n--- Usuarios del Servicio ---")
    for u in usuarios_servicio:
        print(f"ID: {u['id']} | Nombre: {u['nombre']} | Doc: {u['documento']} | "
              f"Estrato: {u['estrato']} | Estado: {u['estado']} | "
              f"Consumo total: {sum(u['consumoEnergetico'])} KWH")

def ordenar_por_consumo():
    # sorted() ordena la lista de menor a mayor según la suma de consumos
    usuarios_ordenados = sorted(usuarios_servicio, key=lambda u: sum(u["consumoEnergetico"]))
    print("\n--- Usuarios ordenados por consumo (menor a mayor) ---")
    for u in usuarios_ordenados:
        print(f"ID: {u['id']} | Nombre: {u['nombre']} | Consumo total: {sum(u['consumoEnergetico'])} KWH")

# ============================================================
# MENÚS
# ============================================================
def menu_gestion():
    while True:
        print("\n--- Gestión de Usuarios del Servicio ---")
        print("1. Mostrar usuarios")
        print("2. Ordenar por consumo (menor a mayor)")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_usuarios()
        elif opcion == "2":
            ordenar_por_consumo()
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_principal():
    print("╔══════════════════════════════╗")
    print("║    SERVICIOS PÚBLICOS S.A.   ║")
    print("╚══════════════════════════════╝")
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registro_usuario()
        elif opcion == "2":
            if login_usuario():
                menu_gestion()  # si el login es exitoso, mostramos el menú de gestión
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# ============================================================
# INICIO DEL PROGRAMA
# ============================================================
menu_principal()