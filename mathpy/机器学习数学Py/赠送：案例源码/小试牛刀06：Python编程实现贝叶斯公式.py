#coding:utf-8
def bayesF(pIsRoom1, pRoom1, pRoom2):
    return (pIsRoom1 * pRoom1)/((pIsRoom1 * pRoom1) + (1 - pIsRoom1) * pRoom2)
def sexProblem():
    pIsRoom1 = 0.5
    for i in range(1, 7):
        pIsRoom1 = bayesF(pIsRoom1, 0.6, 0.3)
        print ("只走出 %d 个男生，该房间为A教室的先验概率: %f" % (i, pIsRoom1))
    for i in range(1, 6):
        pIsRoom1 = bayesF(pIsRoom1, 0.4, 0.7)
        print ("先走出6个男生，再走出 %d 个女生，此为A教室的先验概率: %f" % (i, pIsRoom1))
sexProblem()


