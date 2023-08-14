# %s       strings
# %d       int
# %f        float

nome = "jonnas"
idade = 18
profissao = "Programador"
linguagem = "Python"


print("ola, me chamo {0}, tenho {1} anos de idade e sou {2}. No momento estou me dedicando em estudar {3}".format(nome,idade,profissao,linguagem)) 

print("ola, me chamo {nome}, tenho {idade} anos de idade e sou {profissao}. No momento estou me dedicando em estudar {linguagem}".format(nome=nome,idade=idade,profissao=profissao,linguagem=linguagem)) 

print(f"ola, me chamo {nome}, tenho {idade} anos de idade e sou {profissao}. No momento estou me dedicando em estudar {linguagem}") 