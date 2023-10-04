""" Python script to validate data

Run as:

    python3 scripts/validate_data.py data
"""

from pathlib import Path
import sys
import hashlib
# import numpy as np
# import pandas as pd

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
UNDERLINE = '\033[4m'
CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

# +
"""soluttion 1 """
def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    # Open the file, read contents as bytes.
    pth = Path(filename)
    pth_bytes = pth.read_bytes()
    # Calculate, return SHA1 has on the bytes from the file.
    pth_bytes_HEXsha1 = hashlib.sha1(pth_bytes).hexdigest()
#     print('file_hash done')
    # This is a placeholder, replace it to write your solution.
    return pth_bytes_HEXsha1
#     ('This is just a template -- you are expected to code this.')

"""soluttion 2 """
# def file_hash(filename):
#     """Calculate SHA1 hash of file contents.

#     Parameters:
#     filename (str): The path to the file.

#     Returns:
#     str: The SHA1 hash of the file contents.
#     """
#     # Initialize the SHA1 hash object
#     sha1 = hashlib.sha1()

#     # Open the file in binary read mode
#     with open(filename, 'rb') as file:
#         while True:
#             # Read a chunk of the file
#             chunk = file.read(4096)  # You can adjust the chunk size as needed

#             # If the chunk is empty (end of file), break the loop
#             if not chunk:
#                 break

#             # Update the hash object with the bytes from the chunk
#             sha1.update(chunk)

#     # Get the hexadecimal representation of the hash
#     hash_value = sha1.hexdigest()

#     return hash_value
# -

def validate_data(data_directory):
    """ Read ``data_hashes.txt`` file in `data_directory`, check hashes

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``data_hashes.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``data_hashes.txt`` file.
    """
    # Read lines from ``data_hashes.txt`` file.
    # Split into SHA1 hash and filename
    # Calculate actual hash for given filename.
    # If hash for filename is not the same as the one in the file, raise
    # ValueError
    # This is a placeholder, replace it to write your solution.
    # Create an empty list to store the address of *.txt files
#     print('initiate validate_data')
    txt_file_paths = []  
    # Create a Path object for the current directory
    files_directory = Path(data_directory)
#     sys.stdout.write(RED)
#     print(files_directory)
#     sys.stdout.write(RESET)
#     data_directory_path = current_path / '..' /  data_directory
#     files_directory = data_directory_path / 'group-02'
#     print('validate_data initiation done')

    # Iterate through the files in the data directory
    for file in files_directory.iterdir():
        if file.is_file() and file.suffix == '.txt':
            txt_file_paths.append(file)
#             sys.stdout.write(CYAN)
#             print(file)
#             sys.stdout.write(RESET)

    # Convert the Path object to a string before opening the file
#     sys.stdout.write(RED)
#     print(txt_file_paths[0])
#     sys.stdout.write(RESET)
    txt_file_path_str = txt_file_paths[0].resolve()
    
    data_directory_path = files_directory.parent
#     sys.stdout.write(BLUE)
#     print(data_directory_path)
#     sys.stdout.write(RESET)
    # Create an empty list to store the lines from hash_list.txt
    hash_list = [] 
    # Open the file for reading
    with open(txt_file_path_str, 'r') as file:
        for line in file:
            hash_list.append(line.strip())  # Append each line to the list after stripping newline characters
#             sys.stdout.write(CYAN)
#             print(line)
#             sys.stdout.write(RESET)
    #         line_str = line.split()[1].resolve()
            full_path = data_directory_path / line.split()[1]
            line_HEXsha1 = file_hash(str(full_path))
#             print('validate_data almost done')
            if line_HEXsha1 != line.split()[0]:
                raise NotImplementedError(f'hash value for {file} is different from hash value recorded in ``hash_list.txt`` file')


# +
"""This is a test cell. 
It is just for testing, 
afetr that we should make it as a comment"""
# # Create an empty list to store the address of *.txt files
# txt_file_paths = []  
# # Create a Path object for the current directory
# current_path = Path('.')

# data_directory = current_path / '..' /  'data'
# files_directory = data_directory / 'group-02'

# # Iterate through the files in the data directory
# for file in files_directory.iterdir():
#     if file.is_file() and file.suffix == '.txt':
#         txt_file_paths.append(file)
#         print(file)

# # Convert the Path object to a string before opening the file
# txt_file_path_str = txt_file_paths[0].resolve()      

# # Create an empty list to store the lines from hash_list.txt
# hash_list = [] 
# # Open the file for reading
# with open(txt_file_path_str, 'r') as file:
#     for line in file:
#         hash_list.append(line.strip())  # Append each line to the list after stripping newline characters
#         print(line)
# #         line_str = line.split()[1].resolve()
#         full_path = data_directory / line.split()[1]
#         line_HEXsha1 = file_hash(str(full_path))
#         if line_HEXsha1 != line.split()[0]:
#             raise NotImplementedError(f'hash value for {file} is different from hash value recorded in ``hash_list.txt`` file')

# # Path2data = current_path / '..' /  'data'/ hash_list[0].split()[1]


# # # Now, you can access the current path as a string using the 'resolve' method
# # Path2data_str = Path2data.resolve()
# # print(Path2data)
# # print(file_hash(Path2data_str))
# # print(hash_list[0])
# validate_data('data')
# -

def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    current_path = Path('.')
    data_directory_path = current_path / data_directory
    files_directory = data_directory_path / 'group-02'
    files_directory_str = files_directory.resolve()
    # Call function to validate data in data directory
    validate_data(files_directory_str)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()


