# huffman_encoding.py

def max_heap(array):
    """
    Converts a list of tuples (frequency, character) into a max heap.

    Parameters:
    array (list of tuples): The array to be converted into a max heap.

    Returns:
    list: The array arranged as a max heap.
    """
    l = len(array)

    def repair_up(index):
        """
        Repairs the heap upwards from a given index.

        Parameters:
        index : The index of the element to repair.
        """
        holder = array[index]
        # Move up the heap while the parent is smaller than the holder
        while index > 0 and array[(index - 1) // 2][0] < holder[0]:  # Compare frequencies only
            array[index] = array[(index - 1) // 2]  # Move parent down
            index = (index - 1) // 2  # Move to the parent's index
        array[index] = holder  # Place holder at the correct position

    def repair_down(index):
        """
        Repairs the heap downwards from a given index.

        Parameters:
        index (int): The index of the element to repair.
        """
        holder = array[index]
        while 2 * index + 1 < l:  # While there is at least one child (left child)
            child = 2 * index + 1  # Left child index
            # Choose the larger child if there's a right child
            if child + 1 < l and array[child][0] < array[child + 1][0]:  # Compare frequencies
                child += 1
            if holder[0] >= array[child][0]:  # If holder's frequency is larger or equal, stop
                break
            array[index] = array[child]  # Move the larger child up
            index = child  # Move to the child's index
        array[index] = holder  # Place holder at the correct position

    # Build the heap in O(n) time
    for i in range((l - 2) // 2, -1, -1):
        repair_down(i)

    # Then, repair upwards for the newly added elements to maintain the max-heap property
    for i in range(1, l):
        repair_up(i)

    return array


def huffman(Text):
    """
    Encodes a given text using Huffman coding.

    Parameters:
    Text (str): The input text to be encoded.

    Returns:
    tuple: A tuple containing a dictionary of Huffman codes and the root of the Huffman tree.
    """
    
    # Step 1: Count the frequency of each character
    def count(X):
        """
        Counts the frequency of each character in the input string.

        Parameters:
        X (str): The input string.

        Returns:
        dict: A dictionary where keys are characters and values are their frequencies.
        """
        num_of_char = {}
        for char in X:
            if char not in num_of_char:
                num_of_char[char] = 1
            else:
                num_of_char[char] += 1
        return num_of_char

    char_count = count(Text)

    # Step 2: Prepare the heap array for Huffman nodes
    heap = []
    for char, freq in char_count.items():
        heap.append((freq, char))  # Create tuple (frequency, character)

    # Convert the list into a max heap
    heap = max_heap(heap)

    # Step 3: Build the Huffman Tree
    while len(heap) > 1:
        # Pop the two nodes with the smallest frequencies (at the end of the heap)
        left = heap.pop()   # Node with smaller frequency
        right = heap.pop()  # Node with next smaller frequency

        # Merge these two nodes
        merged = (left[0] + right[0], left, right)  # New node: (total frequency, left, right)
        heap.append(merged)  # Add merged node back to heap
        
        # Maintain the heap property
        heap = max_heap(heap)

    # The last remaining node is the root of the Huffman Tree
    root = heap[0]

    # Step 4: Generate codes by traversing the tree
    codes = {}

    def generate_codes(node, current_code=""):
        """
        Generates Huffman codes by traversing the Huffman tree.

        Parameters:
        node (tuple): The current node of the Huffman tree.
        current_code (str): The code generated so far.
        """
        if len(node) == 2:  # Leaf node
            char = node[1]
            codes[char] = current_code
            return
        # Traverse left
        generate_codes(node[1], current_code + "0")
        # Traverse right
        generate_codes(node[2], current_code + "1")

    generate_codes(root)

    return codes, root  # Return both the codes and the root of the Huffman Tree
