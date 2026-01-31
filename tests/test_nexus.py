import unittest
from nexus.orchestrator import NexusOrchestrator

class TestNexusIntegration(unittest.TestCase):
    def test_full_pipeline(self):
        orchestrator = NexusOrchestrator()
        specification = """
        Assignment: Implement a fast memory allocator.
        REQ: Must use slab allocation.
        REQ: Must be performance-optimized for small objects.
        """
        results = orchestrator.run_pipeline(specification)

        self.assertIn("certification", results)
        self.assertEqual(results["certification"], "100% Correctness Guaranteed")
        print("\nIntegration test results:", results)

if __name__ == "__main__":
    unittest.main()
