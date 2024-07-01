import numpy as np
import matplotlib.pyplot as plt

def euler_method(dt, T):
    # 初期条件
    t = 0
    y1 = 1
    y2 = 0
    t_values = [t]
    y1_values = [y1]
    y2_values = [y2]

    while t < T:
        y1_new = y1 + dt * y2
        y2_new = y2 + dt * (-16 * y1 - 10 * y2)
        t += dt
        y1, y2 = y1_new, y2_new
        t_values.append(t)
        y1_values.append(y1)
        y2_values.append(y2)

    return t_values, y1_values

# 計算とプロット
T = 2  # 最終時間

for dt in [0.1, 0.2]:
    t_values, y1_values = euler_method(dt, T)
    plt.plot(t_values, y1_values, label=f'Euler dt={dt}')

plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Euler Method')
plt.grid(True)
plt.show()
