import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Args:
      suffix(str): suffix of the file names to be found
      path(str): path of the file system

    Returns:
      a list of paths
    """
    # Cannot proceed if path or suffix are empty or None
    if not path or not suffix:
        return []
    # List to store the found file paths
    file_paths = []

    def find_files_recursive(suffix, path):
        # Check if the current path is a file with the desired suffix

        if os.path.isfile(path) and path.endswith(suffix):
            file_paths.append(path)
        # Check if the current path is a directory
        elif os.path.isdir(path):
            # Iterate over all items in the directory
            for item in os.listdir(path):
                # Recursive call for subdirectories
                find_files_recursive(suffix, os.path.join(path, item))

    find_files_recursive(suffix, path)
    return file_paths

# Note: These assume testdir is saved in project directory (i.e. same dir as problem_2.py)
# Test Case 1: Normal case with files ending in ".c"
files = find_files(".c", "./testdir")
print(files)
# Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

# Test Case 2: Edge case with non-existent suffix
files = find_files(".txt", "./testdir")
print(files)
# Expected output: []

# Test Case 3: Edge case with empty directory
files = find_files(".c", "./emptydir")
print(files)
# Expected output: []

# Test Case 4: Edge case with null values
files = find_files(None, None)
print(files)
# Expected output: []

# Test Case 4: Edge case with empty values
files = find_files("", "")
print(files)
# Expected output: []

# Expected output: [list of file paths ending with ".c" in the large_dir directory and its subdirectories]
