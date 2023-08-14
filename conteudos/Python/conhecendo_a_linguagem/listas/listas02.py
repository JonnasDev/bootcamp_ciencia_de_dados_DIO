matriz = [
    
    [1, "a", 2],
    ["b", 3, 4],
    [6,9,"j"]
]

matriz[0] #[1, "a", 2]
matriz[0][0] # [1]
matriz[2][-1] # ["j"]

lista = ["p","y","t","h","o","n"]

lista  [2:] # ['y', 't', 'h', 'o', 'n']
lista [:2] # ['p', 'y',]
lista[1:3] # ['p', 't']
lista [0:3:2] # ['p', 't']
lista [::] # ['p','y', 't', 'h', 'o', 'n']
lista [::-1] # ['n', 'o', 'h', 't', 'y', 'p']

carros = ["gol", "celta", "palio"]

for indice, carro  in enumerate(carros):
    print(f"{indice}: {carro}")
    
numeros = [1,20,23,42,51,26,45]
pares = [ numero for numero in numeros if numero % 2 ==0]
print(pares)

numeros = [1,20,23,42,51,26,45]
quadrado = [ numero ** 2 for numero in numeros]
print (quadrado)

