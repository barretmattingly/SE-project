#!/usr/bin/env python3

class CC:
    def __init__ (self, last4_=0, custId_=0, name_='', ccNum_=0, ccExp_='', ccv_=0):
        self.last4 = last4_
        self.custId = custId_
        self.name = name_
        self.ccNum = ccNum_
        self.ccExp = ccExp_
        self.ccv = ccv_

'''
def createCC(last4, custId, name, ccNum, ccExp, ccv):
    ccDic[key] = CC(last4, custId, name, ccNum, ccExp, ccv)

def updateCC(cc):
    ccDic[last4] = cc

def deleteCC(last4):
    del ccDic[last4]

def loadCC(self):
    filepath = 'data/CC.csv'
    file = open(filepath, 'r')
    for line in file.readlines():
        tmp = line.strip().split(',')
        createCC(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])
    file.close()

def saveCC(self):
    filepath = 'data/CC.csv'
    file = open(filepath, 'w')
    for keys in CCdic.keys():
        tmp = ','.join(CCdic[key])
        file.write(tmp)
    file.close()

def printCC(key):
    print('\t%d,%d,%s,%d,%s,%d' %(last4, custId, name, ccNum, ccExp, ccv) )
'''

