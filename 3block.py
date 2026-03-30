import hashlib
import time
import random
# Simulating IoT Nodes
nodes = ["Node1", "Node2", "Node3"]
# PoW Function
def proof_of_work(last_proof, difficulty=4):
 proof = 0
 start_time = time.time()
 while True:
 hash_result = hashlib.sha256(f"{last_proof}{proof}".encode()).hexdigest()
 if hash_result[:difficulty] == "0" * difficulty: # Condition for valid block
Page | 29
 end_time = time.time()
 return proof, hash_result, end_time - start_time
 proof += 1
# Running PoW Simulation
last_proof = 0
for node in nodes:
 print(f"\n{node} is mining...")
 proof, block_hash, time_taken = proof_of_work(last_proof)
 print(f"{node} found proof: {proof}")
 print(f"Block Hash: {block_hash}")
 print(f"Time Taken: {time_taken:.2f} seconds")
 last_proof = proof # Update last proof for next round

‐------------


# Simulating stakes (IoT nodes with different stakes)
stakes = {
 "Node1": 5, # Lower stake
 "Node2": 20, # Higher stake
 "Node3": 10 # Medium stake
}
def select_validator(stakes):
 total_stake = sum(stakes.values())
 choice = random.uniform(0, total_stake)
 cumulative = 0
 
 for node, stake in stakes.items():
 cumulative += stake
 if choice <= cumulative:
 return node
# Running PoS Simulation
for _ in range(5): # Simulate 5 block validations
 validator = select_validator(stakes)
 print(f"Block validated by: {validator}")
