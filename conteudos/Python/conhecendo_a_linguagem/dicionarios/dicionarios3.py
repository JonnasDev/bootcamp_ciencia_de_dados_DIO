contatos = {
    "Jonnas@gmail.com": {"nome":"Jonnas", "idade": 18, "telefone":"11-22"},
    "Raiza@gmail.com": {"nome":"Raiza", "idade": 17, "telefone": "22-33"},
    "Cris@gmail.com": {"nome": "Cris", "idade": 23, "telefone": "33-44"}
        
}

del contatos["Cris@gmail.com"]

for chaves in contatos:
 print(chaves, contatos[chaves])

resultado = "Jonnas@gmail.com" in contatos
print(resultado)#verifica se existe esta chave