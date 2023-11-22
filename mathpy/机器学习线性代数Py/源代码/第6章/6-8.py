import numpy as np
from PIL import Image

def imgCompress(channel,percent):
    U, sigma, V_T = np.linalg.svd(channel)
    m = U.shape[0]
    n = V_T.shape[0]
    reChannel = np.zeros((m,n))

    for k in range(len(sigma)):
        reChannel = reChannel + sigma[k]* np.dot(U[:,k].reshape(m,1),V_T[k,:].reshape(1,n))
        if float(k)/len(sigma) > percent:
            reChannel[reChannel < 0] = 0
            reChannel[reChannel > 255] = 255
            break

    return np.rint(reChannel).astype("uint8")


oriImage = Image.open(r'test.png', 'r')
imgArray = np.array(oriImage)

R = imgArray[:, :, 0]
G = imgArray[:, :, 1]
B = imgArray[:, :, 2]
A = imgArray[:, :, 3]

for p in [0.001,0.005,0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
    reR = imgCompress(R, p)
    reG = imgCompress(G, p)
    reB = imgCompress(B, p)
    reA = imgCompress(A, p)
    reI = np.stack((reR, reG, reB, reA), 2)

    Image.fromarray(reI).save("{}".format(p)+"img.png")