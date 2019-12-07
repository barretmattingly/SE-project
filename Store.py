#!/usr/bin/env python3

import User
import Produce
import Cart

class Store:
    def __init__(self, curUser_, userDic_, produceDic_, cart_)
        self curUser = curUser_
        self userDic = userDic_
        self.produceDic = produceDic_
        self.cart = cart_

    '''
    PRODUCE METHODS
    '''
    def createProduce(id, name, price, qty):
        self.produceDic[id] = Produce(id, name, price, qty)

    def updateProduce(produce):
        self.produceDic[produce.id] = produce

    def deleteProduce(id):
        del self.produceDic[id]

    def loadProduce():
        filepath = 'data/Produce.csv'
        file = open(filepath, 'r')
        for line in file.readlines():
            tmp = line.strip().split(',')
            createProduce(tmp[0],tmp[1],tmp[2],tmp[3])
        file.close()

    def saveProduce():
        filepath = 'data/Produce.csv'
        file = open(filepath, 'w')
        for key in self.produceDic.keys():
            p = self.produceDic[key]
            tmp = p.id+','+p.name+','+p.price+','+p.qty
            file.write(tmp)
        file.close()

    '''
    USER METHODS
    '''
    def createUser(userId, username, password, userType, firstname, lastname, address, phoneNr, email, userCCDic):
        self.userDic[userId] = User(userId,
                username,
                password,
                userType,
                firstname,
                lastname,
                address,
                phoneNr,
                email,
                userCCDic)

    def updateUser(user):
        userDic[user.userId] = user

    def deleteUser(userId):
        del userDic[userId]

    '''
    return 0 - useromer information correct
    return 1 - incorrect password
    return 2 - incorrect username (useromer does not exist)
    '''
    def validateLogin(username, password):
        for key in useromerDic.keys():
            tmpuser = userDic[key]
            if tmpuser.username == username:
                if tmpuser.password == password:
                    return 0
                else:
                    return 1
        return 2

    def loadUsers():
        filepath = 'data/Users.csv'
        file = open(filepath, 'r')
        for line in file.readlines():
            temp = line.split(',')
            createUser(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8], dict())

    def saveUsers():
        filepath = 'data/Users.csv'
        file = open(filepath, 'w')
        for key in userDic.keys():
            u = userDic[key]
            tmp = u.userId+','+u.username+','+u.password+','+u.userType+','
            tmp += u.firstname+','+u.lastname+','+u.address+','+u.zipcode+','
            tmp += u.city+','+u.state+','+u.phoneNr+','+u.email
            file.write(tmp)
        file.close()

    def printUser(user):
        print('userId:', user.id)
        print('username:', user.username)
        print('password:', user.password)
        print('type:', user.userType)
        print('firstname:', user.firstname)
        print('lastname:', user.lastname)
        print('address:', user.address)
        print('phoneNr:', user.phoneNr)
        print('email:', user.email)
