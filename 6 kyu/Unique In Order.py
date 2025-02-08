"""
Description:
Implement the function unique_in_order which takes as argument a sequence and 
returns a list of items without any elements with the same value next to each other and 
preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""

def unique_in_order(sequence):
    if not sequence:
        return []
    else:
        letters = [char for char in sequence]
        result = []
        last_seen = None
        for char in sequence:
            if char != last_seen:
                result.append(char)
                last_seen = char
        return result
