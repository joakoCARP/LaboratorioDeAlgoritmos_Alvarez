frase = input("ingrese una frase")
vocales = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print(f"la frase tiene {contador} vocales")
