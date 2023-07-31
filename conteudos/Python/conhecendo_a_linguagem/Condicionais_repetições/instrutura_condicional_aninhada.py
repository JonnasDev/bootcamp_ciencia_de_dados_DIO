CONTA_NORMAL = False
CONTA_UNIVERSITARIA = True
CONTA_ESPECIAL = True

saldo= 2000
saque = 2300
CHEQUE_ESPECIAL =  450


if CONTA_NORMAL:
    if saldo >= saque:
        print("saque realizado com sucesso")      
    elif saque <= (saldo + CHEQUE_ESPECIAL):
          print("saque realizado com uso do cheque especial") 
    else:
        print("não foi possivel realizar o saque, saldo insuficiente")



elif CONTA_ESPECIAL:
    print("conta especial selecionada")



elif CONTA_UNIVERSITARIA:
    if saldo >= saque:
        print("saque realizado com sucesso")     
    else :
        print("saldo insuficiente")   
          
else:
     print("sistema não reconheceu esse tipo de conta")    