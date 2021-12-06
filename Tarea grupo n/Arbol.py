# Python program to demonstrate searching operation
# in binary search tree without recursion
from typing import Dict


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
    visited_nodes = []
    base=0
    pos=0
    visited_nodes.append({'root':True, 'data':root.data, 'pos':pos})
    while root != None:
		
		# pass right subtree as new tree
        if key > root.data:
            root = root.right
            pos += 1
            visited_nodes.append({'root':False, 'dir':'right', 'data':root.data, 'pos':pos})
            base = min(pos, base)

		# pass left subtree as new tree
        elif key < root.data:
            root = root.left
            pos -= 1
            visited_nodes.append({'root':False, 'dir':'left', 'data':root.data, 'pos':pos})
            base = min(pos, base)
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

def show_data(data:dict)->None:
    node_line=" {data} "
    node_left="  /"
    node_right="\\  "
    if len(data):
        print('Encontrado en:')
        for line in data['visited_nodes']:
            output_tab="  "*(line['pos']-data['base'])
            if not line['root']:
                if line['dir'] == 'left':
                    print(output_tab+node_left)
                else:
                    print(output_tab+node_right)
            print(output_tab+node_line.format(data=line['data']))
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

