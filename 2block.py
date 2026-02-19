import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __str__(self):
        return f"Block {self.index} | Hash: {self.hash[:15]}... | Prev: {self.previous_hash[:15]}... | Data: {self.data}"

def calculate_hash(index, previous_hash, timestamp, data):
    block_content = f"{index}{previous_hash}{timestamp}{data}"
    return hashlib.sha256(block_content.encode()).hexdigest()

def create_genesis_block():
    ts = int(time.time())
    # Ensuring the hash uses the exact same timestamp stored in the block
    genesis_hash = calculate_hash(0, "0", ts, "Genesis Block")
    return Block(0, "0", ts, "Genesis Block", genesis_hash)

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash_value = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash_value)

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = create_new_block(previous_block, data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Verifies that the hashes and links are intact."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            # 1. Check if the block's own hash is correct
            if current.hash != calculate_hash(current.index, current.previous_hash, current.timestamp, current.data):
                return False
            
            # 2. Check if the block points correctly to the previous hash
            if current.previous_hash != previous.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(block)

# Execution
my_blockchain = Blockchain()
my_blockchain.add_block("Sensor data 1")
my_blockchain.add_block("Sensor data 2")
my_blockchain.add_block("Sensor data 3") # Added your third sensor

print("--- Blockchain Ledger ---")
my_blockchain.display_chain()

print(f"\nIs the blockchain valid? {my_blockchain.is_chain_valid()}")