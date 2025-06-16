import hashlib
import json

class Block:
    def __init__(self, proposer_id, parent_hash, data, epoch):
        self.proposer_id = proposer_id
        self.parent_hash = parent_hash
        self.data = data
        self.epoch = epoch
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            'proposer_id': self.proposer_id,
            'parent_hash': self.parent_hash,
            'data': self.data,
            'epoch': self.epoch
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block({self.epoch}, {self.proposer_id}, {self.hash[:6]}...)"
