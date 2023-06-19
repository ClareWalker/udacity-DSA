Explanation:

 - The find_files function takes a suffix (e.g., ".c") and a path as inputs and returns a list of file paths. we are using a list (file_paths) to collect the paths of files that match the desired suffix. This allows us to return all the file paths as a result.
 - Inside the function, we define a helper function called find_files_recursive that performs the actual recursive search for files.
 - In the find_files_recursive function, we first check if the current path is a file with the desired suffix. If it is, we add the path to the file_paths list.
 - If the current path is a directory, we iterate over all items in that directory using os.listdir. For each item, we make a recursive call to find_files_recursive, passing the suffix and the joined path of the current directory and the item.
 - By using recursion, we can traverse the directory structure and search for files in all subdirectories.

Time Complexity:

 - The time complexity of the function depends on the number of files and directories in the file system hierarchy.
 - In the worst case, where every item in the file system is a file and ends with the desired suffix, the function will visit all the files in the file system hierarchy once.
 - If there are n files/directories in the file system hierarchy, the time complexity of the function can be considered as O(n).

Space Complexity:

 - The space complexity of the function depends on the recursive stack depth and the size of the file_paths list.
 - In the worst case, where the file system hierarchy is deep and all files end with the desired suffix, the recursive stack depth will be equal to the depth of the file system hierarchy.
 - If there are m levels of directories in the file system hierarchy, the space complexity of the function can be considered as O(m).
 - The file_paths list stores the paths of all the files that match the desired suffix. In the worst case, if all files in the file system hierarchy end with the suffix, the size of the file_paths list will be equal to the number of files in the hierarchy, which is n.
 - Therefore, the space complexity of the function can be considered as O(n + m).

In summary, the time complexity of the function is O(n), and the space complexity is O(n + m), where n is the number of files/directories in the file system hierarchy, and m is the depth of the file system hierarchy.