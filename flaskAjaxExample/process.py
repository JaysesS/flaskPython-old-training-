import os
import threading
from queue import Queue
import hashlib
from time import sleep
import random
import string

class Process():

    def __init__(self):
        self.queue = Queue()
        self.count = 15

    def start(self):
        threads = []
        for i in range(self.count):
            t = threading.Thread(target = self.hashsum)
            threads.append(t)

        [t.start() for t in threads]

 
    def hashsum(self):

        sleep(random.randint(0,20))

        someword = self.randomWord()

        res = hashlib.md5(someword.encode('utf-8')).hexdigest()
        print(res)
        self.queue.put(res)

    def randomWord(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(8, 12)
        return ''.join(random.choice(chars) for x in range(size))
