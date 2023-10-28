"""
This script demonstrates a simple blockchain structure in Python. A blockchain is a continuously growing 
list of records, called blocks, which are linked and secured using cryptography. Each block contains 
an index, a timestamp (in Unix time), a data value, a hash of the previous block, and its own unique hash value.

The Blockchain class contains methods to create the genesis block, add new blocks to the chain, 
validate the integrity of the chain, and retrieve the latest block in the chain. The Block class 
represents the structure of an individual block on the chain.

The `test_blockchain` function at the bottom of the script creates a new Blockchain instance and adds 
some blocks to demonstrate how the blockchain works.
"""

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        """
        Constructor for a Block.
        
        :param index: Index of the block in the blockchain.
        :param previous_hash: Hash value of the previous block.
        :param timestamp: Timestamp when the block is created.
        :param data: Any data to be stored in the block.
        :param hash: Hash value of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
            """
            Calculates the hash value of a block.
            
            :param index: Index of the block.
            :param previous_hash: Hash value of the previous block.
            :param timestamp: Timestamp of the block creation.
            :param data: Data stored in the block.
            :return: Hash value of the block.
            """
            value = str(index) + str(previous_hash) + str(timestamp) + str(data)
            value = value.encode()
            return hashlib.sha256(value).hexdigest()

class Blockchain:
    def __init__(self):
        """
        Constructor for a Blockchain.
        Initializes a blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the genesis block.
        
        :return: The genesis block.
        """
        return Block(0, "0", int(time.time()), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Retrieves the latest block in the blockchain.
        
        :return: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain.
        
        :param new_block: The new block to be added.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = Block.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        
        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the hash value of the current block
            if current_block.hash != Block.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            # Validate the link between the current block and the previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        return True  # Return True if no invalid conditions were found

# Test the Blockchain
def test_blockchain():
    """
    Tests the Blockchain implementation.
    """
    test_chain = Blockchain()
    test_chain.add_block(Block(1, "", int(time.time()), "This is block 1", ""))
    test_chain.add_block(Block(2, "", int(time.time()), "This is block 2", ""))

    # Validate the blockchain
    print("Blockchain validity:", test_chain.is_chain_valid())

    # Output the blocks in the blockchain
    for block in test_chain.chain:
        print(f"Block #{block.index} has been added to the blockchain!")
        print(f"Hash: {block.hash}\\n")

if __name__ == '__main__':
    test_blockchain()
