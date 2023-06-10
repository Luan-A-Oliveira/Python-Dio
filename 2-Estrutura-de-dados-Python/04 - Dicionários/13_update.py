contatos = {"luan@gmail.com": {"nome": "Luan", "telefone": "3333-2221"}}

contatos.update({"luan@gmail.com": {"nome": "Luanzitow"}})
print(contatos)  # {'uan@gmail.com': {'nome': 'Luanzitow'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'luan@gmail.com': {'nome': 'Luanzitow'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
