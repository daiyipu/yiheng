import redis

class Task:
    def __init__(self):
        self.rcon = redis.Redis(host = 'localhost', db = 5)
        self.queue = 'task:prodcons:queue'

    def process_task(self):
        while True:
            task = self.rcon.blpop(self.queue, 0)[1]
            print('Task: ', task)

Task().process_task()
