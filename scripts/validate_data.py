""" Python script to validate data

Run as:

    python3 scripts/validate_data.py data
"""

from pathlib import Path
import sys
import hashlib
import numpy as np
import pandas as pd

# +
hash_list = []  # Create an empty list to store the lines from hash_list.txt

# Open the file for reading
with open('../data/group-02/hash_list.txt', 'r') as file:
    for line in file:
        hash_list.append(line.strip())  # Append each line to the list after stripping newline characters

# Create a Path object for the current directory
current_path = Path('.')
Path2data = current_path / '..'/  'data'/ hash_list[0].split()[1]


# Now, you can access the current path as a string using the 'resolve' method
Path2data_str = Path2data.resolve()
print(Path2data)
print(file_hash(Path2data_str))
print(hash_list[0])


# +
# def file_hash(filename):
#     """ Get byte contents of file `filename`, return SHA1 hash

#     Parameters
#     ----------
#     filename : str
#         Name of file to read

#     Returns
#     -------
#     hash : str
#         SHA1 hexadecimal hash string for contents of `filename`.
#     """
#     # Open the file, read contents as bytes.
#     # Calculate, return SHA1 has on the bytes from the file.
#     # This is a placeholder, replace it to write your solution.
#     raise NotImplementedError(
#         'This is just a template -- you are expected to code this.')
def file_hash(filename):
    """Calculate SHA1 hash of file contents.

    Parameters:
    filename (str): The path to the file.

    Returns:
    str: The SHA1 hash of the file contents.
    """
    # Initialize the SHA1 hash object
    sha1 = hashlib.sha1()

    # Open the file in binary read mode
    with open(filename, 'rb') as file:
        while True:
            # Read a chunk of the file
            chunk = file.read(4096)  # You can adjust the chunk size as needed

            # If the chunk is empty (end of file), break the loop
            if not chunk:
                break

            # Update the hash object with the bytes from the chunk
            sha1.update(chunk)

    # Get the hexadecimal representation of the hash
    hash_value = sha1.hexdigest()

    return hash_value


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
    raise NotImplementedError('This is just a template -- you are expected to code this.')


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()


