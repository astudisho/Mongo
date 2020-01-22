from pymongo import MongoClient

from pprint import pprint

#pass = 'Michi!123'
# chimi michi123


if __name__ == "__main__":
    
    connectionString = "mongodb://localhost:27017/test"
    # client = MongoClient("mongodb+srv://chimi:Michi%21123@mongo0-9gbwm.azure.mongodb.net/test?retryWrites=true&w=majority")
    client = MongoClient()
    db = client.test

    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    # pprint(serverStatusResult)

    cliente = { "id": 2, "nombre": "Michi", "subids": [1,3,4,6], "tipo": "fisico" }

    res = db.clientes.insert_one(cliente)

    clienteRead = db.clientes.find_one({"nombre": "Michi"})

    pprint(clienteRead)

    pass