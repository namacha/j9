# -*- coding: utf-8 -*-

import threading
import time


class Queue:

    JOB_ID = 0

    def __init__(self):
        self._task = []
        self.running = False
        self.result = {}

    def enqueue(self, func, args=()):
        self.JOB_ID += 1
        self._task.append((self.JOB_ID, func, args))
        return self.JOB_ID

    def _do(self):
        if self._task:
            job_id, func, args = self._task.pop(0)
            result = func(*args)
            self.result[job_id] = result
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
