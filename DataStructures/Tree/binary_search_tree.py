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

def is_empty(my_bst):
    """ 
    Informa si el mapa esta vacio

    Args:
        my_bst (BST): El mapa bst
    Returns:
        True si la tabla es vacía, False en caso contrario
    """
    contador = size(my_bst)
    if contador != 0:
        return False
    else:
        return True

def min_key(my_bst):
    """ 
    Retorna la menor llave de la tabla de simbolos

    Args:
        my_bst (BST): arbol de busqueda binaria
    Returns:
        Valor de la menor llave
    """
    if my_bst['root'] is None:
        return None
    else: 
        return min_key_nodo(my_bst['root'])
    
def min_key_nodo(root):
    if root['left'] is not None:
        return min_key_nodo(root['left'])
    else:
        return root['key']

def max_key(my_bst):
    """ 
    Retorna la menor llave de la tabla de simbolos

    Args:
        my_bst (BST): arbol de busqueda binaria
    Returns:
        Valor de la menor llave
    """
    if my_bst['root'] is None:
        return None
    else: 
        return max_key_nodo(my_bst['root'])
    
def max_key_nodo(root):
    if root['right'] is not None:
        return max_key_nodo(root['right'])
    else:
        return root['key']

def delete_min(my_bst):
    """ 
    Elimina el menor elemento del árbol de búsqueda binaria.

    Args:
        my_bst (BST): Árbol de búsqueda binaria.
        
    Returns:
        El árbol sin la llave más pequeña.
    """
    if my_bst['root'] is None:
        return my_bst  
    
    my_bst['root'] = delete_min_nodo(my_bst['root'])
    
    return my_bst

def delete_min_nodo(root):
    """
    Función recursiva que elimina el nodo con la menor clave en el subárbol.

    Args:
        root: Nodo raíz del subárbol.

    Returns:
        La nueva raíz del subárbol después de eliminar el nodo mínimo.
    """
    # Caso base: Si no hay un hijo izquierdo, este es el nodo mínimo
    if root['left'] is None:
        return root['right']  # Reemplaza el nodo actual con su hijo derecho (si lo tiene)
    
    root['left'] = delete_min_nodo(root['left'])

    root['size'] = 1 + node_size(root['left']) + node_size(root['right'])
    return root

def delete_max(my_bst):
    """ 
    Elimina el menor elemento del árbol de búsqueda binaria.

    Args:
        my_bst (BST): Árbol de búsqueda binaria.
        
    Returns:
        El árbol sin la llave más pequeña.
    """
    if my_bst['root'] is None:
        return my_bst  
    
    my_bst['root'] = delete_max_nodo(my_bst['root'])
    
    return my_bst

def delete_max_nodo(root):
    """
    Función recursiva que elimina el nodo con la menor clave en el subárbol.

    Args:
        root: Nodo raíz del subárbol.

    Returns:
        La nueva raíz del subárbol después de eliminar el nodo mínimo.
    """
    # Caso base: Si no hay un hijo derecho, este es el nodo mínimo
    if root['right'] is None:
        return root['left']  # Reemplaza el nodo actual con su hijo izquierdo (si lo tiene)
    
    root['right'] = delete_max_nodo(root['right'])

    root['size'] = 1 + node_size(root['left']) + node_size(root['right'])
    return root

def height(my_bst):
    """
    Retorna la altura del árbol de búsqueda binaria (BST).

    Args:
        my_bst: El árbol de búsqueda binaria (BST).

    Returns:
        int: La altura del árbol. Si el árbol está vacío, retorna -1.
    """
    if my_bst['root'] is None:
        return -1  # Si el árbol está vacío, la altura es -1
    
    return height_nodo(my_bst['root'])

def height_nodo(root):
    """
    Función auxiliar recursiva que calcula la altura de un subárbol.

    Args:
        root: Nodo raíz del subárbol.

    Returns:
        int: La altura del subárbol.
    """
    if root is None:
        return -1  # Caso base: Si el nodo es None, la altura es -1
    
    # Calculamos la altura de los subárboles izquierdo y derecho
    altura_izq = height_nodo(root['left'])
    altura_der = height_nodo(root['right'])
    
    # La altura del nodo actual es 1 más la altura máxima de sus hijos
    return 1 + max(altura_izq, altura_der)

