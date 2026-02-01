from .synthesis.templates import TemplateLibrary

class ConcurrencyIPCSynthesizer:
    """
    Section 6: Concurrency & IPC Synthesizer
    """
    def __init__(self):
        self.templates = TemplateLibrary()

    def select_concurrency_model(self, analysis_results):
        all_text = str(analysis_results).lower()
        model = {
            "threads": "None",
            "ipc": "None",
            "sync": "None",
            "templates": {}
        }

        if "thread" in all_text or "concurrent" in all_text:
            model["threads"] = "POSIX Threads"
            model["sync"] = "Mutex / Condition Variables"
            model["templates"]["THREAD_POOL"] = self.templates.get_template("THREAD_POOL")

        if "signal" in all_text:
            model["templates"]["SIGNAL_HANDLER"] = self.templates.get_template("SIGNAL_HANDLER")

        if "ipc" in all_text or "pipe" in all_text:
            model["ipc"] = "Named Pipes (FIFO)"

        # Section 6.2: Socket Programming
        if "socket" in all_text or "network" in all_text or "tcp" in all_text:
            model["ipc"] = "TCP Sockets"
            model["templates"]["TCP_SERVER"] = self.templates.get_template("TCP_SERVER")

        # Section 6.2: Shared Memory
        if "shared memory" in all_text or "shm" in all_text or "mmap" in all_text:
            model["ipc"] = "POSIX Shared Memory"
            model["templates"]["SHARED_MEMORY"] = self.templates.get_template("SHARED_MEMORY")

        return model

    def process(self, analysis_results):
        print("Concurrency & IPC Synthesizer: Generating thread and IPC logic...")
        model = self.select_concurrency_model(analysis_results)
        return model
