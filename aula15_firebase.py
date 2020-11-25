import pyrebase

config = {
    "apiKey": "AIzaSyBqLBA8kfIKCjcv-h6lRHIMylQxBsStNBE",
    "authDomain": "clientes-28e4a.firebaseapp.com",
    "databaseURL": "https://clientes-28e4a.firebaseio.com/",
    "storageBucket": "clientes-28e4a.appspot.com"
}

f = pyrebase.initialize_app(config)
c = f.database()

dados = {
    'nome': 'André Ricardo Prazeres',
    'idade': 46,
}
chave = '3918'
#c.child('t').child(chave).set(dados)
#c.child('t').push(dados)


c.child('t').child(chave).update(dados)
#c.child('t').child(chave).set(dados)

resultado = c.child('t').child(chave).get()

for i in resultado.each():
    print(i.key(), i.val())


c.child('t').child(chave).remove()