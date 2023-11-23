import requests
import threading

def get_stock(code):
    url = 'http://hq.sinajs.cn/list=' + code
    resp = requests.get(url).text
    print('%s\n' % resp)

codes = ['sz000878', 'sh600993', 'sz000002', 'sh600153', 'sz002230', 'sh600658']
threads = [threading.Thread(target = get_stock, args = (code, )) for code in codes]
for t in threads:
    t.start()
for t in threads:
    t.join()
