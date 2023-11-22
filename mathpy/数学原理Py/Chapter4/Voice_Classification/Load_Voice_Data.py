#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 20:26
# @Author  : DaiPuWei
# E-Mail   : 771830171@qq.com
# blog     : https://blog.csdn.net/qq_30091945
# @Site    : 中国民航大学北教25实验室506
# @File    : Load_Voice_Data.py
# @Software: PyCharm

import numpy as np

def Load_Voice_Data(path):
    """
    这是导入数据的函数
    :param path: 数据文件的路径
    :return: 数据集
    """
    data = []
    label = []
    with open(path) as f:
        for line in f.readlines():
            str = line.strip().split("\t")
            tmp = []
            for i in range(1,len(str)):
                tmp.append(float(str[i]))
            data.append(tmp)
            if 1 == int(str[0]):
                label.append([1,0,0,0])
            elif 2 == int(str[0]):
                label.append([0,1,0,0])
            elif 3 == int(str[0]):
                label.append([0,0,1,0])
            else:
                label.append([0,0,0,1])
    data = np.array(data)
    label = np.array(label)
    return data,label