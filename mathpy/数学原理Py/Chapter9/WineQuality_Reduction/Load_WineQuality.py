#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 12:14
# @Author  : DaiPuWei
# E-Mail   : 771830171@qq.com
# blog     : https://blog.csdn.net/qq_30091945
# @Site    : 中国民航大学北教25-506实验室
# @File    : Load_WineQuality.py
# @Software: PyCharm

import numpy as np
import pandas as pd

def Load_WineQuality(path,one_hot = False):
    """
    这是导入数据的函数
    :param path: 数据文件的路径
    :param one_hot: one-hot编码标志，默认为False
    :return: 数据集
    """
    WineQuality = pd.read_csv(path)
    Data = []
    Label = []
    for str in WineQuality.values:
        str = str[0].split(";")
        tmp = []
        for i in range(0,len(str)-1):
            tmp.append(float(str[i]))
        Data.append(tmp)
        Label.append(int(str[-1]))
    if one_hot == True:
        for (index,label) in enumerate(Label):
            _label = [0]*10
            _label[label] = 1
            Label[index] = _label
    Data = np.array(Data)
    Label = np.array(Label)
    return Data,Label