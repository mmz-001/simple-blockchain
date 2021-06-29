import hashlib
from datetime import datetime


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_tx = []

        # Add the genesis block the the Blockchain
        self.chain.append(self.genesis_block)

    @property
    def genesis_block(self):
        """The first block in the Blockchain."""
        block = {
            "index": 0,
            "timestamp": "0",
            "txs": "[]",
            "nonce": 634,
            "prev_hash": 0
        }

        return block

    def create_block(self, nonce=0):
        """Create a new block."""

        block = {
            "index": self.last_block["index"] + 1,
            "timestamp": str(datetime.now()),
            "txs": str(self.current_tx),
            "nonce": nonce,
            "prev_hash": self.hash(self.chain[-1])
        }

        # Reset current list of transactions
        self.current_tx.clear()

        return block

    def new_tx(self, sender, recipient, amount):
        """Create a new transaction."""

        self.current_tx.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

        return self.last_block["index"] + 1

    @staticmethod
    def hash(block):
        """Return the SHA-256 hash of a Block."""
        return hashlib.sha256(str(block).encode()).hexdigest()

    @property
    def last_block(self):
        """Return the last block in the chain."""
        return self.chain[-1]

    def proof(self, block):
        """Proof of work algorithm."""

        nonce = 0
        while not self.valid_proof(block):
            block["nonce"] = nonce
            nonce += 1

        self.chain.append(block)
        return nonce

    @staticmethod
    def valid_proof(block):
        """Validates the proof: Checks whether hash of the block contains 3 leading zeros."""
        return Blockchain.hash(block)[:3] == "000"


if __name__ == "__main__":
    blockchain = Blockchain()

    # Create a new transaction.
    blockchain.new_tx("Alice", "Bob", 5)

    # Mine a block.
    new_block = blockchain.create_block()
    blockchain.proof(new_block)

    # Print the current Blockchain.
    print(*blockchain.chain, sep="\n")




















