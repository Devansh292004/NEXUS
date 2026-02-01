import unittest
from nexus.multi_stage_analysis_engine import MultiStageAnalysisEngine
from nexus.formal_verification_core import FormalVerificationCore
from nexus.intelligent_testing_system import IntelligentTestingSystem
from nexus.compliance_checker import ComplianceChecker

class TestV7Features(unittest.TestCase):
    def test_requirement_decomposition(self):
        analysis = MultiStageAnalysisEngine()
        spec = "REQ: Implement a fast memory allocator and it must be thread-safe."
        results = analysis.process(spec)
        self.assertIn("atomic_reqs", results)
        self.assertTrue(len(results["atomic_reqs"]) >= 2)
        self.assertIn("Implement a fast memory allocator", results["atomic_reqs"])

    def test_test_case_inference(self):
        analysis = MultiStageAnalysisEngine()
        spec = "REQ: Must be performance-optimized."
        results = analysis.process(spec)
        self.assertIn("test_specs", results)
        self.assertTrue(any("Property: Execution time" in s for s in results["test_specs"]))

    def test_constraint_solving_simulation(self):
        verification = FormalVerificationCore()
        analysis_results = {"test_specs": ["Property: Memory safety"]}
        results = verification.process(analysis_results)
        self.assertIn("constraint_solving", results)
        self.assertEqual(results["constraint_solving"]["status"], "SAT")

    def test_mutation_testing_simulation(self):
        testing = IntelligentTestingSystem()
        results = testing.process({"code": "int main(){}"})
        self.assertIn("mutation_testing", results)
        self.assertEqual(results["mutation_testing"]["mutation_score"], "98%")

    def test_code_style_enforcement(self):
        checker = ComplianceChecker()
        # Code with TABS and CamelCase function
        bad_code = {"code": "void MyFunction() {\n\treturn;\n}"}
        results = checker.process(bad_code)
        self.assertEqual(results["status"], "FAILED")
        self.assertTrue(any("Naming convention" in v for v in results["violations"]))
        self.assertTrue(any("Formatting violation" in v for v in results["violations"]))

if __name__ == "__main__":
    unittest.main()
