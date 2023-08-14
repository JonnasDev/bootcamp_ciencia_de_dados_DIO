curso = "PyTHon"

print(curso.upper()) #maiusculo
print(curso.lower()) #minusculo
print(curso.title()) #titulo

curso1 = "       python      "

print(curso1.strip()) #remove os espaços
print(curso1.lstrip()) #remove espaços da esquerda
print(curso1.rstrip()) #remove espaços da direita


curso2 = "python"

print(curso2.center(10, "#")) #centraliza a var curso e bota # ate preencher os 10 caracteres 
print(".".join(curso2)) #bota um . no entre cada letra