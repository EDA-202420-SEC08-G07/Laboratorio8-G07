
def new_list():
    """Crea una lista implementada con un Array List vacío.
        Define una lista vacía y con un tamaño de cero
    Returns:
        array_list: Lista creada
    """
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist


def add_first(lista, elemento):
    """Añade un elemento en la primera posicion de la lista

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño
        elemento : Elemento a añadir en la primera posicion

    Returns:
        array_list modificada con el elemento puesto en la primera posicion
    """
    lista["elements"].insert(0, elemento)
    lista["size"]+=1
    return lista


def add_last(lista, elemento):
    """Añade un elemento en la ultima posicion de la lista

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño
        elemento : Elemento a añadir en la ultima posicion

    Returns:
        array_list modificada con el elemento puesto en la ultima posicion
    """
    lista["elements"].append(elemento)
    lista["size"]+=1
    return lista


def is_empty(lista):
    """Verifica si la lista contiene algun elemento o esta vacia

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño

    Returns:
        bool: Verdadero si la lista esta vacia, falso de lo contrario
    """
    return lista["size"] == 0


def size(lista):
    """Retorna cuantos elementos contiene el array_list

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño

    Returns:
        int: valor de cuantos elementos contiene la lista
    """
    
    return lista['size']


def first_element(lista):
    """Busca el primer elemento de la lista
    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño

    Returns:
        Retorna el primer elemento de la lista
    """
    return lista["elements"][0]


def last_element(lista):
    """Busca el ultimo elemento de la lista

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño

    Returns:
        Retorna el ultimo elemento de la lista
    """
    return lista["elements"][-1]


def remove_first(lista):
    """Remueve el primer elemento de la lista

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño

    Returns:
        array_list: Lista de elementos con el primer elemento eliminado
    """
    del lista["elements"][0]
    lista["size"]-=1
    return lista


def remove_last(lista):
    """Remueve el ultimo elemento de la lista

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño

    Returns:
        array_list: Lista de elementos con el ultimo elemento eliminado
    """
    del lista["elements"][-1]
    lista["size"]-=1
    return lista


def insert_element(lista, elemento, posicion):
    """Inserta en la lista un elemento dado en una posicion especificada
    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño
        elemento : elemento que se quiere insertar en la lista
        posicion (int): Posicion en la cual se quiere insertar el elemento dado

    Returns:
        array_list: Lista modificada con el elemento añadido en la posicion especificada
    """
    lista["elements"].insert(posicion, elemento) 
    lista["size"]+=1
    return lista


def delete_element(lista, elemento):
    """Elimina un elemento dado en la lista

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño
        elemento: elemento que se desea eliminar de la lista

    Returns:
        array_list: Lista modoficada con el elemento especificado eliminado
    """
    lista['elements'].pop(elemento)
    lista["size"] -= 1
    return lista


def change_info(lista, pos, elemento_final):
    """Cambia un elemento dado por el usuario con la posicion por otro elemento final dado por el usuario

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño
        pos: Posicion del elemento a sustituir 
        elemento_final: Elemento que va a sostituir al inicial

    Returns:
        array_list: Lista modoficada con el cambio de elementos
    """
    # Encontramos el indice del elemento
    lista['elements'][pos] = elemento_final
    return lista


def exchange(lista, pos1, pos2):
    """Intercambia la info en las posiciones pos1 y pos2 de la lista

    Args:
        lista (array_list): array_list que contiene los datos y una variable de tamaño
        pos1 (int): posicion del primer elemento que se requiere cambiar
        pos2 (int) : posicion del segundo elemento que se requiere cambiar

    Returns:
        array_list: Lista modoficada con el cambio de elementos
    """
    elemento_1 = lista['elements'][pos1]
    elemento_2 = lista['elements'][pos2]
    lista['elements'][pos1] = elemento_2
    lista['elements'][pos2] = elemento_1
    
    return lista


def sub_list(lista, inicio, final):
    """Crea una sublista iniciando por una posicion dada por el usuario y terminada en otra posicion dada por el usuario

    Args:
        lista (array_lista): array_list que contiene los datos y una variable de tamaño
        inicio (int): posicion en la cual se quiere iniciar la nueva lista
        final (int): posicion en la cual se quiera finalizar la nueva lista

    Returns:
        array_list: Nueva sublista proveniente de la lista original
    """
    sub_lista = new_list()
    sub_lista['type'] = 'ARRAY_LIST' 
    sub_lista['elements'] = lista["elements"][inicio:final]
    sub_lista["size"]=len(sub_lista["elements"])
    return sub_lista


def get_element(my_list, pos):
    """Retorna el elemento que se ubica en la posicion dada por el usuario

    Args:
        my_list (array_list): array_list que contiene los datos y una variable de tamaño
        pos (_type_): posicion en la cual se desea buscar el elemento

    Returns:
        Elemento que se encontro en la posicion dada por el usuario 
    """
    return my_list['elements'][pos]

