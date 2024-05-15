#####学籍番号:1223033155
#####情報コース3年水越優友
#####ヤコビ法のプログラム
import numpy as np
def Progress(k,x):
    print(k,end="")
    for val in x:
        print(f"{val:.8f}",end="")
    print('')

#ヤコビ法
def Jacobi(A,b,eps):
    N = len(b)
    x = np.zeros(N)
    z = np.zeros(N)
    k=0
    Progress(0,x)

    while True:
        error = 0.0
        sum = 0.0
        for i in range(N):
            total = np.dot(A[i],x)-A[i,i]*x[i]
            z[i] = (b[i]-total)/A[i,i]
            sum += abs(z[i])
            error += abs(z[i]-x[i])

        if error < eps*sum:
            break

        x = np.copy(z)

        k=k+1
        Progress(k,x)

    return x
    
A = np.array([[5,4],[2,3]])
b = np.array([13,8])
eps = 1.0e-8
x = Jacobi(A,b,eps)
print(x)