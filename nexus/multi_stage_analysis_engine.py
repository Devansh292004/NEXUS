import re
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

class SpecificationParser:
    def parse(self, specification):
        """
        Extracts requirements from assignment specifications.
        Supports text and PDF intelligence.
        """
        print("Parsing specification using Neural Engine...")

        # Section 1.1: PDF/Document Intelligence
        if isinstance(specification, str) and (specification.endswith('.pdf') or os.path.exists(specification)):
            if specification.endswith('.pdf') and fitz:
                print(f"Extracting text from PDF: {specification}")
                try:
                    doc = fitz.open(specification)
                    text = ""
                    for page in doc:
                        text += page.get_text()
                    specification = text
                except Exception as e:
                    print(f"PDF Error: {e}")
            elif os.path.exists(specification) and not specification.endswith('.pdf'):
                # Read as text file
                with open(specification, 'r') as f:
                    specification = f.read()

        requirements = re.findall(r'REQ: (.*?)(?=REQ:|$)', specification, re.DOTALL)
        return [req.strip() for req in requirements]

class RequirementDecomposer:
    """
    Section 1.1: Requirement Decomposition
    Breaks down complex specs into atomic requirements (REQ).
    """
    def decompose(self, requirements):
        print("Decomposing requirements into atomic units...")
        atomic_reqs = []
        for req in requirements:
            # Split by conjunctions or periods to find atomic units
            units = re.split(r' and |\. ', req)
            atomic_reqs.extend([u.strip() for u in units if u.strip()])
        return atomic_reqs

class TestCaseInferrer:
    """
    Section 1.1: Test Case Inference
    Generates property-based test specifications from natural language descriptions.
    """
    def infer_test_specs(self, atomic_reqs):
        print("Inferring test specifications from requirements...")
        test_specs = []
        for req in atomic_reqs:
            if "fast" in req.lower() or "performance" in req.lower():
                test_specs.append(f"Property: Execution time < threshold for {req}")
            if "memory" in req.lower():
                test_specs.append(f"Property: Memory usage < limit for {req}")
            if "concurrent" in req.lower() or "thread" in req.lower():
                test_specs.append(f"Property: Thread safety and linearizability for {req}")
        return test_specs

class SemanticAnalyzer:
    def analyze(self, requirements):
        """
        Breaks down requirements into atomic REQs, ASMs, and dependencies.
        """
        print("Analyzing requirements semantics...")
        analysis = {
            "req": [],
            "asm": [],
            "dep": [],
            "constraints": []
        }
        for req in requirements:
            lower_req = req.lower()
            if "assume" in lower_req:
                analysis["asm"].append(req)
            elif "depends on" in lower_req:
                analysis["dep"].append(req)
            else:
                analysis["req"].append(req)

            # Constraint extraction
            constraint_keywords = ["memory", "performance", "limit", "restriction", "fast", "concurrent", "thread"]
            if any(word in lower_req for word in constraint_keywords):
                analysis["constraints"].append(req)
        return analysis

class MultiStageAnalysisEngine:
    def __init__(self):
        self.parser = SpecificationParser()
        self.analyzer = SemanticAnalyzer()
        self.decomposer = RequirementDecomposer()
        self.test_inferrer = TestCaseInferrer()

    def process(self, specification):
        print("Starting Multi-Stage Analysis...")
        requirements = self.parser.parse(specification)
        analysis_results = self.analyzer.analyze(requirements)

        # Section 1.1 Enhancements
        atomic_reqs = self.decomposer.decompose(analysis_results["req"])
        test_specs = self.test_inferrer.infer_test_specs(atomic_reqs)

        analysis_results["atomic_reqs"] = atomic_reqs
        analysis_results["test_specs"] = test_specs

        return analysis_results
