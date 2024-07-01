import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_method(dt, T):
    # 初期条件
    t = 0
    y1 = 1
    y2 = 0
    t_values = [t]
    y1_values = [y1]
    y2_values = [y2]

    while t < T:
        k1_y1 = dt * y2
        k1_y2 = dt * (-16 * y1 - 10 * y2)

        k2_y1 = dt * (y2 + 0.5 * k1_y2)
        k2_y2 = dt * (-16 * (y1 + 0.5 * k1_y1) - 10 * (y2 + 0.5 * k1_y2))

        k3_y1 = dt * (y2 + 0.5 * k2_y2)
        k3_y2 = dt * (-16 * (y1 + 0.5 * k2_y1) - 10 * (y2 + 0.5 * k2_y2))

        k4_y1 = dt * (y2 + k3_y2)
        k4_y2 = dt * (-16 * (y1 + k3_y1) - 10 * (y2 + k3_y2))

        y1_new = y1 + (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1) / 6
        y2_new = y2 + (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2) / 6

        t += dt
        y1, y2 = y1_new, y2_new
        t_values.append(t)
        y1_values.append(y1)
        y2_values.append(y2)

    return t_values, y1_values

T = 2  # 最終時間

# 計算とプロット
for dt in [0.1, 0.2]:
    t_values, y1_values = runge_kutta_method(dt, T)
    plt.plot(t_values, y1_values, label=f'Runge-Kutta dt={dt}')

plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Runge-Kutta Method')
plt.grid(True)
plt.show()
