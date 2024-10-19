#!/usr/bin/python3
"""
A method that determines if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Function to validate UTF-8 encoding.
    
    Args:
        data (list): Data set containing multiple characters, where each integer
                     represents 1 byte of data.
    
    Returns:
        bool: True if the data is valid UTF-8 encoded, otherwise False.
    """
    utf8valid = 0
    
    for val in data:
        # Consider only the least significant 8 bits (1 byte)
        byte = val & 255
        
        # If we're expecting continuation bytes
        if utf8valid:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if byte >> 6 != 0b10:
                return False
            utf8valid -= 1
            continue
        
        # Determine the number of bytes in the current UTF-8 character
        while (1 << (7 - utf8valid)) & byte:
            utf8valid += 1
        
        # If utf8valid is 1 (invalid scenario) or greater than 4, it's invalid
        if utf8valid == 1 or utf8valid > 4:
            return False
        
        # If the byte represents a single-byte character, reset utf8valid
        utf8valid = max(utf8valid - 1, 0)
    
    # After processing all data, ensure there are no pending continuation bytes
    return utf8valid == 0

