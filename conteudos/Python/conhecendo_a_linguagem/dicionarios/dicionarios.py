dados = {"nome":"Jonnas", "idade": 18, "telefone": "3333-4444"}
print(f"print 1{dados}")

print("print 2", dados["nome"], dados["idade"], dados["telefone"])


dados["nome"] = "João"
dados["idade"] = 39

print("print 3",dados["nome"], dados["idade"])
# ele pega o valor do objeto X dentro da variavel


