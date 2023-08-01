pessoa = {"nome": "Eduardo", "idade": 27}

pessoa2 = dict(nome="Lívia", idade=38)

pessoa["telefone"] = "3333-3333"
pessoa2["telefone"] = "2222-2222"

print(pessoa)
print(pessoa2)

dados = {"nome": "Eduardo", "idade": 28, "telefone": "3333-3333"}
print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Maaria"
dados["idade"] = 55
dados["telefone"] = "8888-8888"
print(dados)

contatos = {
    "zaza@gmail.com": {"nome": "Zaza", "idade": 22},
    "zuzu@gmail.com": {"nome": "Zuzu", "idade": 11},
    "zizi@gmail.com": {"nome": "Zizi", "idade": 33},
    "zozo@gmail.com": {"nome": "Zozo", "idade": 44, "extra": {"a": 1}}, 
}

print(contatos["zaza@gmail.com"])
print(contatos["zizi@gmail.com"]["nome"])
print(contatos["zozo@gmail.com"]["extra"]["a"])

for contato in contatos:
    print(contato, contatos[contato])

for chave, valor in contatos.items():
    print(chave, valor)