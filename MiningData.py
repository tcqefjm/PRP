from pymongo import MongoClient
from multiprocessing import Pool
from functools import reduce
from configparser import ConfigParser

def CalculateRule(association_rule):
    db=MongoClient(mongo_address)[database_name]
    itemset=association_rule.split('->')
    Ix,Iy=itemset[0].split(','),itemset[1].split(',')
    support_x,support_xy=0,0
    for t in db.encrypted.find():
        sub_support_x=reduce(lambda x,y:x*y,map(lambda item:int(t[item]),Ix))
        sub_support_xy=sub_support_x*reduce(lambda x,y:x*y,map(lambda item:int(t[item]),Iy))
        support_x+=sub_support_x
        support_xy+=sub_support_xy
    db.mining_result.insert_one({'rule':association_rule,'xy':str(support_xy),'x':str(support_x),'N':str(db.encrypted.count_documents({}))})
        
def MiningData(username):
    global mongo_address,database_name
    cf=ConfigParser()
    cf.read('config.ini')
    mongo_address,database_name=cf.get(username,'MONGO_ADDRESS'),cf.get(username,'DATABASE_NAME')
    pool=Pool()
    pool.map(CalculateRule,cf.get(username,'ASSOCIATION_RULE').split())
    pool.close()

MiningData('user0')
