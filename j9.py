# -*- coding: utf-8 -*-

import threading
import time


class Queue:

    def __init__(self):
        self._task = []
        self.running = False

    def enqueue(self, func, args=()):
        self._task.append((func, args))

    def _do(self):
        if self._task:
            func, args = self._task.pop(0)
            func(*args)
        else:
            time.sleep(0.1)

    def _worker(self):
        while self.running:
            self._do()

    def start(self):
        self.worker = threading.Thread(target=self._worker)
        self.running = True
        self.worker.setDaemon(True)
        self.worker.start()
