To implement the LRU Cache, we can use a combination of a doubly linked list and a dictionary (hash map).

 - The doubly linked list will help us maintain the order of the elements based on their usage. The most recently used element will be placed at the head of the list, and the least recently used element will be at the tail.
 - The dictionary will serve as a lookup table, allowing us to quickly access elements based on their keys.
 
Explanation:

1. Doubly-Linked List:

   - We use a doubly-linked list to keep track of the order of the elements based on their usage. The most recently used element is placed at the head of the list, while the least recently used element is at the tail.
   - The doubly-linked list allows us to efficiently perform two crucial operations: insertion at the head and removal from any position in the list.
   - When a cache hit occurs (i.e., an element is accessed), we move the corresponding node to the head of the list to indicate its updated usage.
   - When the cache is full and we need to remove the least recently used element, we can simply remove the node at the tail of the list.
   - Overall, the doubly-linked list helps us maintain the order of elements and perform efficient removal and insertion operations, all of which are crucial for an LRU Cache.

2. Dictionary (Hash Map):

   - We use a dictionary to achieve fast lookup of elements based on their keys.
   - The dictionary allows us to quickly determine if a key exists in the cache and retrieve its corresponding node in constant time.
   - When we access an element (cache hit) or insert a new element, we update the dictionary accordingly to keep track of the key-node mappings.
   - The dictionary's fast lookup capability is essential for the constant-time performance requirement of the LRU Cache.
   - By combining the doubly-linked list and the dictionary, we can efficiently implement the LRU Cache operations:
 
Time Complexity:

Both the get and set operations have a time complexity of O(1) since we're using a dictionary to achieve constant time lookup, and the linked list operations (addition and removal) are also constant time O(1).

Space Complexity:

The space complexity is O(capacity) (e.g. O(5)) since we're using a dictionary and a linked list, both of which can store up to the capacity number of elements.