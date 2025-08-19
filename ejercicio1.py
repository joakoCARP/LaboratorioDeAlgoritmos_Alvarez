nombres = ["felipe", "gabriel", "esteban", "lautaro", "ezequiel", "brisa", "bianca", "rolon", "martin", "daniel"]

mayor = ""
for nombre in nombres:
    if len(nombre) > len(mayor):
        mayor = nombre

print(f"la palabra con mas caracteres es {mayor}")
