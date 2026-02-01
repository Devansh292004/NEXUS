import unittest
from nexus.orchestrator import NexusOrchestrator
from nexus.compliance_checker import ComplianceChecker

class TestNexusIntegration(unittest.TestCase):
    def test_full_pipeline_with_templates(self):
        orchestrator = NexusOrchestrator()
        specification = """
        Assignment: Implement a fast and concurrent data store.
        REQ: Must use slab allocation.
        REQ: Must be performance-optimized.
        REQ: Must handle concurrent threads.
        REQ: Must include data integrity verification.
        """
        results = orchestrator.run_pipeline(specification)

        # In our implementation, orchestrator.run_pipeline returns OutputGuarantees.process output
        # But wait, I need to check the code itself.
        # OutputGuarantees.process doesn't return the code currently.
        # Let's check orchestrator.run_pipeline return value.
        self.assertIn("certification", results)

    def test_code_generation_content(self):
        orchestrator = NexusOrchestrator()
        specification = "REQ: Must be fast and concurrent. REQ: verification needed."
        # We need to peek into the pipeline.
        # Let's modify run_pipeline to return more info for testing or just test the parts.
        analysis_results = orchestrator.analysis_engine.process(specification)
        plans = {
            "structures": orchestrator.data_structure_synthesis.process(analysis_results),
            "concurrency": orchestrator.concurrency_synthesizer.process(analysis_results),
            "memory": orchestrator.memory_optimizer.process(analysis_results),
            "network": orchestrator.network_engine.process(analysis_results),
            "algorithms": orchestrator.algorithm_library.process(analysis_results)
        }
        verification_plan = orchestrator.verification_core.process(analysis_results)
        code_info = orchestrator.synthesis_framework.process(analysis_results, verification_plan, plans)

        code = code_info["code"]
        self.assertIn("Lock-free Queue", code)
        self.assertIn("Arena Allocator", code)
        self.assertIn("POSIX Thread Pool", code)
        self.assertIn("compute_sha256", code)

    def test_compliance_checker_detection(self):
        checker = ComplianceChecker()

        # Safe code
        safe_code = {"code": "#include <stdio.h>\nint main() { printf(\"Hello\"); return 0; }"}
        results = checker.process(safe_code)
        self.assertEqual(results["status"], "PASSED")

        # Unsafe code
        unsafe_code = {"code": "#include <stdio.h>\nint main() { char buf[10]; gets(buf); return 0; }"}
        results = checker.process(unsafe_code)
        self.assertEqual(results["status"], "FAILED")
        self.assertIn("gets", results["violations"])

if __name__ == "__main__":
    unittest.main()
