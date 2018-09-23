from Crypto.Util import number
from pymongo import MongoClient

def GenerateKey(db):
    security_parameter={'a':str(number.getPrime(600)),'p':str(number.getPrime(8192)),'s':str(number.getRandomNBitInteger(8190))}
    db.security_parameter.insert_one(security_parameter)

GenerateKey(MongoClient('mongodb://127.0.0.1:27017/').user)
