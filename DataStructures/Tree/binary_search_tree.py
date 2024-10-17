from DataStructures.Tree import bst_node as bst_nd
def new_map():
    """Crea una tabla de símbolos ordenada basada en un árbol binario de búsqueda (BST) vacía."""
    return {
        "root": None,
        "type": "BST"
    }   

def put(my_bst, key, value):
    """Inserta una pareja llave-valor en el BST. Si la llave ya existe, reemplaza el valor."""
    # Caso base -> Raiz = None
    if my_bst['root'] is None:
        my_bst['root'] = bst_nd.new_node(key, value)
    
    # Caso recursivo -> Insertar en el arbol
    else:
        # Menor para la izquierda
        if key < my_bst['root']['key']:
            if my_bst['root']['left'] is None:
                my_bst['root']['left'] = bst_nd.new_node(key, value)
            else:
                put(my_bst['root']['left'], key, value)
                
        # Mayor para la derecha
        elif key > my_bst['root']['key']:
            if my_bst['root']['right'] is None:
                my_bst['root']['right'] = bst_nd.new_node(key, value)
            else:
                put(my_bst['root']['right'], key, value)
        
        # Iguales, actualizamos valor
        elif key == my_bst['root']['key']:
            pass
            
    return my_bst
           
        
    
    
        
