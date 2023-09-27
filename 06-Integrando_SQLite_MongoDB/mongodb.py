import pymongo
import pprint

print("Iniciando a conexão com o MongoDB")


client = pymongo.MongoClient("link mongodb")


db = client.banco
collection = db.clients


new_clients = [{
    "agency": 1,
    "name": "Luan Aquino",
            "cpf": "234.434.456-50",
            "address": "Rua 1, número 1",
            "account": ["cc", "23000"],
            "balance": 1500
},
    {
    "agency": 1,
    "name": "Regina Garcia",
            "cpf": "125.652.970-80",
            "address": "Rua 2, número 2",
            "account": ["cp", "33000"],
            "balance": 3000
},
    {
    "agency": 1,
    "name": "Marcio Melo",
            "cpf": "348.610.999-20",
            "address": "Rua 3, número 3",
            "account": ["cc", "43000"],
            "balance": 4500
}]


print("Salvando as informações no MongoDB")
clients = db.clients
result = clients.insert_many(new_clients)
print(result.inserted_ids)


print("\n Recuperando as informações da cliente Sandy:")
pprint.pprint(db.clients.find_one({"name": "Sandy Júnior"}))


print("\n Listagem dos clientes presentes na coleção clients:")
for client in clients.find():
    pprint.pprint(client)


print("\n Recuperando informação dos clientes de maneira ordenada pelo nome:")
for client in clients.find({}).sort("name"):
    pprint.pprint(client)


print("\n Clientes da agência 2000:")
for client in clients.find({"agency": 2000}):
    pprint.pprint(client)


print("\n Clientes com conta poupança:")
for client in clients.find({"account": "cp"}):
    pprint.pprint(client)


print("\n Clientes com conta corrente:")
for client in clients.find({"account": "cc"}):
    pprint.pprint(client)
