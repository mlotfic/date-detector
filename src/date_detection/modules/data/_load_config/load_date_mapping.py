# -
# Import path helper to ensure modules directory is in sys.path
# ===================================================================================
if __name__ == "__main__":
    print("This module is not intended to be run directly. Import it in your code.")
    # This is necessary for importing other modules in the package structure
    from path_helper import add_modules_to_sys_path
    # Ensure the modules directory is in sys.path for imports
    add_modules_to_sys_path()
    # Optionally, add data directory to sys.path
    add_data_to_sys_path()


