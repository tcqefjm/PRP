from Crypto.Util import number

class Transaction(object):
    def __init__(self,item_set,item_num=1000):
        self.item=[1 if str(i) in item_set else 0 for i in range(item_num)]
    def encrypt(self,s,a,p):
        encrypted_transaction=[]
        for i in self.item:
            r=number.getRandomNBitInteger(100)
            encrypted_transaction.append(s*(a+r)%p if i else s*r%p)
        return encrypted_transaction

s=101010001010100101001011                
def test():
    with open('prime.dat','r') as g:
        a,p=int(g.readline()),int(g.readline())
    with open('retail.dat','r') as f:
        for times in range(10):
            item_list=f.readline().split()
            test=Transaction(item_list)
            print(test.encrypt(s,a,p))

test()
