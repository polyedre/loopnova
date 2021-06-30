import threading, queue

class Controller:

    def __init__(self) -> None:
        self.queue = queue.Queue()
        self.analyzer_map = {}

    def run(self):
        threading.Thread(target=self.process_queue, daemon=True).start()
        self.queue.join()

    def run_async(self):
        threading.Thread(target=self.process_queue, daemon=True).start()

    def process_queue(self):
        while True:
            type, target = self.queue.get()
            if type in self.analyzer_map:
                for analyze_function in self.analyzer_map[type]:
                    analyze_function(target, self)
            else:
                print(f"Type {type} has no analyzers")
            self.queue.task_done()

    def add_target(self, type, value):
        self.queue.put((type, value))
        return self

    def load_analyzer(self, analyzer, type):
        if type in self.analyzer_map:
            self.analyzer_map[type].append(analyzer)
        else:
            self.analyzer_map[type] = [analyzer]
        return self