import re

class SpecificationParser:
    def parse(self, specification):
        """
        Extracts requirements from assignment specifications.
        Supports text and placeholder for PDF intelligence.
        """
        print("Parsing specification using Neural Engine...")
        # Placeholder for PDF OCR/Intelligence
        if specification.endswith('.pdf'):
            print("Extracting text from PDF...")
            specification = "EXTRACTED_TEXT_FROM_PDF"

        requirements = re.findall(r'REQ: (.*?)(?=REQ:|$)', specification, re.DOTALL)
        return [req.strip() for req in requirements]

class SemanticAnalyzer:
    def analyze(self, requirements):
        """
        Breaks down requirements into atomic REQs, ASMs, and dependencies.
        """
        print("Analyzing requirements semantics...")
        analysis = {
            "REQ": [],
            "ASM": [],
            "DEP": [],
            "CONSTRAINTS": []
        }
        for req in requirements:
            if "assume" in req.lower():
                analysis["ASM"].append(req)
            elif "depends on" in req.lower():
                analysis["DEP"].append(req)
            else:
                analysis["REQ"].append(req)

            # Constraint extraction
            if any(word in req.lower() for word in ["memory", "performance", "limit", "restriction"]):
                analysis["CONSTRAINTS"].append(req)
        return analysis

class MultiStageAnalysisEngine:
    def __init__(self):
        self.parser = SpecificationParser()
        self.analyzer = SemanticAnalyzer()

    def process(self, specification):
        print("Starting Multi-Stage Analysis...")
        requirements = self.parser.parse(specification)
        analysis_results = self.analyzer.analyze(requirements)
        return analysis_results
