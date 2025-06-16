from block import Block

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.blockchain = []
        self.received_votes = {}

    def propose_block(self, parent_hash, data, epoch):
        block = Block(proposer_id=self.node_id, parent_hash=parent_hash, data=data, epoch=epoch)
        return block

    def vote(self, block):
        """Vote for a block (simulate signature by ID)"""
        return {'block_hash': block.hash, 'voter_id': self.node_id}

    def receive_vote(self, vote):
        """Store vote received"""
        h = vote['block_hash']
        if h not in self.received_votes:
            self.received_votes[h] = []
        self.received_votes[h].append(vote['voter_id'])

    def has_supermajority(self, block_hash, total_nodes):
        """Check if a block has 2/3 majority"""
        return len(self.received_votes.get(block_hash, [])) >= (2 * total_nodes) // 3

    def add_block(self, block):
        """Add block to local chain"""
        self.blockchain.append(block)
