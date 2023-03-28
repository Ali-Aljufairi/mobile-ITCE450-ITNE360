import numpy as np
import matplotlib.pyplot as plt
def free_space_path_loss(d, f, Gt):
    # d - distance in m
    # f - frequency in MHz
    # return - path loss in dB
    path_loss = 32.45 + 20 * np.log10(d) + 20 * np.log10(f) - Gt
    return path_loss
def CCIR_path_loss(d, f, b, hb, hm):
    # d - distance in m
    # f - frequency in MHz
    # hb - height of base station in m
    # hm - height of mobile station in m
    # b - area covered by building in percentage
    # return - path loss in dB
    a = (1.1 * np.log10(f) - 0.7) * hm - (1.56 * np.log10(f) - 0.8)
    path_loss = 69.55 + 26.16 * np.log10(f) - 13.82 * np.log10(hb) - a + (44.9 - 6.55 * np.log10(hb)) * np.log10(d) - b
    return path_loss

d = np.arange(1, 1000, 1)
f = [900, 1800]
Gt =28
CCIR_path_loss_1=CCIR_path_loss(d,f[0],0.35,35,1)
CCIR_path_loss_2=CCIR_path_loss(d,f[1],0.35,35,1)
path_loss = free_space_path_loss(d, f[0], Gt)
path_loss_2 = free_space_path_loss(d, f[1], Gt)


fig1 =plt.figure(1)
plt.plot(d, path_loss, label='900 MHz')
plt.xlabel('Distance (m)')  # Add a label for the x-axis
plt.ylabel('Path loss (dB)')
plt.title('Free space path loss')

fig2 =plt.figure(2)
plt.plot(d, path_loss_2, 'r', label='1800 MHz')
plt.legend()
plt.xlabel('Distance (m)')  # Add a label for the x-axis
plt.ylabel('Path loss (dB)')
plt.title('Free space path loss')

fig3 =plt.figure(3)
plt.plot(d, path_loss, label='900 MHz')
plt.plot(d, path_loss_2, 'r', label='1800 MHz')
plt.legend()
plt.xlabel('Distance (m)')  # Add a label for the x-axis
plt.ylabel('Path loss (dB)')
plt.title('Free space path loss')
# 

fig4 =plt.figure(4)
plt.plot(d, CCIR_path_loss_2, 'r', label='1800 MHz')
plt.legend()
plt.xlabel('Distance (m)')  # Add a label for the x-axis
plt.ylabel('Path loss (dB)')
plt.title('CCIR path loss')

fig5 =plt.figure(5)
plt.plot(d, CCIR_path_loss_1, label='900 MHz')
plt.plot(d, CCIR_path_loss_2, 'r', label='1800 MHz')
plt.legend()
plt.xlabel('Distance (m)')  # Add a label for the x-axis
plt.ylabel('Path loss (dB)')
plt.title('CCIR path loss')


plt.show()
