import numpy as np
import pandas as pd

def daikei_rule(f, a, b, p):
    epsilon = 10**(-p)
    N = 1
    h = b - a
    T = (h / 2) * (f(a) + f(b))
    true_value = np.exp(1) - np.exp(0) if f == np.exp else np.sin(b) - np.sin(a)
    error = abs(T - true_value)
    results = [(N, T, error)]
    
     # N = 1, 2, 4, 8, ..., 1024
    N_values = [2**i for i in range(11)] 
    
    while N < 1024:
        N *= 2
        h /= 2
        s = sum(f(a + i * h) for i in range(1, N, 2))
        new_T = T / 2 + h * s
        true_value = np.exp(1) - np.exp(0) if f == np.exp else np.sin(b) - np.sin(a)
        error = abs(new_T - true_value)
        if N in N_values:
            results.append((N, new_T,error))
        
        if abs(new_T - T) < epsilon * abs(new_T):
            break
        T = new_T
    
    # 1,2,4...,1024のときだけテーブルに表示
    if N == 1024 and abs(new_T - T) >= epsilon * abs(new_T):
        while N in N_values:
            results.append((N, new_T,error))
            N *= 2
            h /= 2
            s = sum(f(a + i * h) for i in range(1, N, 2))
            new_T = T / 2 + h * s
            true_value = np.exp(1) - np.exp(0) if f == np.exp else np.sin(b) - np.sin(a)
            error = abs(new_T - true_value)

            if abs(new_T - T) < epsilon * abs(new_T):
                break
            T = new_T
    
    return results

# 関数の定義
f_exp = np.exp
f_cos = np.cos

# 桁数の定義
p = 8  

# テーブルの作成
table_4_1_a = daikei_rule(f_exp, 0, 1, p)
table_4_1_b = daikei_rule(f_cos, 0, 2, p)

# DataFrame内の浮動小数点数の表示桁数を増やす
pd.set_option('display.float_format', '{:.10f}'.format)
df_4_1_a = pd.DataFrame(table_4_1_a, columns=["N", "T", "Error"])
df_4_1_b = pd.DataFrame(table_4_1_b, columns=["N", "T", "Error"])

# テーブルの表示
print("Table 4-1(a): 台形則 for ∫exp(x)dx [0,1]")
print(df_4_1_a.to_string(index=False))

print("\nTable 4-1(b): 台形則 for ∫cos(x)dx [0,2]")
print(df_4_1_b.to_string(index=False))
