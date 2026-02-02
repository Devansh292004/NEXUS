import re
import os

class CodeStyleEnforcer:
    """
    Section 11.1: Code Style
    Enforces style guide (formatting, naming conventions, modularity).
    """
    def check_style(self, code):
        print("Code Style Enforcer: Validating formatting and naming conventions...")
        violations = []

        # Check for CamelCase in functions (assuming snake_case is required for C)
        if re.search(r'\b[A-Z][a-z]+[A-Z][a-z]+\s*\(', code):
            violations.append("Naming convention violation: Functions should use snake_case")

        # Check for TAB indentation (assuming spaces are required)
        if "\t" in code:
            violations.append("Formatting violation: Use spaces instead of TABS")

        # Modularity check (simulated)
        if len(code.split("\n")) > 500:
            violations.append("Modularity violation: File too long, consider decomposing")

        return violations

class ComplianceChecker:
    """
    Section 11.1: Restriction Enforcement
    Static analysis and repository cleanliness validation.
    """
    def __init__(self):
        self.style_enforcer = CodeStyleEnforcer()

    def check_forbidden_functions(self, code):
        """
        Uses static analysis (regex/AST) to detect forbidden C functions.
        """
        print("Compliance Checker: Scanning for forbidden functions...")
        # Expanded forbidden function list
        forbidden = ["gets", "strcpy", "sprintf", "system", "popen", "strcat", "scanf"]
        violations = []
        for func in forbidden:
            if re.search(rf"\b{func}\s*\(", code):
                violations.append(func)
        return violations

    def check_repository_cleanliness(self, repo_path="."):
        """
        Validates .gitignore and checks for binary files in repository.
        """
        print("Compliance Checker: Validating repository cleanliness...")
        violations = []

        # Check for .gitignore
        if not os.path.exists(os.path.join(repo_path, ".gitignore")):
            violations.append("Missing .gitignore file")

        # Check for binary files (simulated check for common binary extensions)
        binary_extensions = [".o", ".a", ".so", ".out", ".bin", ".exe"]
        for root, dirs, files in os.walk(repo_path):
            if ".git" in dirs:
                dirs.remove(".git")
            for file in files:
                if any(file.endswith(ext) for ext in binary_extensions):
                    violations.append(f"Binary file detected: {os.path.join(root, file)}")

        return violations

    def process(self, code_info):
        print("Starting Compliance Checking stage...")
        code = code_info.get("code", "")

        function_violations = self.check_forbidden_functions(code)
        repo_violations = self.check_repository_cleanliness()
        style_violations = self.style_enforcer.check_style(code)

        all_violations = function_violations + repo_violations + style_violations

        if all_violations:
            return {"status": "FAILED", "violations": all_violations}
        return {"status": "PASSED", "style": "Verified"}
