# -*- coding: utf-8 -*-
'''
Created on Sun Jun 22 21:38:10 2025
@author: m.lotfi
@description: This module provides calendar conversion utilities and functions to get calendar variants.
'''

from .normalize_key import normalize_key

# Era normalization and keywords
# ===================================================================================
# This module provides functions to normalize era terms in different languages and calendars.
from .normalize_era import (
    normalize_era,  # Main era normalization function
)

# Month normalization and keywords
# ===================================================================================
# This module provides functions to normalize month names in different languages and calendars.
from .normalize_month import (
    normalize_month,  # Main month normalization function
    get_month_info,  # Get month information for a given month name
)

# Weekday normalization and keywords
# ===================================================================================
# This module provides functions to normalize weekday names in different languages.
from .normalize_weekday import (
    normalize_weekday,  # Main weekday normalization function
    get_weekday_info,  
)

# Numeric word normalization
# ===================================================================================
# This module provides functions to normalize numeric words in Arabic.
from .normalize_numeric_words import (
    numeric_words_pattern_ar,  # Regex pattern for Arabic numeric words
)

from .normalize_key import normalize_key

# Exported functions
# ===================================================================================
# This section defines the functions that will be available when this module is imported.
__all__ = [
    "normalize_key",
    # Era normalization and keywords
    "normalize_era",  # Main era normalization function
    
    # Month normalization and keywords
    "normalize_month",  # Main month normalization function
    "get_month_info",  # Get month information for a given month name
    
    # Weekday normalization and keywords
    "normalize_weekday",  # Main weekday normalization function
    "get_weekday_info",  # All weekday keywords
    
    # Numeric word normalization
    "numeric_words_pattern_ar",  # Regex pattern for Arabic numeric words
]