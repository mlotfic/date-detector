# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 20:01:16 2025

@author: m.lotfi

@description:
    
"""
    
# my_package/path_helper.py
import sys
import os
from pathlib import Path



# Import path helper to ensure data directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other data in the package structure
    from path_helper import add_data_to_sys_path
    # Ensure the data directory is in sys.path for imports
    add_data_to_sys_path()
    # Optionally, add data directory to sys.path
    add_data_to_sys_path()
