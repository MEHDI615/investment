import random
from node import Node

class StreamletProtocol:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes = [Node(i) for i in range(num_nodes)]
        self.epoch = 0
        self.chain_heads = {}  # Keep track of the latest block for each node

    def run_epoch(self, data="TX_DATA"):
        leader_id = self.choose_leader()
        leader = self.nodes[leader_id]

        parent_hash = self.chain_heads.get(leader_id, "GENESIS")
        proposed_block = leader.propose_block(parent_hash, data, self.epoch)

        votes = []
        for node in self.nodes:
            vote = node.vote(proposed_block)
            node.receive_vote(vote)
            votes.append(vote)

        # Broadcast votes to everyone
        for node in self.nodes:
            for vote in votes:
                node.receive_vote(vote)

        # Check for consensus
        for node in self.nodes:
            if node.has_supermajority(proposed_block.hash, self.num_nodes):
                node.add_block(proposed_block)
                self.chain_heads[node.node_id] = proposed_block.hash

        self.epoch += 1

    def choose_leader(self):
        return self.epoch % self.num_nodes
