from pymongo import MongoClient

def test_mining(Ix,Iy):
    client=MongoClient('mongodb://172.17.0.3:27017/')
    encrypted=client.testdata.encrypted
    N=encrypted.count()
    transaction=encrypted.find()
    
    support_x,support_xy=0,0
    for i in range(N):
        sub_support_x=1
        for item in Ix:
            sub_support_x*=int(transaction[i]['item'+str(item)])
        sub_support_xy=sub_support_x
        for item in Iy:
            sub_support_xy*=int(transaction[i]['item'+str(item)])
        support_x+=sub_support_x
        support_xy+=sub_support_xy
    with open('calculation.dat','w') as f:
        f.write("%s\n%s\n%s" %(support_xy,support_x,N))

test_mining([0,1,2],[3])
