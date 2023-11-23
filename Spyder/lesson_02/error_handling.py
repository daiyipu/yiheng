# 错误处理

import logging

'''
作业：自己实现将不同的等级的信息写到不同的日志文件
logging.info(...)
logging.debug(...)
'''

try:
    r = 10 / 0
except ZeroDivisionError as e:
    print(type(e))
    print(e)
finally:
    # 主要防止资源泄露！
    print('Always come here.')
