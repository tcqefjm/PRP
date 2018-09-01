from pymongo import MongoClient
from multiprocessing import Pool
from functools import reduce,partial
from configparser import ConfigParser

def CalculateRule(association_rule,cf):
    db=MongoClient(cf('MONGO_ADDRESS'))[cf('DATABASE_NAME')]
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
    cf=ConfigParser()
    cf.read('config.ini')
    pool=Pool()
    pool.map(partial(CalculateRule,cf=partial(cf.get,username)),cf.get(username,'ASSOCIATION_RULE').split())
    pool.close()    

MiningData('user0')
