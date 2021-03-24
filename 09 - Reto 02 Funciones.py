def bienvenida_general():
    print("Welcome")
    print("Julio")

bienvenida_general()



usuario = "Daniela"

def bienvenido_usuario(usuario):
    print(f"Bienvenido {usuario}")

bienvenido_usuario(usuario)

def bienvenido_usuario(usuario):
    return usuario

empleado = bienvenido_usuario("Julio")

print(empleado)