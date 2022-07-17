import pymongo

#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://gopalip:mongo1996@cluster0.urrq1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Praveen",
    "email" : "Praveen.g@gmail",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )