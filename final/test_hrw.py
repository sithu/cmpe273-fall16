import unittest
import hrw

class RingTest(unittest.TestCase):
    def setUp(self):
        self.node1 = '127.0.0.1:3000'
        self.node2 = '127.0.0.1:4000'
        self.node3 = '127.0.0.1:5000'
        

    def test_add_remove(self):
        ring = hrw.Ring()
        ring.add(self.node1)
        ring.add(self.node2)
        ring.add(self.node3)
        self.assertEqual({self.node1, self.node2, self.node3}, ring.nodes())
        
        ring.remove(self.node1)
        self.assertEqual({self.node2, self.node3}, ring.nodes())
        ring.remove(self.node2)
        ring.remove(self.node3)
        self.assertEqual(set(), ring.nodes())


    def test_hash(self):
        ring = hrw.Ring({self.node1})
        keys = [str(x) for x in range(100)]
        for k in keys:
            self.assertEqual(self.node1, ring.hash(k))

        ring.add(self.node2)
        ring.add(self.node3)
        counts = {
            self.node1: 0,
            self.node2: 0,
            self.node3: 0
        }
        key2node_1 = []
        for k in keys:
            node = ring.hash(k)
            key2node_1.append((k, node))
            counts[node] += 1
        
        key2node_2 = []
        for k in keys:
            node = ring.hash(k)
            key2node_2.append((k, node))
        
        # Two iterations should generate the same key-2-node mapping.
        self.assertEqual(key2node_1, key2node_2)
        print "Num of entries / node:", counts
        # For 100 keys, each slot should have at least 10 entries.
        self.assertTrue(10 <= counts[self.node1])
        self.assertTrue(10 <= counts[self.node2])
        self.assertTrue(10 <= counts[self.node3])
        

if __name__ == "__main__":
    unittest.main()