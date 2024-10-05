# huffman_decoding.py

def decode_huffman(encoded_text, huffman_tree):
    """
    Decodes the encoded text using the Huffman tree.

    Parameters:
    encoded_text (str): The text encoded using Huffman coding.
    huffman_tree (tuple): The root of the Huffman tree used for decoding.

    Returns:
    str: The decoded text.
    """
    current_node = huffman_tree
    decoded_text = ""

    for bit in encoded_text:
        # Go left for '0' and right for '1'
        if bit == '0':
            current_node = current_node[1]  # Left child
        else:
            current_node = current_node[2]  # Right child
        
        # If we reach a leaf node, decode the character
        if len(current_node) == 2:  # Leaf node has only the character
            decoded_text += current_node[1]  # Append character to decoded text
            current_node = huffman_tree  # Go back to the root of the tree

    return decoded_text


def encode_text(text, huffman_codes):
    """
    Encodes the input text using the provided Huffman codes.

    Parameters:
    text (str): The text to be encoded.
    huffman_codes (dict): The dictionary containing characters as keys and their corresponding Huffman codes as values.

    Returns:
    str: The encoded text.
    """
    encoded_text = ""
    for char in text:  # Iterate through each character in the input text
        encoded_text += huffman_codes[char]  # Append the corresponding Huffman code for the character
    return encoded_text  # Return the fully encoded text
