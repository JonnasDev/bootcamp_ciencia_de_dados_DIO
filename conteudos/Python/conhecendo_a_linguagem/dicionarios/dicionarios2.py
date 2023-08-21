contatos = {
    "Jonnas@gmail.com": {"nome":"Jonnas", "idade": 18, "telefone":"11-22"},
    "Raiza@gmail.com": {"nome":"Raiza", "idade": 17, "telefone": "22-33"},
    "Cris@gmail.com": {"nome": "Cris", "idade": 23, "telefone": "33-44"}
        
}
# cria um dicionario que recebe uma chave, essa chave recebe uma cadeia de valores

print(contatos["Jonnas@gmail.com"])
# printa a cadeia de valores da chave EMAIL, que esta no dicionario

for chave in contatos:
    print(chave, contatos[chave])
    
for chaves, valor in contatos.items():
    print(chaves,valor)

    
    
    