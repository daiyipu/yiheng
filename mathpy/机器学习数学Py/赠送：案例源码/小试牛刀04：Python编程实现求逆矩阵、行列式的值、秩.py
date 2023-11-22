# Python编程实现求逆矩阵、求行列式、求模

# https://blog.csdn.net/manjhOK/article/details/80014833
import numpy as np
# a=np.array([[1,4,7],[2,5,8],[3,6,9]])
# a=np.array([[1,2,3],[4,5,6]])
A=np.array([[1,4,9],[2,5,8],[3,6,9]])
print("A矩阵为：")
print(A)
print('*'*40)
F = np.linalg.inv(A)
print("A矩阵的逆矩阵为：")
print(F)
print('*'*40)
print("A矩阵与其逆矩阵乘积为：")
print(np.dot(A,np.linalg.inv(A)))
print(np.dot(A,np.linalg.inv(A)).astype(int))
print('*'*40)
print("A矩阵的行列式的值为：")
print(np.linalg.det(A))
print('*'*40)
print("A矩阵的秩为：")
print(np.linalg.matrix_rank(A))




