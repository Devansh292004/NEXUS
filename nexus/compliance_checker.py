import re

class ComplianceChecker:
    def check_forbidden_functions(self, code):
        """
        Uses static analysis (regex/AST) to detect forbidden C functions.
        """
        print("Compliance Checker: Scanning for forbidden functions...")
        forbidden = ["gets", "strcpy", "sprintf"]
        violations = []
        for func in forbidden:
            if re.search(rf"\b{func}\s*\(", code):
                violations.append(func)
        return violations

    def process(self, code_info):
        print("Starting Compliance Checking stage...")
        code = code_info.get("code", "")
        violations = self.check_forbidden_functions(code)

        if violations:
            return {"status": "FAILED", "violations": violations}
        return {"status": "PASSED", "style": "Verified"}
