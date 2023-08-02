saldo = 2500
saque = 500

status_saque = "Sucesso" if saldo >= saque else "Falha"

print(f"{status_saque} ao realizar o saque")



if saldo >= saque:
    print("saque feito com sucesso")
else:
    print("erro ao realizar o saque")