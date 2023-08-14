texto = input("informe um texto: ")
VOGAIS= "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()
print("aqui esta o texto sem as consoantes")


