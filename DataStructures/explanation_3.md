Explanation:

1. Binary Tree:
  - The binary tree data structure is used to build the Huffman tree, which is the core of Huffman encoding and decoding. Each node in the binary tree represents a character along with its frequency. 
  - The binary tree is constructed in a bottom-up manner by combining nodes with the lowest frequencies until a single root node is formed. In the Huffman tree, each node has either 0 or 2 children, representing the binary encoding scheme of characters. 
  - The binary tree data structure allows for efficient traversal from the root to leaf nodes during encoding and decoding.

2.  List of Nodes:
  - The list of nodes is used to mimic a priority queue (or min heap) during the construction of the Huffman tree. 
  - Initially, each character and its frequency are represented as individual nodes in the list. 
  - The list is sorted based on the frequencies of the nodes, with the node having the lowest frequency being at the front. 
  - Nodes are repeatedly popped out from the list based on their frequencies, combined to form a new internal node, and then reinserted back into the list. 
  - Using a list as a priority queue simplifies the implementation and understanding of the Huffman tree construction process, at the expense of time complexity. 

Time Complexity:

The time complexity of the Huffman encoding algorithm depends on two main aspects: building the Huffman tree and generating the encoded data. 
 - Building the Huffman Tree: The construction of the Huffman tree involves iterating over the list of nodes and repeatedly popping out nodes with the minimum frequency until only the root node remains. This process has a time complexity of O(n^2), where n is the number of unique characters in the input message. This worst-case scenario occurs when the characters are sorted in order of decreasing frequency.
 - Generating the Encoded Data: Generating the encoded data involves traversing the Huffman tree for each character in the input message to find its corresponding binary code. This process has a time complexity of O(m), where m is the length of the input message. 
Overall, the time complexity of the Huffman encoding algorithm is O(n^2 + m), with n being the number of unique characters and m being the length of the input message.
 
Space Complexity:

The space complexity of the Huffman encoding algorithm depends on the data structures used and the size of the input message.
 - Binary Tree: The space required for the binary tree is proportional to the number of nodes in the tree, which is equal to the number of unique characters in the input message. Therefore, the space complexity for the binary tree is O(n), where n is the number of unique characters.
 - List of Nodes: The space required for the list of nodes is also proportional to the number of unique characters in the input message. Hence, the space complexity for the list of nodes is also O(n).
 - Encoded Data: The space required for the encoded data depends on the size of the input message and the compression achieved by the Huffman encoding algorithm. In the worst-case scenario, where the encoding does not result in any compression, the space complexity for the encoded data is O(m), where m is the length of the input message. 

Overall, the space complexity of the Huffman encoding algorithm is O(n + m), with n being the number of unique characters and m being the length of the input message.