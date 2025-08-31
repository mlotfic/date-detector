# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 23:01:21 2025

@author: m.lotfi

@description:
    This module provides a function to normalize date components for different languages and calendar systems.
    It handles both flat and nested structures, extracting and normalizing components like year, month, day, era, and weekday.
"""

# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()

from modules.keywords import era_keywords_dict

from typing import Optional, Dict, Union, Tuple

# ===================================================================================
# FUNCTION
# ===================================================================================
def normalize_era(era:str, lang=None) -> Tuple[str, str]:
    """
    Normalize era strings to standardized formats based on calendar system and language.
    
    Args:
        era (str): The era string to normalize (e.g., "AD", "BC", "AH", etc.)
        lang (str, optional): Target language for normalization ("en" or "ar")
    
    Returns:
        str: Normalized era string, or empty string if era is None/empty
    
    Raises:
        NameError: If required era constant dictionaries are not defined
    
    TODO: Consider using a configuration dictionary or class to reduce code duplication
    """
    # Handle None or empty era input
    if not era:
        return ""
    
    # Initialize normalized era variable
    n_calendar = ""
    n_era = ""
    
    try:
        # HIJRI CALENDAR - After Hijrah (AH)
        if era in era_keywords_dict["ar"]["hijri"]["after_hijrah"]["keywords"]:
            n_era = era_keywords_dict["ar"]["hijri"]["after_hijrah"]["normalized"]
            n_calendar = "hijri"
            if lang == "en":
                n_era = era_keywords_dict["en"]["hijri"]["after_hijrah"]["normalized"]
                
        elif era in era_keywords_dict["en"]["hijri"]["after_hijrah"]["keywords"]:
            n_era = era_keywords_dict["en"]["hijri"]["after_hijrah"]["normalized"]
            n_calendar = "hijri"
            if lang == "ar":
                n_era = era_keywords_dict["ar"]["hijri"]["after_hijrah"]["normalized"]
        
        # HIJRI CALENDAR - Before Hijrah (BH)
        elif era in era_keywords_dict["ar"]["hijri"]["before_hijrah"]["keywords"]:
            n_era = era_keywords_dict["ar"]["hijri"]["before_hijrah"]["normalized"]
            n_calendar = "hijri"
            if lang == "en":
                n_era = era_keywords_dict["en"]["hijri"]["before_hijrah"]["normalized"]
                
        elif era in era_keywords_dict["en"]["hijri"]["before_hijrah"]["keywords"]:
            n_era = era_keywords_dict["en"]["hijri"]["before_hijrah"]["normalized"]
            n_calendar = "hijri"
            if lang == "ar":
                n_era = era_keywords_dict["ar"]["hijri"]["before_hijrah"]["normalized"]
        
        # GREGORIAN CALENDAR - After Christ (AD/CE)
        elif era in era_keywords_dict["ar"]["gregorian"]["after_christ"]["keywords"]:
            n_era = era_keywords_dict["ar"]["gregorian"]["after_christ"]["normalized"]
            n_calendar = "gregorian"
            if lang == "en":
                n_era = era_keywords_dict["en"]["gregorian"]["after_christ"]["normalized"]
                
        elif era in era_keywords_dict["en"]["gregorian"]["after_christ"]["keywords"]:
            n_era = era_keywords_dict["en"]["gregorian"]["after_christ"]["normalized"]
            n_calendar = "gregorian"
            if lang == "ar":
                n_era = era_keywords_dict["ar"]["gregorian"]["after_christ"]["normalized"]
        
        # GREGORIAN CALENDAR - Before Christ (BC/BCE)
        elif era in era_keywords_dict["ar"]["gregorian"]["before_christ"]["keywords"]:
            n_era = era_keywords_dict["ar"]["gregorian"]["before_christ"]["normalized"]
            n_calendar = "gregorian"
            if lang == "en":
                n_era = era_keywords_dict["en"]["gregorian"]["before_christ"]["normalized"]
                
        elif era in era_keywords_dict["en"]["gregorian"]["before_christ"]["keywords"]:
            n_era = era_keywords_dict["en"]["gregorian"]["before_christ"]["normalized"]
            n_calendar = "gregorian"
            if lang == "ar":
                n_era = era_keywords_dict["ar"]["gregorian"]["before_christ"]["normalized"]
        
        # julian CALENDAR - After julian
        elif era in era_keywords_dict["ar"]["julian"]["after_hijrah"]["keywords"]:
            n_era = era_keywords_dict["ar"]["julian"]["after_hijrah"]["normalized"]
            n_calendar = "julian"
            if lang == "en":
                n_era = era_keywords_dict["en"]["julian"]["after_hijrah"]["normalized"]

        elif era in era_keywords_dict["en"]["julian"]["after_hijrah"]["keywords"]:
            n_era = era_keywords_dict["en"]["julian"]["after_hijrah"]["normalized"]
            n_calendar = "julian"
            if lang == "ar":
                n_era = era_keywords_dict["ar"]["julian"]["after_hijrah"]["normalized"]
        
        # julian CALENDAR - Before julian
        elif era in era_keywords_dict["ar"]["julian"]["before_hijrah"]["keywords"]:
            n_era = era_keywords_dict["ar"]["julian"]["before_hijrah"]["normalized"]
            n_calendar = "julian"
            if lang == "en":
                n_era = era_keywords_dict["en"]["julian"]["before_hijrah"]["normalized"]

        elif era in era_keywords_dict["en"]["julian"]["before_hijrah"]["keywords"]:
            n_era = era_keywords_dict["en"]["julian"]["before_hijrah"]["normalized"]
            n_calendar = "julian"
            if lang == "ar":
                n_era = era_keywords_dict["ar"]["julian"]["before_hijrah"]["normalized"]
        
        # UNRECOGNIZED ERA - No match found
        else:
            # Consider logging this case or raising a warning
            n_era = era  # Return original era if no match found
            n_calendar = ""
            
    except NameError as e:
        # Handle case where era constants are not defined
        raise NameError(f"Era constants not defined: {e}")
    
    return n_era, n_calendar