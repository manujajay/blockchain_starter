"""
This script demonstrates a simplified blockchain system integrated with basic DeFi (Decentralized Finance) concepts.
The core components of the script include a transaction structure, a block structure, a blockchain structure,
a basic proof-of-work mechanism, and a simplified DeFi lending pool. 

- Transaction class represents a transfer of value between two addresses.
- Block class represents a collection of transactions and includes a proof-of-work value.
- Blockchain class represents a chain of blocks and includes methods for adding transactions, 
  mining new blocks, and verifying the integrity of the chain.
- LendingPool class represents a simplified DeFi lending pool where users can deposit and borrow funds.
- A testing function `test_blockchain` is included to demonstrate the functionality of the script.

This script aims to provide a foundational understanding of how blockchain and DeFi systems operate.
"""

import hashlib
import time
import json

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender  # Address of the sender
        self.recipient = recipient  # Address of the recipient
        self.amount = amount  # Amount being transferred

    def to_json(self):
        # Converts the transaction object to a JSON string
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof, hash=None):
        self.index = index  # Index of the block in the blockchain
        self.previous_hash = previous_hash  # Hash of the previous block
        self.timestamp = timestamp  # Timestamp when the block is created
        self.transactions = transactions  # List of transactions in the block
        self.proof = proof  # Proof of work value
        self.hash = hash or self.calculate_hash()  # Hash of the block

    def calculate_hash(self):
        """
        Calculates the hash of the block based on its contents.
        """
        value = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof)
        value = value.encode()
        return hashlib.sha256(value).hexdigest()
    
    def mine_block(self, difficulty):
        while self.calculate_hash()[:difficulty] != '0' * difficulty:
            self.proof += 1
        print(f'Block mined with hash: {self.calculate_hash()}')

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initializes the blockchain with a genesis block
        self.pending_transactions = []  # Holds transactions before they are added to a block
        self.mining_reward = 50  # Reward for mining a block
        self.difficulty = 2  # Difficulty level for mining

    def create_genesis_block(self):
        # Creates the genesis block of the blockchain
        return Block(0, "0", int(time.time()), [], 0)

    def get_latest_block(self):
        # Retrieves the latest block in the blockchain
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        # This transaction will reward the miner for their work
        reward_transaction = Transaction(None, miner_address, self.mining_reward)
        # Including the reward transaction with the other pending transactions
        self.pending_transactions.append(reward_transaction)
        block = Block(len(self.chain), self.get_latest_block().hash, int(time.time()), self.pending_transactions, 0)
        block.mine_block(self.difficulty)
        print(f'Block successfully mined by {miner_address}!')
        self.chain.append(block)
        self.pending_transactions = []  # Resetting the list of pending transactions


    def add_transaction(self, transaction):
        # Adds a new transaction to the list of pending transactions
        self.pending_transactions.append(transaction)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():  # Updated line
                return False

            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def proof_of_work(self, block):
        # Implements proof of work for mining a block
        block.proof = 0
        while block.calculate_hash()[:self.difficulty] != '0' * self.difficulty:
            block.proof += 1
        return block.proof


    def get_balance_of_address(self, address):
        """
        Calculates and returns the balance of a given address.
        
        :param address: The address whose balance is to be calculated.
        :return: The balance of the address.
        """
        balance = 0  # Initialize balance to 0
        for block in self.chain:  # Iterate through each block in the blockchain
            for trans in block.transactions:  # Iterate through each transaction in the block
                # If the address is the recipient, add the amount to balance
                if trans.recipient == address:
                    balance += trans.amount
                # If the address is the sender, subtract the amount from balance
                if trans.sender == address:
                    balance -= trans.amount
        return balance

# DeFi Lending Pool
class LendingPool:
    def __init__(self):
        self.liquidity_pool = 0  # Amount of funds in the lending pool

    def deposit(self, amount):
        # Deposits an amount into the lending pool
        self.liquidity_pool += amount
        print(f'Deposit of {amount} made to the lending pool.')

    def borrow(self, amount):
        # Borrows an amount from the lending pool
        if self.liquidity_pool >= amount:
            self.liquidity_pool -= amount
            print(f'Borrow of {amount} made from the lending pool.')
        else:
            print('Insufficient funds in the lending pool.')

# Testing
def test_blockchain():
    test_chain = Blockchain()  # Create a new blockchain instance
    test_chain.add_transaction(Transaction('address1', 'address2', 100))  # Add transactions
    test_chain.add_transaction(Transaction('address2', 'address1', 50))
    test_chain.mine_pending_transactions('miner1')  # Mine transactions

    print(f'Balance of miner1 is {test_chain.get_balance_of_address("miner1")}')

    lending_pool = LendingPool()  # Create a new lending pool instance
    lending_pool.deposit(1000)  # Deposit and borrow from the lending pool
    lending_pool.borrow(500)
    lending_pool.borrow(600)

if __name__ == '__main__':
    test_blockchain()  # Run the testing function