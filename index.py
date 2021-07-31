import hashlib
import datetime

class Block:
    def __init__(self,previous_hash,data,timestamp):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.hash = self.get_hash()

    def get_hash(self):
        header_bin = (str(self.previous_hash)+str(self.data)+str(self.timestamp)).encode()
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest().encode()
        return outer_hash

    @staticmethod   
    def create_genesis_block():
        return Block("0","0",datetime.datetime.now())





