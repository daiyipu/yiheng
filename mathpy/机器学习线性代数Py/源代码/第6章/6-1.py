import numpy as np

scoreData = np.mat([
[5,2,1,4,0,0,2,4,0,0,0],
[0,0,0,0,0,0,0,0,0,3,0],
[1,0,5,2,0,0,3,0,3,0,1],
[0,5,0,0,4,0,1,0,0,0,0],
[0,0,0,0,0,4,0,0,0,4,0],
[0,0,1,0,0,0,1,0,0,5,0],
[5,0,2,4,2,1,0,3,0,1,0],
[0,4,0,0,5,4,0,0,0,0,5],
[0,0,0,0,0,0,4,0,4,5,0],
[0,0,0,4,0,0,1,5,0,0,0],
[0,0,0,0,4,5,0,0,0,0,3],
[4,2,1,4,0,0,2,4,0,0,0],
[0,1,4,1,2,1,5,0,5,0,0],
[0,0,0,0,0,4,0,0,0,4,0],
[2,5,0,0,4,0,0,0,0,0,0],
[5,0,0,0,0,0,0,4,2,0,0],
[0,2,4,0,4,3,4,0,0,0,0],
[0,3,5,1,0,0,4,1,0,0,0]
])

def cosSim(vec_1, vec_2):
    dotProd = float(np.dot(vec_1.T, vec_2))
    normProd = np.linalg.norm(vec_1)*np.linalg.norm(vec_2)
    return 0.5+0.5*(dotProd/normProd)

def estScore(scoreData,scoreDataRC,userIndex,itemIndex):
    n = np.shape(scoreData)[1]
    simSum = 0
    simSumScore = 0
    for i in range(n):
        userScore = scoreData[userIndex,i]
        if userScore == 0 or i == itemIndex:
            continue
        sim = cosSim(scoreDataRC[:, i], scoreDataRC[:, itemIndex])
        simSum = float(simSum + sim)
        simSumScore = simSumScore + userScore * sim
    if simSum == 0:
        return 0
    return simSumScore / simSum

U, sigma, VT = np.linalg.svd(scoreData)

sigmaSum = 0
k_num = 0

for k in range(len(sigma)):
    sigmaSum = sigmaSum + sigma[k] * sigma[k]
    if float(sigmaSum)/float(np.sum(sigma ** 2)) > 0.9:
        k_num = k+1
        break

sigma_K = np.mat(np.eye(k_num)*sigma[:k_num])
scoreDataRC = sigma_K * U.T[:k_num, :] * scoreData

n = np.shape(scoreData)[1]
userIndex = 17

for i in range(n):
    userScore = scoreData[17, i]
    if userScore != 0:
        continue
    print("index:{},score:{}".format(i, estScore(scoreData, scoreDataRC, userIndex, i)))