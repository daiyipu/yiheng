from skfuzzy.cluster import cmeans
from pylab import*
from sklearn.datasets.samples_generator import make_blobs
centers = [(-20, -48), (0, 30), (15, -12), (-15, 20)]
data, cluster_location = make_blobs(n_samples=600, centers=centers, n_features=4, shuffle=True, cluster_std=[0.9, 0.7, 0.5, 0.1], random_state=14)
#参数设置c=4,聚类为4类
center, u, u0, d, jm, p, fpc = cmeans(data.T, m=2, c=4, error=0.0001, maxiter=1000)
for i in u:
    label = np.argmax(u, axis=0)  # 取得列的最大值
print('聚类为4类的center值：')
print(center)
print('聚类为4类的fpc值：',fpc)
#参数设置c=6,聚类为6类
center, u, u0, d, jm, p, fpc = cmeans(data.T, m=2, c=6, error=0.0001, maxiter=1000)
for i in u:
    label = np.argmax(u, axis=0)  # 取得列的最大值
print('--'*25)
print('聚类为6类的center值：')
print(center)
print('聚类为6类的fpc值：',fpc)