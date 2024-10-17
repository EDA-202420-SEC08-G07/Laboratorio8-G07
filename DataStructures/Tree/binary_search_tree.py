from DataStructures.Tree import bst_node as bst_nd
def new_map():
    """Crea una tabla de símbolos ordenada basada en un árbol binario de búsqueda (BST) vacía."""
    return {
        "root": None,
        "type": "BST"
    }   

def put(my_bst, key, value):
    """Inserta una pareja llave-valor en el BST. Si la llave ya existe, reemplaza el valor."""
    #menor
    if my_bst['root'] is None:
        my_bst['root'] = bst_nd.new_node(key, value)
    else:
        _put(my_bst["root"], key, value)
    return my_bst

def _put(node, key, value):
    if key < node['key']:
        if node['left'] is None:
            node['left'] = bst_nd.new_node(key, value)
        else:
            _put(node['left'], key, value)
    elif key > node['key']:
        if node['right'] is None:
            node['right'] = bst_nd.new_node(key, value)
        else:
            _put(node['right'], key, value)
    else:
        node['value'] = value
    node["size"] = 
    
    
        
