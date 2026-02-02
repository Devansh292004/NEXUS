import argparse
import sys
from nexus.orchestrator import NexusOrchestrator

def main():
    parser = argparse.ArgumentParser(description="NEXUS: Universal Systems Programming Assignment Solver")
    parser.add_argument("--spec", type=str, help="Textual specification of the assignment")
    parser.add_argument("--file", type=str, help="Path to a file containing the specification")
    parser.add_argument("--iterations", type=int, default=3, help="Maximum synthesis refinement iterations")

    args = parser.parse_args()

    specification = ""
    if args.file:
        try:
            with open(args.file, 'r') as f:
                specification = f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    elif args.spec:
        specification = args.spec
    else:
        # Default sample specification
        specification = """
        Assignment: Implement a thread-safe object pool.
        REQ: Must use Mutex for synchronization.
        REQ: Must handle up to 1024 small objects.
        REQ: Must be performance-optimized for frequent allocation.
        """
        print("No specification provided. Running with default sample...")

    orchestrator = NexusOrchestrator()
    try:
        result = orchestrator.run_pipeline(specification, max_iterations=args.iterations)

        print("\n" + "="*50)
        print("NEXUS OUTPUT SUMMARY")
        print("="*50)
        print(f"Certification: {result['certification']}")
        print(f"Status: {result['status']}")
        print(f"Generated Files: main.c, Makefile")
        print("="*50)

    except Exception as e:
        print(f"Framework Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
