#####学籍番号:1223033155
#####情報コース3年水越優友
#####SOR法のプログラム

import numpy as np

#経過表示
def Progress(k,x):
    print(k,end="")
    for val in x:
        print(f"{val:.8f}",end="")
    print('')

#SOR法
def SOR(A,b,omega,eps):
    N = len(b)
    x = np.zeros(N)
    k =0
    Progress(0,x)
         
    while True:
        error = 0
        sum = 0
        for i in range(N):
            total = np.dot(A[i],x)-A[i,i]*x[i]
            new_x = (b[i]-total)/A[i,i] + (1-omega)*x[i]
            sum += abs(new_x)
            error += abs(new_x-x[i])
            x[i] = new_x
        if error < eps*sum:
            break
        k = k+1
        Progress(k,x)
    return x
    
A = np.array([[5,4],[2,3]])
b = np.array([13,8])
eps = 1.0e-8
omega = 1.2

x = SOR(A,b,omega,eps)
print(x)

        