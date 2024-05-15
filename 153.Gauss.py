#サブルーチン
def Gauss(A,y):
    #未知数の個数
    N = len(y)
    #未知数のベ(クトル
    x = [0]*N

    #前進消去
    for k in range(N-1):
        #最大値
        m = 0
        for i in range(k,N):
            if m < abs(A[i][k]):
                m = abs(A[i][k])
                l = i
            if l != k:
                for n in range(k,N):
                    A[k][n],A[l][n] = A[l][n],A[k][n]
                y[k],y[l] = y[l],y[k]
        for i in range(k+1,N):
            alpha = A[i][i]/A[k][k]
            for j in range(k+1,N):
                A[i][j] -= alpha*A[k][j]
            y[i] -= alpha*y[k]
    #後退代入
    x[N-1] = y[N-1]/A[N-1][N-1]

    for i in range(N-2,-1,-1):
        s = 0
        for k in range(i+1,N):
            s += A[i][k]*x[k]
        x[i] = (y[i] - s)/A[i][i]
    return x

#設定
A = [[1,-1,2],[-1,2,-3],[3,1,1]]
y = [5,-6,8]

x = Gauss(A,y)

#結果の表示
for n in x:
    print(f"{n:.2f}", end = "")