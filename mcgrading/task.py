from .errors import *

class Task():
    def __init__(self, function, args=(), timeout=600):
        self.function = function
        self.args = args
        self.timeout = timeout

    def run(self):
        thread = Process(target=self.function, args=self.args)
        thread.start()
        thread.join(self.timeout)
        if thread.is_alive():
            thread.terminate()
            thread.join()
            raise TimeoOutError('Killed after %d seconds'%self.timeout)
