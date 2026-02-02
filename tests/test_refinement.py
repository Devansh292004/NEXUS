import unittest
from nexus.orchestrator import NexusOrchestrator
from unittest.mock import MagicMock

class TestRefinementLoop(unittest.TestCase):
    def test_refinement_iteration(self):
        orchestrator = NexusOrchestrator()

        # Mock ComplianceChecker to fail on first call and pass on second
        orchestrator.compliance_checker.process = MagicMock(side_effect=[
            {"status": "FAILED", "violations": ["gets"]},
            {"status": "PASSED"}
        ])

        # Mock TestingSystem to always report no leaks
        orchestrator.testing_system.process = MagicMock(return_value={
            "coverage_results": {"memory_leaks": "None"}
        })

        specification = "REQ: Use gets function. (Wait, Compliance will catch this)"
        results = orchestrator.run_pipeline(specification, max_iterations=2)

        self.assertEqual(orchestrator.compliance_checker.process.call_count, 2)
        self.assertEqual(results["status"], "Finalized")

    def test_max_iterations_reached(self):
        orchestrator = NexusOrchestrator()

        # Mock ComplianceChecker to always fail
        orchestrator.compliance_checker.process = MagicMock(return_value={
            "status": "FAILED", "violations": ["gets"]
        })

        orchestrator.testing_system.process = MagicMock(return_value={
            "coverage_results": {"memory_leaks": "None"}
        })

        specification = "REQ: Use gets function."
        results = orchestrator.run_pipeline(specification, max_iterations=2)

        self.assertEqual(orchestrator.compliance_checker.process.call_count, 2)
        # It still returns results but they will show failure status in compliance_results passed to output_guarantees
        self.assertEqual(results["status"], "Finalized")

if __name__ == "__main__":
    unittest.main()
