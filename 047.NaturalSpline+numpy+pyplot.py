#####学籍番号:1223033155
#####情報コース3年水越優友
#####スプライン補間によるプログラム

import numpy as np
import matplotlib.pyplot as plt

# natural spline
def NaturalSpline(px,py,ndiv):
    N = len(px)-1
    h = np.diff(px)
    v = np.zeros(N)
    for j in range(1,N):
        v[j] = 6*((py[j+1]-py[j])/h[j]
                  -(py[j]-py[j-1])/h[j-1])
        
        #連立方程式の作成
        A = np.zeros((N-1,N-1))

        for i in range(N-1):
            A[i,i] = 2*(h[i]+h[i+1])
        
        for i in range(N-2):
            A[i,i+1] = h[i+1]
            A[i+1,i] = h[i]
        
        y = v[1:N]
        x = np.linalg.solve(A,y)

        u = np.concatenate(([0],x,[0]))

        b = np.zeros(N)
        for j in range(N):
            b[j] = u[j]/2
        a = np.zeros(N)
        for j in range(N):
            du = u[j+1] - u[j]
            dx = h[j]
            a[j] = du/(6*dx)
        d = py.copy()

        c = np.zeros(N)
        for j in range(N):
            dy = py[j+1] - py[j]
            dx = h[j]
            c[j] = dy/dx-dx*(2*u[j]+u[j+1])/6

        #スプライン曲線のプロット
            for j in range(N):
                qx = np.linspace(px[j],px[j+1],ndiv+1)
                qy = a[j]*(qx-px[j])**3 + b[j]*(qx-px[j])**2 + c[j]*(qx-px[j]) + d[j]
                plt.plot(qx,qy)

        #与えられた点のプロット
            plt.scatter(px,py,s=30,c='red')
        plt.show()

### 元の関数 y = 1 / (1 + 25x^2)
def function(x):
    return 1 / (1 + 25 * x**2)

###実行
xs = -1.0; xe = 1.0
N = 10
px = np.linspace(xs,xe,N+1)
py = function(px)

NaturalSpline(px,py,ndiv=10)

            
        
