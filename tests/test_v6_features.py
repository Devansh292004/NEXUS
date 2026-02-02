import unittest
from nexus.concurrency_ipc_synthesizer import ConcurrencyIPCSynthesizer
from nexus.output_guarantees import OutputGuarantees
from nexus.compilation_build_system import CompilationBuildSystem

class TestV6Features(unittest.TestCase):
    def test_ipc_selection_socket_and_shm(self):
        synthesizer = ConcurrencyIPCSynthesizer()
        analysis = {"requirements": ["Must use TCP socket and shared memory"]}
        results = synthesizer.process(analysis)
        self.assertEqual(results["ipc"], "POSIX Shared Memory") # Last match wins in current simple logic
        self.assertIn("TCP_SERVER", results["templates"])
        self.assertIn("SHARED_MEMORY", results["templates"])

    def test_formal_proof_generation(self):
        guarantees = OutputGuarantees()
        results = guarantees.process({"code": "/* target */"}, {}, {"status": "PASSED"})
        self.assertIn("formal_proof", results["documentation"])
        self.assertIn("Theorem 1: Memory Safety", results["documentation"]["formal_proof"])

    def test_build_variants_makefile(self):
        build_system = CompilationBuildSystem()
        results = build_system.process({"code": "int main(){}"})
        makefile = results["makefile"]
        self.assertIn("DEBUG_FLAGS", makefile)
        self.assertIn("RELEASE_FLAGS", makefile)
        self.assertIn("TEST_FLAGS", makefile)
        self.assertIn("debug:", makefile)
        self.assertIn("release:", makefile)

if __name__ == "__main__":
    unittest.main()
