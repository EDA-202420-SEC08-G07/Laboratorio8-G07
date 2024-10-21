from DataStructures.Tree import bst_node as bst_nd
def new_map():
    """Crea una tabla de símbolos ordenada basada en un árbol binario de búsqueda (BST) vacía."""
    return {
        "root": None,
        "type": "BST"
    }   

def put(my_bst, key, value):
    """Inserta una pareja llave-valor en el BST. Si la llave ya existe, reemplaza el valor."""
    my_bst["root"]=insert_node(my_bst["root"], key, value)
    return my_bst

def insert_node(root, key, value):
    # Caso base -> Raíz = None, crea un nuevo nodo
    if root is None:
        return bst_nd.new_node(key, value)

    # Llave menor, inserta a la izquierda
    if key < root['key']:
        root['left'] = insert_node(root['left'], key, value)
    
    # Llave mayor, inserta a la derecha
    elif key > root['key']:
        root['right'] = insert_node(root['right'], key, value)
    
    # Llave igual, actualiza el valor
    else:
        root['value'] = value
    
    #actualizacion del tamanio
    root['size'] = 1 + node_size(root['left']) + node_size(root['right'])

    return root

def node_size(node):
    """Devuelve el tamaño del subárbol enraizado en `node`. Si es `None`, devuelve 0."""
    if node is None:
        return 0
    return node['size']

def get(my_bst, key):
    """
    Retorna la pareja lleve-valor con llave igual a key 
    Args:
        my_bst: El arbol de búsqueda 
        key: La llave asociada a la pareja
    """
    return get_node(my_bst['root'], key)

def get_node(root, key):
    if root is None:
        return None
    elif root['key'] == key:
        return root['value']
    elif key < root['key']:
        return get_node(root['left'], key)
    else: 
        return get_node(root['right'], key)
    
def contains(my_bst, key):
    """
    Informa si la llave key se encuentra en la tabla de hash
    Args:
    my_bst: El arbol de búsqueda
    key: La llave a buscar
    Returns:
        True si la llave está presente False en caso contrario
    """
    return contains_nodo(my_bst['root'], key)

def contains_nodo(root, key):
    if root is None:
        return False
    if root['key'] == key:
        return True
    elif key < root['key']:
        return contains_nodo(root['left'], key)
    else: 
        return contains_nodo(root['right'], key)

def size(my_bst):
    """ 
    Retorna el número de entradas en la tabla de simbolos

    Args:
        my_bst (BST): El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    """
    if my_bst['root'] is None:
        return 0
    else:
        return my_bst['root']['size']