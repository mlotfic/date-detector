# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides a function to extract date component values from regex match objects.
    It handles both single and multiple group indices, returning the first non-empty value found.
"""

import re
from typing import Optional, Union, List


def get_match_value(match, idx: Optional[Union[int, str, List[Union[int, str]]]] = None) -> Optional[str]:
    """
    Extract component values from a regex match object.
    
    Args:
        match: A regex match object (or None if no match found)
        idx: Either an integer (single group index), a string (convertible to int),
             or a list of integers/strings (multiple group indices to try in order)
    
    Returns:
        str: The first non-empty captured group value found, or None if no match
    
    Example:
        match = re.search(r'(\d{4})-(\d{2})-(\d{2})', '2023-12-25')
        get_match_value(match, 1)        # Returns '2023'
        get_match_value(match, [1, 2])   # Returns '2023'
        get_match_value(match, "1")      # Returns '2023'
    """
    
    # Handle None match (no regex match found)
    if match is None:
        return None
    
    # Handle None idx
    if idx is None:
        return None
    
    # Handle single index (int or str)
    if isinstance(idx, (int, str)):
        try:
            # Convert string to int if needed
            group_idx = int(idx) if isinstance(idx, str) else idx
            
            # Validate index bounds (group 0 is the full match, groups start at 1)
            if group_idx < 0 or group_idx > len(match.groups()):
                return None
                
            group_value = match.group(group_idx)
            return group_value if group_value else None
            
        except (ValueError, IndexError):
            return None
    
    # Handle list of indices
    elif isinstance(idx, list):
        for single_idx in idx:
            group_value = get_match_value(match, single_idx)
            if group_value:  # Return first non-empty group
                return group_value
        return None
    
    else:
        return None


# Example usage and tests
if __name__ == "__main__":
    # Test cases
    test_string = "2023-12-25"
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    match = re.search(pattern, test_string)
    
    print("Test string:", test_string)
    print("Pattern:", pattern)
    print()
    
    # Test single index
    print("get_match_value(match, 1):", get_match_value(match, 1))    # Should return '2023'
    print("get_match_value(match, 2):", get_match_value(match, 2))    # Should return '12'
    print("get_match_value(match, '3'):", get_match_value(match, '3')) # Should return '25'
    
    # Test list of indices
    print("get_match_value(match, [1, 2]):", get_match_value(match, [1, 2]))  # Should return '2023'
    print("get_match_value(match, [5, 2]):", get_match_value(match, [5, 2]))  # Should return '12'
    
    # Test edge cases
    print("get_match_value(None, 1):", get_match_value(None, 1))      # Should return None
    print("get_match_value(match, None):", get_match_value(match, None)) # Should return None
    print("get_match_value(match, 10):", get_match_value(match, 10))  # Should return None
    print("get_match_value(match, []):", get_match_value(match, []))  # Should return None