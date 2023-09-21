import datetime
import pprint
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:qms8vg74@cluster0.alfwqtm.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
#print(db.test_collection)
#print(db.list_collection_names())

#definicao de infor para compor o doc
post = {
    "autor":"Luan",
    "text":"My first mongodb aplication on python",
    "tags":["mongodb", "pymongo", "python3"],
    "date": datetime.datetime.utcnow()
}

#preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
#print(post_id)
#print(db.posts.find_one())

#pprint.pprint(db.posts.find_one())

#bulk inserts


new_posts = [{
        "autor": "Luan",
        "text": "another text",
        "tags": ["bolk", "post", "insert"],
        "date": datetime.datetime.utcnow()
    },
    {
        "autor": "Regina",
        "text": "regina text",
        "title": "mongo is fun",        
        "date": datetime.datetime(2022, 11, 10, 10, 45)
    }]

result = posts.insert_many(new_posts)
#print(result.inserted_ids)

#pprint.pprint(db.posts.find_one({"autor":"Regina"}))

print("\nDocumentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)
