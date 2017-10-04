import matplotlib.pyplot as plt

def itsPrime(x):
    cnt=0
    if x<=1:
        return cnt
    i=2
    while(i*i<=x):
        cnt+=1
        if x%i==0:
            return cnt
        i+=1
    return cnt

cntprm=[itsPrime(x) for x in range(1,100001,1000)]


plt.plot(range(1,100001,1000),cntprm)
plt.xlabel('Numero')
plt.ylabel('Cantidad de operaciones')
plt.title('Hola')
plt.savefig("test.png")
plt.show()
