def exibir_mensagem():
    print("ola mundo")
    
exibir_mensagem() # para chamar a função nao precisa usar o return
    
def exibir_mensagem_2(nome, idade):
    print(f"seja bem vindo {nome} e você tem {idade}")
    
exibir_mensagem_2(nome="Jonnas", idade= 18) 
# como eu nn passei o valor para nome na função, eu tenho que passar ele no return
 