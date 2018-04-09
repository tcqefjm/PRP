from Crypto.Util import number

s=number.getRandomNBitInteger(4090)
a=number.getPrime(512)
p=number.getPrime(4096)
with open('Security_Parameter.dat','a') as f:
    f.write(str(s)+'\n')
    f.write(str(a)+'\n')
    f.write(str(p)+'\n')
print(s,a,p)