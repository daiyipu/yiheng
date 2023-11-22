#-*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv("./1.csv")
# 分特征和目标
data = df.iloc[:, 2:]
target = df.iloc[:, 1]
# 划分训练和测试数据
x_train, x_test, y_train, y_test = train_test_split(data.values, target.values, test_size=0.15)
knn_clf=KNeighborsClassifier(n_neighbors=2)
knn_clf.fit(x_train,y_train)
scores=knn_clf.score(x_test,y_test)
y_pred_train = knn_clf.predict(x_train)
y_pred_test = knn_clf.predict(x_test)
print('训练集的预测效果:')
print('Precision: %.3f ' % precision_score(y_true=y_train, y_pred=y_pred_train),
      'Recall: %.3f ' % recall_score(y_true=y_train, y_pred=y_pred_train),
      'F1: %.3f ' % f1_score(y_true=y_train, y_pred=y_pred_train))
print('测试集的预测效果:')
print('Precision: %.3f ' % precision_score(y_true=y_test, y_pred=y_pred_test),
      'Recall: %.3f ' % recall_score(y_true=y_test, y_pred=y_pred_test),
      'F1: %.3f ' % f1_score(y_true=y_test, y_pred=y_pred_test))

