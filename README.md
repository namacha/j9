j9
============================
j9 (Job Queue) is a minimal job queue for python script.

## example
```python
import time


def task(n):
    time.sleep(n)
    print('Task Done. ({} seconds)'.format(n))


if __name__ == '__main__':
    from j9 import Queue
    
    q = Queue()
    q.start()
    
    q.enqueue(task, args=(2,))
    q.enqueue(task, args=(1,))
    q.enqueue(task, args=(3,))
    
    
    while True:
        time.sleep(1)   # Do Something
