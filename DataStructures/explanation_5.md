Explanation:

In this implementation, a linked list is used to connect the blocks in the blockchain. Each block contains a reference to the previous block, forming a chain-like structure. A linked list is suitable for this scenario because it allows for efficient insertion of new blocks at the beginning of the chain, which is the most common operation in a blockchain. The order of blocks is preserved in a linked list, making it easier to traverse and validate the chain.

Time complexity: 

The time complexity of adding a new block to the blockchain is O(1) because it involves creating a new block, updating the references, and assigning the hash. Retrieving or printing all the blocks in the blockchain requires traversing the linked list, resulting in a time complexity of O(n), where n is the number of blocks in the chain. The calculation of the hash for each block using the SHA-256 algorithm has a time complexity of O(1) as well.

Space complexity: 

The space complexity of the blockchain implementation depends on the number of blocks in the chain. Each block occupies space in memory to store its attributes such as timestamp, data, previous hash, and hash. Therefore, the space complexity is O(n), where n is the number of blocks in the blockchain. Additionally, a small constant amount of extra space is required for maintaining the linked list structure itself.