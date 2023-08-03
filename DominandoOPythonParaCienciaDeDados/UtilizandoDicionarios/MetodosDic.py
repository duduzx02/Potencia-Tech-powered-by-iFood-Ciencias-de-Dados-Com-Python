contatos = {
    "zaza@gmail.com": {"nome": "Zaza", "idade": 22},
    "zuzu@gmail.com": {"nome": "Zuzu", "idade": 11},
    "zizi@gmail.com": {"nome": "Zizi", "idade": 33},
    "zozo@gmail.com": {"nome": "Zozo", "idade": 44, "extra": {"a": 1}}, 
}
copy = contatos.copy()
contatos.clear()
print(contatos)
print(copy)

dici = dict.fromkeys(["nome", "telefone"], "vazio")
print(dici)

print()
print(copy.get("chave"))
print(copy.get("chave", {}))
print(copy.get("zozo@gmail.com", {})) # o {} só retorna se a chave estiver vazia
print(copy.get("zozo@gmail.com"))
print()
print(copy.items())
print()
print(copy.keys())
print()
print(copy.pop("zozo@gmail.com", "não encontrado"))  # o {} só retorna se a chave estiver vazia
print(copy)
print()
print(copy.popitem())
print(copy)

copy.setdefault("nome", "dudu")
print(copy)

print()
copy.update({"zaza@gmail.com": {"nome": "Zaza", "idade": 25}})
print(copy)
print()
print(copy.values())

print("zaza@gmail.com" in copy)

del copy["zaza@gmail.com"]
print(copy)
del copy["zuzu@gmail.com"]["nome"]
print(copy)