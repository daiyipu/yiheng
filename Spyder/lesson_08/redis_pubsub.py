import redis

class Task:
    def __init__(self):
        self.rcon = redis.Redis(host = 'localhost', db = 5)
        self.ps = self.rcon.pubsub()
        self.ps.subscribe('task:pubsub:channel')

    def process_task(self):
        for i in self.ps.listen():
            if i['type'] == 'message':
                print('Task: ', i['data'])

Task().process_task()

