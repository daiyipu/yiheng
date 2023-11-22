#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 20:00
# @Author  : DaiPuWei
# E-Mail   : 771830171@qq.com
# blog     : https://blog.csdn.net/qq_30091945
# @Site    : 中国民航大学北教25实验室506
# @File    : Other.py
# @Software: PyCharm

import pandas as pd
import numpy as np

def Merge(data,row,col):
    """
    这是生成DataFrame数据的函数
    :param data: 数据，格式为列表(list),不是numpy.array
    :param row: 行名称
    :param col: 列名称
    """
    data = np.array(data).T
    return pd.DataFrame(data=data,columns=col,index=row)

def Transform(Label):
    """
    这是将one-hot编码标签转化为数值标签的函数
    :param Label: one-hot标签
    """
    _Label = []
    for label in Label:
        _Label.append(np.argmax(label))
    return np.array(_Label)