import matplotlib.pyplot as plt
import numpy as np 

def esPrimo(n):
    cnt=0
    if n<=1:
        return cnt
    m=2
    while(m*m<=n):
        cnt+=1
        if n%m==0:
            return cnt
        m+=1
    return cnt

cntprm=[itsPrime(x) for x in range(1,100001,1000)]

x=np.linspace(1,100000)
plt.plot(range(1,100001,1000),cntprm, label="Test de primalidad")
plt.plot(x,x**(0.5),label="Raíz de n",color="green")
plt.xlabel('Número')
plt.ylabel('Cantidad de operaciones')
plt.title('Test de primalidad')
plt.legend()
plt.savefig("test.png")
plt.show()
