contatos = {"luan@gmail.com": {"nome": "Luan", "telefone": "3333-2221"}}

resultado = contatos.pop("luan@gmail.com")  # {'nome': 'Luan', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("luan@gmail.com", {})  # {}
print(resultado)
