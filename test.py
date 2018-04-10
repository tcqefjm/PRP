from Crypto.Util import number
from pymongo import MongoClient

class Transaction(object):
    def __init__(self,item_set,item_num=1000):
        self.item=[1 if str(i) in item_set else 0 for i in range(item_num)]
    def encrypt(self,s,a,p):
        encrypted_transaction={}
        for i,value in enumerate(self.item):
            r=number.getRandomNBitInteger(100)
            encrypted_transaction['item'+str(i)]=str(s*(a+r)%p if value else s*r%p)
        return encrypted_transaction

def test():
    with open('Security_Parameter.dat','r') as g:
        s,a,p=int(g.readline()),int(g.readline()),int(g.readline())
    client=MongoClient('mongodb://172.17.0.2:27017/')#更改为自己mongodb的IP
    db=client.testdata
    
    with open('retail.dat','r') as f:
        tmp=[]
        for times in range(8):
            item_list=f.readline().split()
            test=Transaction(item_list)
            tmp.append(test.encrypt(s,a,p))
        #print(tmp)
        db.encrypted.insert_many(tmp)

test()
