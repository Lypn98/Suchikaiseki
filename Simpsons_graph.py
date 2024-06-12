import numpy as np
import pandas as pd

def simpsons_rule(f, a, b, p):
    epsilon = 10**(-p)
    N = 2
    h = (b - a) / 2
    T = (h/2) * (f(a)+2*f((a+b)/2)+f(b))
    S = (h/3) * (f(a)+4*f((a+b)/2)+f(b))
    true_value = np.exp(b) - np.exp(a) if f == np.exp else np.sin(b) - np.sin(a)
    error = abs(S - true_value)
    results = [(N, S, error)]
    
    N_values = [1,2,4,8,16,32,64,128,256,512,1024] 
    
    while N < 1024:
        N *= 2
        h /= 2
        s = sum(f(a + i * h) for i in range(1, N, 2))
        new_T = T / 2 + h * s
        new_S = (4 * new_T - T) / 3
        true_value = np.exp(b) - np.exp(a) if f == np.exp else np.sin(b) - np.sin(a)
        error = abs(new_S - true_value)
        if N in N_values:
            results.append((N, new_S,error))
        
        if abs(new_S - S) < epsilon * abs(new_S):
            break
        T = new_T
        S = new_S
    
    # 1,2,4...,1024のときだけテーブルに表示
    if N == 1024 and abs(new_S - S) >= epsilon * abs(new_S):
        while N in N_values:
            results.append((N, new_S,error))
            N *= 2
            h /= 2
            s = sum(f(a + i * h) for i in range(1, N, 2))
            new_T = T / 2 + h * s
            new_S = (4 * new_T - T) / 3
            true_value = np.exp(b) - np.exp(a) if f == np.exp else np.sin(b) - np.sin(a)
            error = abs(new_S - true_value)

            if abs(new_S - S) < epsilon * abs(new_S):
                break
            T = new_T
            S = new_S
    
    return results

# 関数の定義
f_exp = np.exp
f_cos = np.cos

# 桁数の定義
p = 15 

# テーブルの作成
table_4_1_a = simpsons_rule(f_exp, 0, 1, p)
table_4_1_b = simpsons_rule(f_cos, 0, 2, p)

# DataFrame内の浮動小数点数の表示桁数を増やす
pd.set_option('display.float_format', '{:.16f}'.format)
df_4_1_a = pd.DataFrame(table_4_1_a, columns=["N", "S", "Error"])
df_4_1_b = pd.DataFrame(table_4_1_b, columns=["N", "S", "Error"])

# テーブルの表示
print("Table 4-1(a): シンプソン則 for ∫exp(x)dx [0,1]")
print(df_4_1_a.to_string(index=False))

print("\nTable 4-1(b): シンプソン則 for ∫cos(x)dx [0,2]")
print(df_4_1_b.to_string(index=False))