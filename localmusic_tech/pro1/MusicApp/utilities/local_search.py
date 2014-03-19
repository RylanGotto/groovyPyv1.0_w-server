import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = {}  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
	    if filename.endswith('.mp3'):  
                filepath = os.path.join(root, filename) # Join the two strings in order to form the full filepath. 
                file_paths.update({filepath:filename})  # Add it to the list.

    return file_paths  # Self-explanatory.


def get_filenames(directory):

    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.mp3'):  
                file_paths.append(filename)  # Add it to the list.
    return file_paths  # Self-explanatory.


