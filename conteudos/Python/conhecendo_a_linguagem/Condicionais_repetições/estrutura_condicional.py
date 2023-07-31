MAIOR_DE_IDADE  = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

    
if idade >=MAIOR_DE_IDADE:
    print("você pode fazer as aulas para tirar sua CNH")
elif idade >= IDADE_ESPECIAL:
    print("você pode fazer as aulas teoricas, mas não as praticas")
else:
    print("vocẽ não pode realizar a aula teorica ou pratica")     