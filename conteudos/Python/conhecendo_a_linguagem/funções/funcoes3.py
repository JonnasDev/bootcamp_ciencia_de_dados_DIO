def somar (a, b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a,b):
    return a / b



def exibir_resultado(a, b, funcao):
    
    resultado = funcao(a,b)
    print(f"o resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)    

sub = subtrair
print("o resultado é: ", sub(10,10))