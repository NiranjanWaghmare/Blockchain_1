from datetime import datetime
from index import Block

block_chain = [Block.create_genesis_block()]
# print("Hash: %s"%block_chain[-1].hash)
# print("Hash: %s"%block_chain[-1].hash)
num_of_blocks = 10


for i in range(1, num_of_blocks+1):
    block_chain.append(Block(block_chain[-1].hash,"DATA!!",datetime.now()))
    print("Block #%d has been created: %s %s %s %s"%(i,block_chain[i].data,block_chain[i].hash,block_chain[i].timestamp,block_chain[i].previous_hash))

