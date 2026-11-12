import time
from typing import Callable, Iterable

process_delay = 0.5

class TickProcessor:
    def __init__(self):
        self._process_queue: list[Callable] = []
        self.last_call = time.time() - process_delay

    def append_process(self, process: Callable):
        self._process_queue.append(process)

    def append_processes(self, processes: Iterable[Callable]):
        self._process_queue.extend(processes)

    def process_next(self):
        if len(self._process_queue) > 0 and self.last_call + process_delay <= time.time():
            self._process_queue.pop(0)()
            self.last_call += process_delay
        elif len(self._process_queue) == 0:
            global active_processor
            active_processor = None
            del self

active_processor: TickProcessor | None = None

def new_processor():
    global active_processor
    active_processor = TickProcessor()
    return active_processor

def process_next_if_available():
    global active_processor
    if active_processor:
        active_processor.process_next()
        return True
    return False