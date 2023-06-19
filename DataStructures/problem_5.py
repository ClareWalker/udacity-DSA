import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash, previous_block):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = previous_block

    def get_hash(self):
        return self.hash

    def get_previous(self):
        return self.previous

    def print(self):
        print("Timestamp:", self.timestamp)
        print("Data:", self.data)
        print("Hash:", self.hash)
        print("Previous Hash:", self.previous_hash)
        print("-------------------")

    def calc_hash(self):
        sha = hashlib.sha256()
        # ensures unique hash for each block
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        # Add new blocks to head
        if self.head is None:
            timestamp = datetime.datetime.utcnow()
            self.head = Block(timestamp, data, 0, None)
        else:
            timestamp = datetime.datetime.utcnow()
            new_block = Block(timestamp, data, self.head.hash, self.head)
            self.head = new_block

    def get_block(self, hash):
        current_block = self.head
        while current_block:
            if current_block.get_hash() == hash:
                current_block.print()

        print('Alas, that block is not in this chain.')


    def print_blocks(self, n=100):
        current_block = self.head
        i = 0
        while current_block and i < n:
            current_block.print()
            current_block = current_block.get_previous()
            i+=1

# Note: Example output, exact values will differ for each run

# Test Case 1: Empty blockchain
blockchain = Blockchain()
blockchain.print_blocks()

# Test Case 2: Adding blocks to the blockchain
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.add_block("Block 3")
blockchain.print_blocks()
# Timestamp: 2023-06-11 16:40:16.233770
# Data: Block 3
# Hash: 2b84bd5d25cfea2ac922843642ac25c6530c101b45c216097c0a304a42c550af
# Previous Hash: daaf45e122b67a66941d127442008e6552a5717626950ebb0fd343911f270c13
# -------------------
# Timestamp: 2023-06-11 16:40:16.233763
# Data: Block 2
# Hash: daaf45e122b67a66941d127442008e6552a5717626950ebb0fd343911f270c13
# Previous Hash: efdabc929cd8ef8464c54582ffb541d2a505e9fe881a215af6f404cc042a8620
# -------------------
# Timestamp: 2023-06-11 16:40:16.233148
# Data: Block 1
# Hash: efdabc929cd8ef8464c54582ffb541d2a505e9fe881a215af6f404cc042a8620
# Previous Hash: 0
# -------------------


# Test Case 3: Large data in a block
blockchain.add_block("I am really enjoying this Udacity course." * 10)
blockchain.print_blocks(1)
# Timestamp: 2023-06-11 16:40:16.233834
# Data: I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.I am really enjoying this Udacity course.
# Hash: 854073fcc1a9566aa4d7975693998e97dce1a507fb24a942917dd678b697e95a
# Previous Hash: 2b84bd5d25cfea2ac922843642ac25c6530c101b45c216097c0a304a42c550af
# -------------------
