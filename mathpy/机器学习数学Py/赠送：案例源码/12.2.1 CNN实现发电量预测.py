import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from torch.autograd import  Variable
import math
import sklearn.metrics as skm
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
def sliding(data_in, sw_width=7, n_out=7):
    data = data_in.reshape((data_in.shape[0] * data_in.shape[1],data_in.shape[2]))  # 将以周为单位的样本展平为以天为单位的序列
    X, y = [], []
    for _ in range(len(data)):
        in_b =  sw_width
        out_b = in_b + n_out
        if out_b < len(data):
            data_in_seq = data[0:in_b, 0]
            data_in_seq = data_in_seq.reshape((len(data_in_seq), 1))
            X.append(data_in_seq)
            y.append(data[in_b:out_b, 0])
    X = np.array(X)
    y = np.array(y)
    X = torch.from_numpy(X).float()
    y = torch.from_numpy(y).float()
    return X, y
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv1d(
                in_channels=7,
                out_channels=32,
                kernel_size=3,
                stride=1,
                padding=2,
            ),
            nn.ReLU(),
            nn.Conv1d(
                in_channels=32,
                out_channels=32,
                kernel_size=3,
                stride=1,
                padding=2,
            ),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            nn.Conv1d(
                in_channels=32,
                out_channels=16,
                kernel_size=3,
                stride=1,
                padding=2,
            ),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
        )
        self.out = nn.Linear(32,10)
        self.out1 = nn.Linear(10,7)
    def forward(self, x):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.out(x))
        output = self.out1(x)
        return output, x
dataset = pd.read_csv('fadian_days.csv', header=0,
                          infer_datetime_format=True, engine='c',
                          parse_dates=['datetime'], index_col=['datetime'])
train, test = dataset.values[1:848], dataset.values[848:]
train = np.array(np.split(train, len(train) / 7))  # 将数据划分为按周为单位的数据
test = np.array(np.split(test, len(test) / 7))
slide = 7
input_sequence_start = 0
train_x, train_y = sliding(train, slide)
test_x, test_y = sliding(test, slide)
torch_dataset = Data.TensorDataset(train_x, train_y)
train_loader = Data.DataLoader(dataset=torch_dataset, batch_size=24, shuffle=True)
name = 'cnn'
EPOCH = 10000  # train the training data n times, to save time, we just train 1 epoch
BATCH_SIZE = 24
LR = 0.001  # learning rate
use_gpu = True
cnn = CNN()
if use_gpu:
    cnn =cnn.cuda()
loss_func  = torch.nn.SmoothL1Loss(reduce = True,size_average=True) # Defined loss function
optimizer = torch.optim.Adam(cnn.parameters(), lr=LR ) # Defined optimizer
optimizer.zero_grad()
for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(train_loader,BATCH_SIZE):  # gives batch data, normalize x when iterate train_loader
        b_x = Variable(b_x, requires_grad=True)
        b_y = Variable(b_y, requires_grad=False)
        if use_gpu:
            b_x = b_x.cuda()
            b_y = b_y.cuda()
        output = cnn(b_x)[0]  # cnn output
        # print(output)
        loss = loss_func(output, b_y)  # cross entropy loss
        print('epoch',epoch,loss)
        optimizer.zero_grad()  # clear gradients for this training step
        loss.backward()  # backpropagation, compute gradients
        optimizer.step()  # apply gradients
    if use_gpu:
        test_x = test_x.cuda()
    out = cnn(test_x)[0]
    out = out.data.cpu().numpy()
    scores = list()
    for i in range(test_y.shape[1]):
        mse = skm.mean_squared_error(test_y[:, i], out[:, i])
        rmse = math.sqrt(mse)
        scores.append(rmse)
    s = 0  # 计算总的 RMSE
    for row in range(test_y.shape[0]):
        for col in range(test_y.shape[1]):
            s += (test_y[row, col] - out[row, col]) ** 2
    score = math.sqrt(s / (test_y.shape[0] *test_y.shape[1]))
    s_scores = ', '.join(['%.1f' % s for s in scores])
    print('%s: score [%.3f] s_scores %s\n' % (name, score, s_scores))


