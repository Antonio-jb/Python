import hashlib
import json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def crearMemoria():
    try:
        with open("memoria.json", "x") as file:
            json.dump({}, file)
        return {}
    except FileExistsError:
        try:
            with open("memoria.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            with open("memoria.json", "w") as file:
                json.dump({}, file)
            return {}

users = crearMemoria()

def guardarMemoria():
    with open("memoria.json", "w") as file:
        json.dump(users, file)

def register(username, password):
    if username in users:
        print("El usuario ya está registrado.")
    else:
        users[username] = hash_password(password)
        guardarMemoria()
        print("Usuario registrado con éxito.")

def login(username, password):
    if username in users and users[username] == hash_password(password):
        print("Login exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        print("Intentelo de nuevo.")

while True:
    print("Escriba opción deseada --> 'registro', 'login', 'exit'")
    action = input("").strip().lower()
    if action == 'exit':
        break
    elif action in ['registro', 'login']:
        username = input("Introduce tu nombre de usuario: ").strip().lower()
        password = input("Introduce tu contraseña: ").strip().lower()
        if action == 'registro':
            register(username, password)
        elif action == 'login':
            login(username, password)
    else:
        print("Acción no reconocida. Inténtalo de nuevo.")
