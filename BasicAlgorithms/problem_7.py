## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        # Initialize the trie with a root node and a handler for root path
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler

    def insert(self, path_parts, handler):
        # Insert a path and its associated handler into the Trie
        current_node = self.root

        for part in path_parts:
            current_node.insert(part)
            current_node = current_node.children[part]

        current_node.set_handler(handler)

    def find(self, path_parts):
        # Find the handler for a given path in the Trie
        current_node = self.root

        for part in path_parts:
            # In operator is efficient way to search dictionaries
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return self.not_found_handler

        return current_node.handler if current_node.handler else self.not_found_handler


## A RouteTrieNode will be similar to our autocomplete TrieNode, with an additional element - a handler
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def set_handler(self, handler):
        self.handler = handler

    def insert(self, part):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode()


## The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # Split the path and pass the parts as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        # Lookup path (by parts) and return the associated handler
        # Return None if it's not found, or the "not found" handler if added
        # Two slashes indicates empth path
        if '//' in path:
            return self.route_trie.not_found_handler

        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)

        if not handler and path[-1] == "/":
            # Check if path without trailing slash exists
            path_parts = self.split_path(path[:-1])
            handler = self.route_trie.find(path_parts)

        return handler

    def split_path(self, path):
        # Split the path into parts for both add_handler and lookup functions
        return [part for part in path.split("/") if part]



# Test Cases
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# Test Case 1: Root handler
# Expected output: 'root handler'
print(router.lookup("/"))

# Test Case 2: Not found handler
# Expected output: 'not found handler'
print(router.lookup("/home"))

# Test Case 3: Match for "/home/about"
# Expected output: 'about handler'
print(router.lookup("/home/about"))

# Test Case 4: Match for "/home/about/" with trailing slash
# Expected output: 'about handler'
print(router.lookup("/home/about/"))

# Test Case 5: Not found handler for "/home/about/me"
# Expected output: 'not found handler'
print(router.lookup("/home/about/me"))

# Additional Test Cases
# Test Case 7: Not found handler with trailing slash
# Expected output: 'not found handler'
print(router.lookup("/home/"))

# Test Case 8: Not found handler with multiple trailing slashes
# Expected output: 'not found handler'
print(router.lookup("/home/about//"))

# Test Case 9: Root handler with multiple trailing slashes
# Expected output: 'not found handler'
print(router.lookup("///"))

# Test Case 10: Root handler for empty path
# Expected output: 'root handler'
print(router.lookup(""))

