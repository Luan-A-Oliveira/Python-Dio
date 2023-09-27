contatos = {"luan@gmail.com": {"nome": "Luan", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "luan@gmail.com", {}
)  # {"luan@gmail.com": {"nome": "Luan", "telefone": "3333-2221"}
print(resultado)
