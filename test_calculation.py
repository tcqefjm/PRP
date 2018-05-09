from Crypto.Util import number

def test_calculation(k1,k2):
    with open('calculation.dat','r') as f:
        SC_xy,SC_x,N=int(f.readline()),int(f.readline()),int(f.readline())
    with open('Security_Parameter.dat','r') as g:
        s,a,p=int(g.readline()),int(g.readline()),int(g.readline())
        
    SC_xy=number.inverse(s**(k1+k2),p)*SC_xy%p//a**(k1+k2)
    SC_x=number.inverse(s**k1,p)*SC_x%p//a**k1
    #print(SC_xy,SC_x)
    return SC_xy/N,SC_xy/SC_x

Ix,Iy=[0,1,2],[3]
Sup,Conf=test_calculation(len(Ix),len(Iy))
print(Sup,Conf)
