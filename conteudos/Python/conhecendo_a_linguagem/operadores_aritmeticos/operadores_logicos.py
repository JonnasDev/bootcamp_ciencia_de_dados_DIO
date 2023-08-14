print(" metodo E-----------------------------------------")

saldo = 1000 
saque = 200
limite_para_saque = 300 

print (saldo >= saque and saque <= limite_para_saque)
# operador E

print("metodo OR-----------------------------------------")

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque or saque <= limite)
# operador OU diz que para dar false, todos os passos tem que ser false


print("metodo parenteses---------------------------------")

print (True and True)
print (True and False)
print (True or True)
print (True or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite ) or  (conta_especial and saldo >= saque)
print(f"expressão 1: {exp}")

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(f"expressão 2: {exp2}")



conta_normal_com_saldo = saldo >= saque and saque <= limite
conta_especial_com_saldo = conta_especial and saldo >= saque

exp3 = conta_normal_com_saldo or conta_especial_com_saldo
print (f"expressão 3: {exp3}")