def is_present(my_list, element, cmp_function):
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if (cmp_function(element, info) == 0):
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def selection_sort(my_list, sort_crit):
    """
    Función de ordenamiento que implementa el algoritmo de Selection Sort

    Se recorre la lista y se selecciona el elemento más pequeño y se intercambia con el primer elemento 
    de la lista. Se repite el proceso con el segundo elemento más pequeño y así sucesivamente.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

    Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

    Args:
        my_list (list):  Lista a ordenar
        sort_crit (function):  Función de comparación de elementos para ordenar
    Returns:
        Lista ordenada (array_list)
    """
    tamanio = size(my_list)
    list_ordenada = my_list['elements']
    if tamanio <= 1:
        return my_list
    
    for i in range (tamanio - 1):
        minimo = i
        
        for j in range(i + 1, tamanio):
            if sort_crit(list_ordenada[j], list_ordenada[minimo]):
                minimo = j
        if minimo != i:
            temp = list_ordenada[i]
            list_ordenada[i] = list_ordenada[minimo]
            list_ordenada[minimo] = temp
            
    return {'elements': list_ordenada, 'size': tamanio}

def insertion_sort(my_list, sort_crit):
    """
    Función de ordenamiento que implementa el algoritmo de Insertion Sort

    Se recorre la lista y se inserta el elemento en la posición correcta en la lista ordenada. Se repite el proceso hasta que la lista esté ordenada.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

    Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

    Args:
        my_list (list):  Lista a ordenar
        sort_crit (function):  Función de comparación de elementos para ordenar
    Returns:
        Lista ordenada (array_list)
    """
    tamanio = my_list['size']
    list_ordenada = my_list['elements']
    if tamanio <= 1:
        return my_list['elements']
    
    for i in range (1, tamanio):
        actual = list_ordenada[i]
        j = i - 1
        while j >= 0 and sort_crit(actual, list_ordenada[j]):
            list_ordenada[j + 1] = list_ordenada[j]
            j -= 1
        list_ordenada[j + 1] = actual
            
    return {'elements': list_ordenada, 'size': tamanio}

def shell_sort(my_list, sort_crit):
    """
    Función de ordenamiento que implementa el algoritmo de Shell Sort.

    El algoritmo de Shell Sort es una versión optimizada de Insertion Sort. Se basa en comparar elementos
    que están separados por un espacio (gap) y reducir progresivamente el gap hasta llegar a un espacio de 1,
    en cuyo punto se comporta como Insertion Sort.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

    Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

    Args:
        my_list (dict): Diccionario que contiene la lista a ordenar en la clave 'elements'.
        sort_crit (function): Función de comparación de elementos para ordenar.
    Returns:
        dict: Diccionario con la lista ordenada en la clave 'elements'.
    """
    tamanio = my_list['size']
    list_ordenada = my_list['elements']
    if tamanio <= 1:
        return my_list

    s = tamanio // 2  
    while s > 0:
        for i in range(s, tamanio):
            temp = list_ordenada[i]
            j = i

            while j >= s and sort_crit(temp, list_ordenada[j - s]):
                list_ordenada[j] = list_ordenada[j - s]
                j -= s

            list_ordenada[j] = temp

        s = s // 2

    return {'elements': list_ordenada, 'size': tamanio}


def merge_sort(my_list, sort_crit):
    """
    Función de ordenamiento que implementa el algoritmo de Merge Sort

    Se divide la lista en dos partes, se ordenan las partes y se combinan las partes ordenadas.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

    Dependiendo de la función de comparación, se ordena la lista de manera ascendente o descendente.

    Args:
        my_list (dict): Estructura de la lista a ordenar, que contiene 'elements' y 'size'.
        sort_crit (function): Función de comparación de elementos para ordenar.
    Returns:
        my_list: La lista ordenada en la estructura original.
    """
    lista_ordenada = my_list['elements']
    tamanio = len(lista_ordenada)
    
    if tamanio <= 1:
        return my_list
    mitad = tamanio // 2
    mitad_izq = {'elements': lista_ordenada[:mitad], 'size': mitad}
    mitad_der = {'elements': lista_ordenada[mitad:], 'size': tamanio - mitad}
    
    izquierda_ordenada = merge_sort(mitad_izq, sort_crit)['elements']
    derecha_ordenada = merge_sort(mitad_der, sort_crit)['elements']
    lista_final = organizacion(izquierda_ordenada, derecha_ordenada, sort_crit)
    
    my_list['elements'] = lista_final
    my_list['size'] = len(lista_final)
    
    return my_list

def organizacion(izquierda, derecha, sort_crit):
    """
    Función auxiliar para fusionar dos listas ordenadas.
    
    Args:
        izquierda (list): Lista ordenada izquierda.
        derecha (list): Lista ordenada derecha.
        sort_crit (function): Función de comparación para definir el orden.
    Returns:
        list: Lista fusionada y ordenada.
    """
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if sort_crit(izquierda[i], derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

        