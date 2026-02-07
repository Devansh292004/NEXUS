import unittest
from nexus.course_roadmap import ROADMAP_CONTENT
from nexus.output_guarantees import OutputGuarantees

class TestRoadmap(unittest.TestCase):
    def test_roadmap_content_exists(self):
        self.assertIsNotNone(ROADMAP_CONTENT)
        self.assertIn("Course Roadmap: Systems Programming Masterclass", ROADMAP_CONTENT)
        self.assertIn("Week 1: The Machine Interface", ROADMAP_CONTENT)
        self.assertIn("Week 12: Performance Engineering", ROADMAP_CONTENT)

    def test_output_guarantees_includes_roadmap(self):
        og = OutputGuarantees()
        # Mocking input for process
        code_info = {"code": "int main() {}"}
        build_artifacts = {"makefile": "all: ..."}
        compliance_results = {"status": "PASSED"}

        results = og.process(code_info, build_artifacts, compliance_results)

        self.assertIn("course_roadmap", results["documentation"])
        self.assertEqual(results["documentation"]["course_roadmap"], ROADMAP_CONTENT)

if __name__ == "__main__":
    unittest.main()
