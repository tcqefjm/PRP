from charm.toolbox.integergroup import IntegerGroup
groupForPS=IntegerGroup()
k1=500 #temporary for test
groupForPS.paramgen(k1)
p=groupForPS.p
s=groupForPS.q
groupForAlpha=IntegerGroup()
groupForRijk=IntegerGroup()
## to generate rijk
##generate 0/1 list
file = open ('retailForTest.dat','r')
L=20
listA=[]
for line in file:
    line=line.rstrip('\n')
    listA.append(line.split(' '))
lengthOfListA=len(listA)
list_1_0=[([0] * L) for i in range(lengthOfListA)]##create 2-dimension list
for colIndex in range(lengthOfListA):
    for rowIndex in listA[colIndex]:
        if rowIndex !='':
            rowIndex=int(rowIndex)
            list_1_0[colIndex][rowIndex]=1
file.close()
##encryption
list_eijk=[([0] * L) for i in range(lengthOfListA)]
for colIndex in range(lengthOfListA):
    for rowIndex in range(L):
        if list_1_0[colIndex][rowIndex]==1:
            groupForAlpha.paramgen(200)
            alpha=groupForAlpha.p
            groupForRijk.paramgen(2*200/20)
            rijk=groupForRijk.p
            list_eijk[colIndex][rowIndex]=(s%p)*((alpha%p)+(rijk%p))
        if list_1_0[colIndex][rowIndex]==0:
            groupForRijk.paramgen(2*200/20)
            rijk=groupForRijk.p
            list_eijk[colIndex][rowIndex]=(s%p)*(rijk%p)
for colIndex in range(lengthOfListA):
    for rowIndex in range(L):
        print list_eijk[colIndex][rowIndex]
