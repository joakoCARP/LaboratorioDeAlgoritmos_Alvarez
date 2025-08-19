nombres = ["felipe", "gabriel", "esteban", "lautaro", "ezequiel", "brisa", "bianca", "rolon", "martin", "daniel"]

vocales = "aeiouAEIOU"
contador = 0
for nombre in nombres:
    for letra in nombre:
        if letra in vocales:
            contador += 1

print(f"las vocales totales son {contador}")
