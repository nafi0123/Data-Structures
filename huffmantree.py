# first we consider a sting 
input_text = 'BCAADDDCCACACAC'  
#step 1: calculate the frequency 
freq = {}
for i in input_text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1 
#sort it in decending order
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#print(freq)  
#after sort
#[('C', 6), ('A', 5), ('D', 3), ('B', 1)]  
#step 2: Create Huffman Tress 
#Rules:we need to create node for all the unique character 
#first we create an empty node. set its key as None after that we assign minimum frequency to left node ('B', 1). 
#second minimum to right node ('D', 3)
#after add assign those minimum, we remove those. set the new nodes value = sum of two nodes and append the new node   
#sort the new nodes 
#create a Node class for storing user definded data. 
class Node: 
    def __init__(self, key, freq):
        self.key = key 
        self.freq = freq   
        self.left = None
        self.right = None
    def __str__(self):
        return self.freq

nodes = [Node(k, f) for k, f in freq]
while len(nodes)> 1: # here we check of the nodes is not empty 
    # Get the two zx with the lowest frequencies.
    left_node = nodes.pop()
    right_node = nodes.pop()
    # Step 2: Combine the frequencies under a new node.using "None" as the key for internal nodes.
    internal_node = Node(None, left_node.freq + right_node.freq) 
    internal_node.left = left_node
    internal_node.right = right_node
    # Step 3: Add the new node back to the nodes list.
    nodes.append(internal_node)
    # Sort the nodes again based on their frequency.
    nodes = sorted(nodes, key=lambda x: x.freq, reverse=True)
    #print([(n.key, n.freq) for n in nodes]) 
    #[('C', 6), ('A', 5), ('D', 3), ('B', 1)]
    #[('C', 6), ('A', 5), (None, 4)]
    #[(None, 9), ('C', 6)]
    #[(None, 15)] 

#step 3: decoding  
# load the tree, we load the root node and we will traverse recursively. 
huffman_tree = nodes[0]
# we create a recursive function  
def derive_huffman_codes(node,code, mapping):
    if node is None:
        return
    # If this node is a leaf node (it has a key), add the current code to the mapping.
    if node.key is not None:
        mapping[node.key] = code
        return
    # Traverse left (append '0' to code) and right (append '1' to code).
    derive_huffman_codes(node.left, code + '0', mapping)
    derive_huffman_codes(node.right, code + '1', mapping)
huffman_codes = {}  #store the result here 
derive_huffman_codes(huffman_tree,'', huffman_codes)
print(huffman_codes)
#{'C': '0', 'B': '100', 'D': '101', 'A': '11'}
