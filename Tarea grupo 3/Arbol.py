# Python program to demonstrate searching operation
# in binary search tree without recursion
from typing import Dict # Typing porque me da un algo si no pongo tipos


class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to check the given
# key exist or not
def iterativeSearch(root:newNode, key:int) -> Dict:
	
    # Traverse until root reaches
    # to dead end
    visited_nodes = []	# Esta lista registra los nodos visitados para trazar el recorrido
    base=0		# Esto marca la posición más a la izquierda de los nodos visitados
    pos=0		# Esto marca la posición relativa del nodo visitado con respecto al nodo root
    visited_nodes.append({'root':True, 'data':root.data, 'pos':pos}) # añadir el nodo root a la lista de nodos visitados
    while root != None:
		
        # pass right subtree as new tree
        if key > root.data:
            root = root.right
            pos += 1			# Ajusta la posición
            visited_nodes.append({'root':False, 'dir':'right', 'data':root.data, 'pos':pos}) # Añade el nodo visitado a la lista
            base = min(pos, base)	# Ajusta base

        # pass left subtree as new tree
        elif key < root.data:
            root = root.left
            pos -= 1			# Ajusta la posición
            visited_nodes.append({'root':False, 'dir':'left', 'data':root.data, 'pos':pos}) # Añade el nodo visitado a la lista
            base = min(pos, base)	# Ajusta base
        else:
            return {'visited_nodes':visited_nodes, 'base':base} # if the key is found return 1
    return {}

# A utility function to insert a
# new Node with given key in BST
def insert(Node:newNode, data:int) -> newNode:
	
	# If the tree is empty, return
	# a new Node
	if Node == None:
		return newNode(data)

	# Otherwise, recur down the tree
	if data < Node.data:
		Node.left = insert(Node.left, data)
	elif data > Node.data:
		Node.right = insert(Node.right, data)

	# return the (unchanged) Node pointer
	return Node

# Esta funcion imprime la información en stdout
def show_data(data:Dict)->None:
    # Estos son graficos
    node_line=" {data} "
    node_left="  /"
    node_right="\\  "
    if len(data): # Chequea si se encontro el nodo especificado
        print('Encontrado en:')
        for line in data['visited_nodes']: # imprime en cada linea el nodo visitado
            output_tab="  "*(line['pos']-data['base']) # calcula la tabulacion requerida usando base y pos
            if not line['root']: # Chequea si el nodo visitado es el nodo root para no escribir '/' o '\' encima de este
                if line['dir'] == 'left':
                    print(output_tab+node_left) # Imprime la coneccion entre nodos
                else:
                    print(output_tab+node_right) # Imprime la coneccion entre nodos
            print(output_tab+node_line.format(data=line['data'])) # Imprime la informacion del nodo
    else:
        print('No Encontrado')

# Driver Code
if __name__ == '__main__':
    root = newNode(int(input("Ingrese el valor raiz del arbol: ")))
    nodes = int(input("Cantidad de nodos: "))
    for i in range(nodes):
        insert(root, int(input("ingrese el valor ({numero}): ".format(numero = i+1))))
    search = int(input("Nodo para buscar: "))
    show_data(iterativeSearch(root, search))

# This code is contributed by PranchalK

