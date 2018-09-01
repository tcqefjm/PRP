from Crypto.Util import number
from pymongo import MongoClient
from configparser import ConfigParser

def CalculateAssociation(username):
    cf=ConfigParser()
    cf.read('config.ini')
    db=MongoClient(cf.get(username,'MONGO_ADDRESS'))[cf.get(username,'DATABASE_NAME')]
    sp=db.security_parameter.find_one()
    a,p,s=int(sp['a']),int(sp['p']),int(sp['s'])
    result={}
    for ar in cf.get(username,'ASSOCIATION_RULE').split():
        itemset=ar.split('->')
        k1,k2=itemset[0].count(',')+1,itemset[1].count(',')+1
        r=db.mining_result.find_one({'rule':ar})
        support_xy,support_x,N=int(r['xy']),int(r['x']),int(r['N'])
        SC_xy=number.inverse(s**(k1+k2),p)*support_xy%p//a**(k1+k2)
        SC_x=number.inverse(s**k1,p)*support_x%p//a**k1
        result[ar]={'Support':SC_xy/N,'Confidence':SC_xy/SC_x if SC_x else 0}
    return result

result=CalculateAssociation('user0')
print(result)
