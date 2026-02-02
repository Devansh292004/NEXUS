from .synthesis.templates import TemplateLibrary

class TradeoffAnalyzer:
    """
    Section 5.1: Structure Selection AI
    Performance Profiling and Trade-off Analysis.
    Provides explainable reasoning for design decisions.
    """
    def analyze_tradeoffs(self, analysis_results):
        print("Tradeoff Analyzer: Balancing time/space complexity...")
        constraints = analysis_results.get("constraints", [])
        reasoning = []

        if any("concurrent" in c.lower() for c in constraints):
            reasoning.append("Selected Lock-free Queue to balance high concurrency with low synchronization overhead.")

        if any("fast" in c.lower() or "performance" in c.lower() for c in constraints):
            reasoning.append("Selected Arena Allocator to achieve O(1) allocation time at the cost of heap fragmentation.")

        if not reasoning:
            reasoning.append("Defaulting to standard POSIX structures for general applicability.")

        return reasoning

class AdvancedDataStructureSynthesis:
    """
    Section 5: Advanced Data Structure Synthesis
    """
    def __init__(self):
        self.templates = TemplateLibrary()
        self.tradeoff_analyzer = TradeoffAnalyzer()

    def select_structures(self, analysis_results):
        selected = []
        constraints = analysis_results.get("constraints", [])

        # Simple selection logic
        is_concurrent = any("concurrent" in c.lower() or "thread" in c.lower() for c in constraints)
        is_high_performance = any("fast" in c.lower() or "performance" in c.lower() for c in constraints)

        if is_concurrent:
            print("Concurrent requirement detected. Adding Lock-free Queue.")
            selected.append(("LOCK_FREE_QUEUE", self.templates.get_template("LOCK_FREE_QUEUE")))

        if is_high_performance:
            print("High performance requirement detected. Adding Arena Allocator.")
            selected.append(("ARENA_ALLOCATOR", self.templates.get_template("ARENA_ALLOCATOR")))

        return selected

    def process(self, analysis_results):
        print("Advanced Data Structure Synthesis: Selecting optimal structures...")
        selected_structures = self.select_structures(analysis_results)
        reasoning = self.tradeoff_analyzer.analyze_tradeoffs(analysis_results)

        return {
            "selected_structures": [name for name, _ in selected_structures],
            "templates": {name: content for name, content in selected_structures},
            "design_reasoning": reasoning
        }
