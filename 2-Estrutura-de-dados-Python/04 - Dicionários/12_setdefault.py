contato = {"nome": "Luan", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Luan"
print(contato)  # {'nome': 'Luan', 'telefone': '3333-2221'}

contato.setdefault("idade", 35)  # 35
print(contato)  # {'nome': 'Luan', 'telefone': '3333-2221', 'idade': 35}
