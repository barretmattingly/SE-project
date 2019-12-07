#!/usr/bin/env python3

import CC

class User:
    def _init_ (self, userId_, username_, password_, userType_, firstname_='', lastnmae_='', address_='', zipcode_=0, city_='', state_='', phoneNr_='', email_='', userCCDic_={}):
        self.userId = userId_
        self.username = username_
        self.password = password_
        self.userType = userType
        self.firstname = firstname_
        self.lastname = lastnmae_
        self.address = address_
        self.zipcode = zipecode_
        self.city = city_
        self.state = state_
        self.phoneNr = phoneNr_
        self.email = email_
        self.userCCDic = userCCDic_

    def createCC(self, last4, custId, name, ccNum, ccExp, ccv):
        self.userCCDic[last4] = CC(last4, custId, name, ccNum, ccExp, ccv)

    def updateCC(self):
        self.userCCDic[last4] = cc

    def deleteCC(self, last4):
        del self.userCCDic[last4]

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
        for keys in self.CCdic.keys():
            cc = self.CCdic[key]
            tmp = cc.last4+','+cc.custId+','+cc.name+','
            tmp += cc.ccNum+','+cc.ccExp+','+cc.ccv
            file.write(tmp)
        file.close()

    self.loadCC()
