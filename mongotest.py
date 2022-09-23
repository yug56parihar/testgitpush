import pymongo

client = pymongo.MongoClient("mongodb+srv://yug56parihar:Maahudi123@cluster0.istfxld.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

#Inserting data

d = {
    "name":"sudhanshu",
    "email": "sudh@ineuron.ai",
    "surname": "kumar"
}

dd = {
    "name":"sudhanshu",
    "email": "sudh@ineuron.ai",
    "surname": "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)