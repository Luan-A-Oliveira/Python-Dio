import pprint
import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:qms8vg74@cluster0.alfwqtm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"autor":"Luan"}))
print(posts.count_documents({"tags":"pymongo"}))

pprint.pprint(posts.find_one({"tags":"insert"}))

print("\nrecuperando info da colecao post de maneira ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('autor', pymongo.ASCENDING)],
                                  unique=True)

print(sorted(list(db.profiles.index_information())))

user_profile = [
    {'user_id': 211, 'name':'Jorge'},
    {'user_id': 212, 'name':'Cleber'}]

result = db.profile_user.insert_many(user_profile)

print("\ncolecoes armazenadas no mongodb")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

#deleta tudo os dados do db
#db['posts'].drop()

for post in posts.find():
    pprint.pprint(post)

#deleta 1 intem de cada vez de acordo com autor
#print(posts.delete_one({"autor":"Luan"}))

#deletar DB
client.drop_database('test')

#print(db.list_collection_names())