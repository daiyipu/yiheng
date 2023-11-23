import time, threading

def loop():
    thread_name = threading.current_thread().name
    print('Thread %s is running...' % thread_name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %d' % (thread_name, n))
    print('Thread %s ends.' % thread_name)
    
thread_name = threading.current_thread().name
print('Thread %s is running...' % thread_name)
t = threading.Thread(target = loop, name = 'loopThread')
t.start()
t.join()
print('Thread %s ends.' % thread_name)