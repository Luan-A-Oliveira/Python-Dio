contatos = {"luan@gmail.com": {"nome": "Luan", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('luan@gmail.com', {'nome': 'Luan', 'telefone': '3333-2221'})
print(resultado)

contatos.popitem()  # KeyError
