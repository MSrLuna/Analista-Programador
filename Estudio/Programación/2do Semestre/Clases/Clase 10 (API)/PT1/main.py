import requests
#Necesitamos tener una URL que devuelva un JSON como información.
url = "https://jsonplaceholder.typicode.com/users"
#Ahora simplemente llamaremos al método get de objeto requests y le pasaremos por parámetro la url de arriba.
#como get() retorna información, puedes guardarla en una variable.
respuesta = requests.get(url)
#respuesta en este momento es un objeto que tiene más información dentro de sí
#print(respuesta)
#status_code es una propiedad que contiene un número, ese número indica si la solicitud fue exitosa o si hubo
#algún error.
# print(respuesta.status_code)
#Si tiene valor 200 significa que va todo bien, por lo tanto podemos validar con un if para que siga leyendo
#el código.
if respuesta.status_code == 200:
    #Lo que nos interesa es obtener cada valor que viene dentro del JSON de respuesta, para obtener esos
    #valores, llamaremos al método .json() de la respuesta.
    json = respuesta.json()
    #En este caso, estamos obteniendo una lista de diccionarios, por lo tanto, primero tenemos que obtener la
    #posición del diccionario que queremos, una vez apuntado a una posición de la lista, apuntaremos a una
    #clave del diccionario.
    #"lng" está dentro de "geo" el cual está dentro de "addres" que está dentro del diccionarios "posición 0".
    # print(json[0]["address"]["geo"]["lng"]
    for i in json:
        print(i["name"])

# lista = ["Benjamín", "Franco", "Rodrigo", "Daniel"]
# print(lista[1])
# tupla = ("Benjamín", "Franco", "Rodrigo", "Daniel")
# print(tupla[1])
# diccionario = {"Benjamín", "Franco", "Rodrigo", "Daniel"}
# print(diccionario[1])