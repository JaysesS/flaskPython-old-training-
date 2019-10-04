import os
import threading
import glob
from queue import Queue
import hashlib
from time import sleep
import random

class Process():

    def __init__(self):
        self.queue = Queue()
        self.paths = self.getPathToFiles()

    def getPathToFiles(self):
        return glob.glob("documents/*")

    def start(self):
        threads = []
        for i in range(len(self.paths)):
            t = threading.Thread(target = self.hashsumFile, args = [self.paths[i],])
            threads.append(t)

        [t.start() for t in threads]
        [t.join() for t in threads]

 
    def hashsumFile(self, path):

        sleep(random.randint(0,5))

        hasher = hashlib.md5()
        with open(path, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        
        res = []
        res.append(path)
        res.append(hasher.hexdigest())
        self.queue.put(res)
