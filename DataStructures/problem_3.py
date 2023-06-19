from collections import defaultdict
import sys

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_frequency_table(data):
    frequency_table = defaultdict(int)
    for char in data:
        frequency_table[char] += 1
    return frequency_table

def find_min_freq_node(nodes):
    min_node = None
    for node in nodes:
        if min_node is None or node.freq < min_node.freq:
            min_node = node
    return min_node

def build_huffman_tree(frequency_table):
    nodes = [Node(char, freq) for char, freq in frequency_table.items()]

    while len(nodes) > 1:
        node1 = find_min_freq_node(nodes)
        nodes.remove(node1)
        node2 = find_min_freq_node(nodes)
        nodes.remove(node2)

        merged_freq = node1.freq + node2.freq
        merged_node = Node(freq=merged_freq)
        merged_node.left = node1
        merged_node.right = node2

        nodes.append(merged_node)

    return nodes[0] if nodes else None

def build_encoding_table(huffman_tree):
    encoding_table = {}

    def build_codes(node, current_code):
        if node.char:
            encoding_table[node.char] = current_code
        else:
            build_codes(node.left, current_code + "0")
            build_codes(node.right, current_code + "1")

    build_codes(huffman_tree, "")
    return encoding_table

def huffman_encoding(data):
    if not data:
        return "0", None

    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)

    encoded_data = ""
    for char in data:
        encoded_data += encoding_table[char]

    return encoded_data, huffman_tree

def huffman_decoding(encoded_data, huffman_tree):
    if not encoded_data or not huffman_tree:
        return ""

    decoded_data = ""
    current_node = huffman_tree
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_data += current_node.char
            current_node = huffman_tree

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    ## Additional Test Cases

    # Test Case 1: Empty input
    empty_data = ""
    print("The size of the empty data is: {}\n".format(sys.getsizeof(empty_data)))
    # The size of the empty data is: 49
    encoded_empty_data, empty_tree = huffman_encoding(empty_data)
    print("The size of the encoded empty data is: {}\n".format(sys.getsizeof(int(encoded_empty_data, base=2))))
    # The size of the encoded empty data is: 24
    print("The content of the encoded empty data is: {}\n".format(encoded_empty_data))
    # The content of the encoded empty data is: 0
    decoded_empty_data = huffman_decoding(encoded_empty_data, empty_tree)
    print("The size of the decoded empty data is: {}\n".format(sys.getsizeof(decoded_empty_data)))
    # The size of the decoded empty data is: 49
    print("The content of the decoded empty data is: {}\n".format(decoded_empty_data))
    # The content of the decoded empty data is:

    # Test Case 2: Large, repeating input
    repeating_data = "Clare is a great computer scientist." * 10000
    print("The size of the repeating data is: {}\n".format(sys.getsizeof(repeating_data)))
    # The size of the repeating data is: 360049
    encoded_repeating_data, repeating_tree = huffman_encoding(repeating_data)
    trimmed = encoded_repeating_data[:10]
    print("The size of the encoded repeating data is: {}\n".format(sys.getsizeof(int(encoded_repeating_data, base=2))))
    # The size of the encoded repeating data is: 185360
    print("The (first part) of the encoded repeating data is: {}\n".format(trimmed))
    # The (first part) of the encoded repeating data is: 0110001101
    decoded_repeating_data = huffman_decoding(encoded_repeating_data, repeating_tree)
    trimmed = decoded_repeating_data.split('.')[0]
    print("The size of the decoded repeating data is: {}\n".format(sys.getsizeof(decoded_repeating_data)))
    # The size of the decoded repeating data is: 360049
    print("The (first part) of the decoded repeating data is: {}\n".format(trimmed))
