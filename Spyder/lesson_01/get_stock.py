import requests
import threading

def display_info(code):
    url = 'http://hq.sinajs.cn/list=' + code
    response = requests.get(url).text
    print(response)
    
def single_thread(codes):
    for code in codes:
        code = code.strip()
        display_info(code)

def multi_thread(tasks):
    # 用列表推导生成线程，注意codes后面的‘，’!
    threads = [threading.Thread(target = single_thread, args = (codes,)) for codes in tasks]
    # 启动线程
    for t in threads:
        t.start()
    # 等待线程结束
    for t in threads:
        t.join()

# 注意main函数的形式
if __name__ == '__main__':
    codes = ['sh600001', 'sh600002', 'sh600003', 'sh600004', 'sh600005', 'sh600006']
    # 计算每个线程要做多少工作
    thread_len = int(len(codes) / 4)
    t1 = codes[0: thread_len]
    t2 = codes[thread_len: thread_len * 2]
    t3 = codes[thread_len * 2: thread_len * 3]
    t4 = codes[thread_len * 3:]

    # 多线程启动
    multi_thread([t1, t2, t3, t4])
        
