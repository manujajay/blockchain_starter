# Blockchain and DeFi Demonstration

This repository contains two scripts `app.py` and `defi.py` that demonstrate the basic concepts of blockchain and Decentralized Finance (DeFi) respectively.

## app.py: Simple Blockchain Structure

`app.py` demonstrates a simple blockchain structure in Python. A blockchain is a continuously growing list of records, called blocks, which are linked and secured using cryptography.

### Classes and Methods

- `Block` Class:
    - `__init__(self, index, previous_hash, timestamp, data, hash)`: Constructor for a Block.
    - `calculate_hash(index, previous_hash, timestamp, data)`: Calculates the hash value of a block based on its content.

- `Blockchain` Class:
    - `__init__(self)`: Constructor for a Blockchain, initializes a blockchain with a genesis block.
    - `create_genesis_block(self)`: Creates the genesis block.
    - `get_latest_block(self)`: Retrieves the latest block in the blockchain.
    - `add_block(self, new_block)`: Adds a new block to the blockchain.
    - `is_chain_valid(self)`: Validates the integrity of the blockchain.

- `test_blockchain()`: A function to test the Blockchain implementation.

## defi.py: DeFi Concepts Including Transactions, Mining, and Lending Pool

`defi.py` demonstrates more advanced blockchain concepts including transactions, proof of work, mining, and a simple DeFi lending pool application.

### Classes and Methods

- `Transaction` Class:
    - `__init__(self, sender, recipient, amount)`: Constructor for a Transaction.
    - `to_json(self)`: Converts the transaction data to a JSON string.

- `Block` Class:
    - `__init__(self, index, previous_hash, timestamp, transactions, proof, hash=None)`: Constructor for a Block with transactions and proof of work.
    - `calculate_hash(self)`: Calculates the hash value of a block based on its content.

- `Blockchain` Class:
    - `__init__(self)`: Constructor for a Blockchain, initializes with a genesis block.
    - `create_genesis_block(self)`: Creates the genesis block.
    - `get_latest_block(self)`: Retrieves the latest block in the blockchain.
    - `mine_pending_transactions(self, miner_address)`: Mines all pending transactions into a new block.
    - `add_transaction(self, transaction)`: Adds a new transaction to the list of pending transactions.
    - `is_chain_valid(self)`: Validates the integrity of the blockchain.
    - `proof_of_work(self, block)`: Implements proof of work for mining.
    - `mine_block(self, difficulty)`: Mines a new block with a specified level of difficulty.

- `LendingPool` Class:
    - `__init__(self)`: Constructor for a LendingPool.
    - `deposit(self, amount)`: Deposits an amount into the lending pool.
    - `borrow(self, amount)`: Borrows an amount from the lending pool.

- `test_blockchain()`: A function to test the Blockchain and LendingPool implementations.

## Objectives

- Understand and implement the basic structure of a blockchain.
- Demonstrate the concept of transactions and how they are added to blocks.
- Implement proof of work to secure the blockchain.
- Demonstrate a simple DeFi lending pool where users can deposit and borrow funds.
- Showcase the mining process and how miners are rewarded for their efforts.
