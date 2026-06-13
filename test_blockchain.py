# test_blockchain.py
"""
Tests for BlockChain module.
"""

import unittest
from blockchain import BlockChain

class TestBlockChain(unittest.TestCase):
    """Test cases for BlockChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockChain()
        self.assertIsInstance(instance, BlockChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
