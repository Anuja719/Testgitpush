import pymongo
client = pymongo.MongoClient("mongodb+srv://Anuja:Welcome1@anuja.suldxsl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Anuja",
    "emailid" : "anuja@ineuron.ai",
    "surname" : "Chalisgaonkar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)