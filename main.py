
from huffman_encoding import huffman
from huffman_decoding import encode_text, decode_huffman

if __name__ == "__main__":
    """
    Main function to execute Huffman encoding and decoding on user-provided text.
    """
    text = input("Give your text to encode: ")

    # Huffman Encoding
    huffman_codes, huffman_tree = huffman(text)  # Encode the text using Huffman coding

    # Encode the original text
    encoded_text = encode_text(text, huffman_codes)

    # Decode the encoded text
    decoded_text = decode_huffman(encoded_text, huffman_tree)

    # Output the results
    print("Original Text:", text)
    print("Encoded Text:", encoded_text)
    print("Decoded Text:", decoded_text)

    # Verify that the decoded text matches the original
    if decoded_text == text:
        print("Success: The decoded text matches the original text!")
    else:
        print("Error: The decoded text does not match the original text!")
