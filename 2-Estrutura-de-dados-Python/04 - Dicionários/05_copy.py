contatos = {"luan@gmail.com": {"nome": "Luan", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["luan@gmail.com"] = {"nome": "Luanzitow"}

print(contatos["luan@gmail.com"])  # {"nome": "Luan", "telefone": "3333-2221"}

print(copia["luan@gmail.com"])  # {"nome": "Luanzitow"}
