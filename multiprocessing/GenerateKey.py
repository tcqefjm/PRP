from Crypto.Util import number
from pymongo import MongoClient

def GenerateKey(db):
    security_parameter={'a':str(number.getPrime(100)),'p':str(number.getPrime(1024)),'s':str(number.getRandomNBitInteger(1020))}
    db.security_parameter.insert_one(security_parameter)

GenerateKey(MongoClient('mongodb://127.0.0.1:27017/').user)
