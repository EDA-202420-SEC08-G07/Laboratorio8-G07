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
    # Caso base -> Raiz = None
    if root is None:
        root = bst_nd.new_node(key, value)
        
    # Caso recursivo -> Insertar en el arbol
    else:
        # Llave menor al nodo, para la izquierda
        if key < root['key']:
            if root['left'] is None:
                root['left'] = bst_nd.new_node(key, value)
            else:
                insert_node(root["left"], key, value)
                
        # Llave mayor al nodo, para la derecha
        elif key > root['key']:
            if root['right'] is None:
                root['right'] = bst_nd.new_node(key, value)
            else:
                insert_node(root['right'], key, value)
        
        # Iguales, actualizamos valor
        elif key == root['key']:
            root["value"]=value
 
 # TODO poner size
    return root
    
        
