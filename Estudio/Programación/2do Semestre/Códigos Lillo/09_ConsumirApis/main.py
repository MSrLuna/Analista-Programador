import requests
# necesitamos tener una URL que devuelva un JSON como información
url = "https://jsonplaceholder.typicode.com/users"
# Ahora simplemente llamaremos al método get del objeto requests y le pasaremos
# por parámetro la URL que tenemos arriba.. como get() retorna información, puedes
# guardarla en una variable.
respuesta = requests.get(url)
# respuesta en este momento es un objeto que tiene más información dentro de sí
# status_code es una propiedad que contiene un número.. ese número indica si tu
# solicitud fue exitosa o si hubo algún error..
print(respuesta.status_code)
# Ahora que sabemos que si status_code tiene el valor 200 significa que está todo OK,
# podemos validar con un simple IF para saber si podemos seguir leyendo código
if respuesta.status_code == 200:
    # Lo que nos interesa es obtener cada valor que viene dentro del JSON de respuesta
    # Para obtener esos valores, llamaremos al método .json() de la respuesta
    json = respuesta.json()
    # En este caso, estamos obteniendo una LISTA de DICCIONARIOS..
    # Por lo tanto, primero tenemos que obtener la posición del diccionario que queremos
    # obtener.. una vez apuntando a una posición de la lista, apuntaremos a una
    # clave del diccionario
    # print(json[0]["name"])
    # Y cómo lo haríamos para obtener la Ciudad donde vive Leanne Graham??
    print(json[0]["address"]["geo"]["lng"])
    # Y cómo obtendríamos TODOS los nombres de los usuarios??
    # Tendríamos que recorrer la lista de diccionarios.. en la variable usuario
    # estaremos guardando temporalmente el diccionario del recorrido actual
    for usuario in json:
        # como usuario es el diccionario que extrajimos de la lista, para acceder
        # a sus propiedades lo haremos con corchetes clave.
        print(usuario["name"])