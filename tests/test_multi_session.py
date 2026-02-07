import unittest
import os
import shutil
from nexus.orchestrator import NexusOrchestrator

class TestMultiSession(unittest.TestCase):
    def test_isolated_sessions(self):
        orchestrator = NexusOrchestrator()

        path1 = "test_session_1"
        path2 = "test_session_2"

        os.makedirs(path1, exist_ok=True)
        os.makedirs(path2, exist_ok=True)

        try:
            orchestrator.run_pipeline("REQ: session 1", base_path=path1)
            orchestrator.run_pipeline("REQ: session 2", base_path=path2)

            self.assertTrue(os.path.exists(os.path.join(path1, "main.c")))
            self.assertTrue(os.path.exists(os.path.join(path2, "main.c")))

            with open(os.path.join(path1, "main.c"), 'r') as f:
                content1 = f.read()
            with open(os.path.join(path2, "main.c"), 'r') as f:
                content2 = f.read()

            # Both should exist independently
            self.assertIsNotNone(content1)
            self.assertIsNotNone(content2)

        finally:
            if os.path.exists(path1): shutil.rmtree(path1)
            if os.path.exists(path2): shutil.rmtree(path2)

if __name__ == "__main__":
    unittest.main()
