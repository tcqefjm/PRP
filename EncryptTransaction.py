from Crypto.Util import number
from Crypto.Random import atfork
from pymongo import MongoClient
from multiprocessing import Pool
from configparser import ConfigParser

class Transaction(object):
    def __init__(self,item_set,item_num=1000):
        self.item=[int(str(i) in item_set) for i in range(item_num)]
    def encrypt(self,a,p,s):
        return {str(i):str(s*(a*value+number.getRandomNBitInteger(300))%p) for i,value in enumerate(self.item)}
    
def init(username):
    cf=ConfigParser()
    cf.read('config.ini')
    m,db,ds=cf.get(username,'MONGO_ADDRESS'),cf.get(username,'DATABASE_NAME'),cf.get(username,'DATASET_NAME').split(',')
    sp=MongoClient(m)[db]['security_parameter'].find_one()
    return (m,db,ds,int(sp['a']),int(sp['p']),int(sp['s']))
    
def EncryptTransaction(line):
    atfork()
    item_list=line.split()
    transaction=Transaction(item_list)
    MongoClient(mongo_address)[database_name].encrypted.insert_one(transaction.encrypt(a,p,s))
    
def Encrypt(username):
    global mongo_address,database_name,a,p,s
    mongo_address,database_name,dataset,a,p,s=init(username)
    pool=Pool()
    for d in dataset:
        with open(d,'r') as f:
            pool.map(EncryptTransaction,f)
    pool.close()

Encrypt('user0')