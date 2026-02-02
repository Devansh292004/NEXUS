import unittest
from nexus.algorithm_library import MerkleTree, AlgorithmLibrary
from nexus.advanced_data_structure_synthesis import AdvancedDataStructureSynthesis
from nexus.memory_management_optimizer import MemoryManagementOptimizer
from nexus.concurrency_ipc_synthesizer import ConcurrencyIPCSynthesizer

class TestNexusComponents(unittest.TestCase):
    def test_merkle_tree(self):
        data = ["A", "B", "C", "D"]
        tree = MerkleTree(data)
        self.assertIsNotNone(tree.root)
        self.assertEqual(len(tree.leaves), 4)

    def test_structure_selection(self):
        analysis = {"constraints": ["Must be fast and concurrent"]}
        synthesis = AdvancedDataStructureSynthesis()
        results = synthesis.process(analysis)
        self.assertIn("LOCK_FREE_QUEUE", results["selected_structures"])
        self.assertIn("ARENA_ALLOCATOR", results["selected_structures"])

    def test_memory_strategy(self):
        analysis = {"requirements": ["batch processing of lifetime grouped objects"]}
        optimizer = MemoryManagementOptimizer()
        results = optimizer.process(analysis)
        self.assertEqual(results["allocation"], "Arena Allocator")

    def test_concurrency_selection(self):
        analysis = {"requirements": ["Must handle signals and threads"]}
        synthesizer = ConcurrencyIPCSynthesizer()
        results = synthesizer.process(analysis)
        self.assertEqual(results["threads"], "POSIX Threads")
        self.assertIn("SIGNAL_HANDLER", results["templates"])

if __name__ == "__main__":
    unittest.main()
