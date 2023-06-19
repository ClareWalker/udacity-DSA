# Helper class to implement doubly-linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        # dictionary used for cache
        self.cache = {}
        # doubly-linked list used to keep record of usage
        # head and tail are place-holders
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # get() call counts as usage
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            # move node to head (most recently used)
            self._remove(node)
        else:
            if len(self.cache) >= self.capacity:
                # remove least recently used node
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]
            # add new node to cache
            node = Node(key, value)
            self.cache[key] = node
        # for both cases, add node as most recently used
        self._add(node)

    def _add(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # Output: 1
print(our_cache.get(2))  # Output: 2
print(our_cache.get(9))  # Output: -1

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # Output: -1

# Additional Test Cases

# Test Case 1: Testing with null values
our_cache = LRU_Cache(5)
our_cache.set(None, None)
print(our_cache.get(None))  # Output: None

# Test Case 2: Testing with empty values
our_cache = LRU_Cache(5)
our_cache.set('', '')
print(our_cache.get(''))  # Output: ''

# Test Case 3: Testing with large values
our_cache = LRU_Cache(5)
our_cache.set(1000000, 'large')
print(our_cache.get(1000000))  # Output: 'large'
