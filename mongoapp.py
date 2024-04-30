from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
client = MongoClient('localhost')

# CREACION DE NUEVO BASE DE DATOS
# SI EL NOMBRE DE BBDD TIENE UN VALOR VACIO, NO APARECIERA SI EJECUTAMOS EL PRINT

db = client['prueba']

col = db['personas']

# VAMOS A AGREGAR DOCUMENTOS

#col.insert_one({
#    'edad':20,
#    'nombre': 'user',
#    'intereses': ['Musica', 'Tiktok']
#})

# CONTAR LOS VALORES DENTRO DEL DOCUMENTO QUE ANTERIORMENTE HEMOS CREADO


# PODEMOS USAR INSERT_MANY() PARA INSERTAR VARIOS DOCUMENTOS

col.insert_many([
    {
        'edad':23,
        'nombre': 'user2',
        'intereses': ['algo1', 'algo2']
    },
    {
        'edad':53,
        'nombre': 'user3',
        'intereses': ['algo3', 'algo4']
    },
    {
        'edad':12,
        'nombre': 'user2',
        'intereses': ['algo1', 'algo2']
    },
    {
        'edad':13,
        'nombre': 'user3',
        'intereses': ['algo3', 'algo4']
    }
])

print(col.count_documents({}))

print(client.list_database_names())
print(db.list_collection_names())

# PARA PODER HACER QUERIES USAMOS FIND()

print(col.find({})) # NOS DEVUELVE UN OBJETO

#for items in col.find({}):
#    print(items)

# HACER UN QUERY DE MUCHOS DOCUMENTOS
for items in col.find({
    "edad": {
        # $gt is greater than, $lt is less than
        "$lt": 20
    }
}):
    print(items)

# HACER UN QUERY DE UN SOLO QUERY UTILIZANDO FIND_ONE()

one_query = col.find_one({
    'edad': {
        '$gt': 55
    }
})

print(f"This is the information of age greater than 55: {one_query}")

# HACER UNA ELIMINACION: DELETE_ONE() Y DELETE_MANY()

delete_many_query = col.delete_many({
    'edad': 63
})

edad_63 = col.find_one({
    'edad': 63
})

print(edad_63)

# HACER UNA MODIFICACION: UPDATE_ONE() Y UPDATE_MANY()

update_one_query = col.update_one({
    "edad": 13
}, {
    "$set": {
        "nombre": "Juan"
    }
})

find_Juan = col.find_one({"nombre":"Juan"})

print(find_Juan)

# HACER UN INDICE

# dentro de las claves

ascending_index = col.create_index([('edad', ASCENDING)])
descending_index = col.create_index([('edad', DESCENDING)])

print(ascending_index)
print(descending_index)
# ELIMINAR EL BASE DE DATOS

db.drop_collection('personas')

print(db.list_collection_names())

client.drop_database('prueba')

print(client.list_database_names())

client.close()