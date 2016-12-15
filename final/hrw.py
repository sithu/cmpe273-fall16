__doc__ = """

Rendezvous hashing (Highest Random Weight hashing) implementation.

"""

import md5

def md5_hash(key):
    """Given a string key, return a long hash value."""
    return long(md5.md5(key).hexdigest(), 16)

def weight(node, key):
    """Return the weight for the key on node.

    @params:
        node : hostname or IP string to be hashed.
        key : string to be hashed.

    """
    a = 1103515245
    b = 12345
    node_hash = md5_hash(node)
    key_hash = md5_hash(key)
    return (a * ((a * node_hash + b) ^ key_hash) + b) % (2^31)


class Ring(object):
    """A ring of nodes supporting rendezvous hashing based node selection."""
    def __init__(self, nodes=None):
        nodes = nodes or {}
        self._nodes = set(nodes)

    def add(self, node):
        """Add the given node to the _nodes set."""
        """ TODO """
        
    def nodes(self):
        return self._nodes

    def remove(self, node):
        """Remove the given node from the _nodes set."""
        """ TODO """
        
    def hash(self, key):
        """Return the node to which the given key hashes to."""
        assert len(self._nodes) > 0
        """ 
        TODO
        1. Loop through all the nodes.
        2. Compute the weight for each node for the given key.
        3. return the node that gave the highest weight.
        """
        
