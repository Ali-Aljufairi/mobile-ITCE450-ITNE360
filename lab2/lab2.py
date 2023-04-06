import numpy as np
import matplotlib.pyplot as plt


d = np.arange(1, 1000, 1)
f = [900, 1800]
Gt = 28
hm = 1


def free_space_path_loss(d, f, Gt):
    """
    ###d - distance in m
    ###f - frequency in MHz
    ###Gt - transmit antenna gain in dBi"""
    path_loss = 32.45 + 20 * np.log10(d) + 20 * np.log10(f) - Gt
    return path_loss


def CCIR_path_loss(d, f, b, hb, hm):
    """
    ###d - distance in m
    ###f - frequency in MHz
    ###b - correction factor for the environment
    ###hb - height of base station in m
    ###hm - height of mobile station in m
    """
    a = (1.1 * np.log10(f) - 0.7) * hm - (1.56 * np.log10(f) - 0.8)
    path_loss = 69.55 + 26.16 * \
        np.log10(f) - 13.82 * np.log10(hb) - a + \
        (44.9 - 6.55 * np.log10(hb)) * np.log10(d) - b
    return path_loss


def Hata_Model_urban(f, h, a, d, C=0):
    """
    ###f - frequency in MHz
    ###h - height of base station in m
    ###a - correction factor for the environment
    ###d - distance in
    ###C - correction factor for the environment"""
    if f > 1500:
        path_loss = 69.55+26.16 * \
            np.log10(f)-13.82*np.log10(h)-a+(44.9-6.55*np.log10(h))*np.log10(d)
    else:
        path_loss = 46.3+33.9 * \
            np.log10(f)-13.82*np.log10(h)-a + \
            (44.9-6.55*np.log10(h))*np.log10(d)+C
    return path_loss


def Hata_Model_medium_city_correction_factor(f, hre):
    """f - frequency in MHz
    hre - effective height of the base station in m"""
    Hata_Model_medium_city_correction_factor = (
        1.1*np.log10(f)-0.7)*hre-(1.56*np.log10(f)-0.8)
    return Hata_Model_medium_city_correction_factor


def Hata_Model_large_city_corection_factor(f, hre):
    """ ###f - frequency in MHz
    ####hre - effective height of the base station in m"""
    if f <= 300:
        correction_factor = 8.29*np.power((np.log10(1.54*hre)), 2)-1.1
    else:
        correction_factor = 3.2*np.power(np.log10(11.75*hre), 2)-4.97
    return correction_factor


def Hata_Model_suburban(f, h, a, d, C=0):
    """
    ###f - frequency in MHz
    ###h - height of base station in m
    ###a - correction factor for the environment
    ###d - distance in m"""
    path_loss = Hata_Model_urban(f, h, a, d, C)-2 * \
        np.power((np.log10(f/28)), 2) - 5.4
    return path_loss


def Hata_Model_rural(f, h, a, d, C=0):
    """
    ###f - frequency in MHz
    ###h - height of base station in m
    ###a - correction factor for the environment
    ###d - distance in m"""

    path_loss = Hata_Model_urban(
        f, h, a, d)-4.78*np.power(np.log10(f), 2)+18.33*np.log10(f)-40.98
    return path_loss


def plot_default(title, x_label='Distance (m)', y_label='Path loss (dB)'):
    plt.legend()
    plt.xlabel(f'{x_label}')  # Add a label for the x-axis
    plt.ylabel(f'{y_label}')
    plt.title(f'{title}')
    plt.grid(True)


CCIR_path_loss_1 = CCIR_path_loss(d, f[0], 0.25, 35, 1)
CCIR_path_loss_2 = CCIR_path_loss(d, f[1], 0.25, 35, 1)
path_loss = free_space_path_loss(d, f[0], Gt)
path_loss_2 = free_space_path_loss(d, f[1], Gt)


fig1 = plt.figure(1)
plt.plot(d, path_loss, label='900 MHz')
plot_default("free_space_path_loss")


fig2 = plt.figure(2)
plt.plot(d, path_loss_2, 'r', label='1800 MHz')
plot_default("free_space_path_loss")


fig3 = plt.figure(3)
plt.plot(d, path_loss, label='900 MHz')
plt.plot(d, path_loss_2, 'r', label='1800 MHz')
plot_default("free_space_path_loss")


fig4 = plt.figure(4)
plt.plot(d, CCIR_path_loss_2, 'r', label='1800 MHz')
plot_default("CCIR_path_loss")


fig5 = plt.figure(5)
plt.plot(d, CCIR_path_loss_1, label='900 MHz')
plt.plot(d, CCIR_path_loss_2, 'r', label='1800 MHz')
plot_default("CCIR_path_loss")


fig6 = plt.figure(6)
plt.plot(d, Hata_Model_urban(
    f[0], 35, Hata_Model_medium_city_correction_factor(900, hm), d), label='900 MHz')
plt.plot(d, Hata_Model_urban(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d), 'r', label='1800 MHz')
plot_default("Hata Model urban medium city")


fig7 = plt.figure(7)
plt.plot(d, Hata_Model_urban(
    f[0], 35, Hata_Model_large_city_corection_factor(900, d), d), label='900 MHz')
plt.plot(d, Hata_Model_urban(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, d), d, 3), 'r', label='1800 MHz')
plot_default("Hata Model urban Metroploitan city")


fig8 = plt.figure(8)
plt.plot(d, Hata_Model_suburban(
    f[0], 35, Hata_Model_medium_city_correction_factor(900, hm), d), label='900 MHz')
plt.plot(d, Hata_Model_suburban(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d), 'r', label='1800 MHz')
plot_default("Hata Model suburban medium city")


fig9 = plt.figure(9)
plt.plot(d, Hata_Model_suburban(
    f[0], 35, Hata_Model_large_city_corection_factor(900, hm), d), label='900 MHz')
plt.plot(d, Hata_Model_suburban(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, hm), d), 'r', label='1800 MHz')
plot_default("Hata Model suburban Metroplotian city")


fig10 = plt.figure(10)
plt.plot(d, Hata_Model_rural(
    f[0], 35, Hata_Model_medium_city_correction_factor(900, hm), d), label='900 MHz')
plt.plot(d, Hata_Model_rural(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d), 'r', label='1800 MHz')
plot_default("Hata Model rural medium city")


fig11 = plt.figure(11)
plt.plot(d, Hata_Model_rural(
    f[0], 35, Hata_Model_large_city_corection_factor(900, hm), d), label='900 MHz')
plt.plot(d, Hata_Model_rural(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, hm), d, 3),  label='1800 MHz')
plot_default("Hata Model rural Metroplotian city")

fig12 = plt.figure(12)
# plot all hata models for urban, suburban and rural and compare them with both frequencies
plt.plot(d, Hata_Model_urban(f[0], 35, Hata_Model_medium_city_correction_factor(
    900, hm), d), label='urban 900 MHz')
plt.plot(d, Hata_Model_urban(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d),  label='urban 1800 MHz')
plt.plot(d, Hata_Model_suburban(f[0], 35, Hata_Model_medium_city_correction_factor(
    900, hm), d), label='suburban 900 MHz')
plt.plot(d, Hata_Model_suburban(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d),  label='suburban 1800 MHz')
plt.plot(d, Hata_Model_rural(f[0], 35, Hata_Model_medium_city_correction_factor(
    900, hm), d), label='rural 900 MHz')
plt.plot(d, Hata_Model_rural(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d),  label='rural 1800 MHz')
# do large city correction for 1800 MHz
plt.plot(d, Hata_Model_urban(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, d), d, 3),  label='urban 1800 MHz large city')
plt.plot(d, Hata_Model_suburban(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, hm), d),  label='suburban 1800 MHz large city')
plt.plot(d, Hata_Model_rural(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, hm), d, 3),  label='rural 1800 MHz large city')
# do large city correction for 900 MHz
plt.plot(d, Hata_Model_urban(f[0], 35, Hata_Model_large_city_corection_factor(
    900, d), d),  label='urban 900 MHz large city')
plt.plot(d, Hata_Model_suburban(f[0], 35, Hata_Model_large_city_corection_factor(
    900, hm), d),  label='suburban 900 MHz large city')
plt.plot(d, Hata_Model_rural(f[0], 35, Hata_Model_large_city_corection_factor(
    900, hm), d),  label='rural 900 MHz large city')


plot_default(
    "All Hata Models COMPARISON (urban, suburban, rural) for 900 and 1800 MHz")

fig12 = plt.figure(13)
plt.plot(d, Hata_Model_urban(f[0], 35, Hata_Model_medium_city_correction_factor(
    900, hm), d), label='urban 900 MHz')
plt.plot(d, Hata_Model_urban(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d),  label='urban 1800 MHz')
plt.plot(d, Hata_Model_suburban(f[0], 35, Hata_Model_medium_city_correction_factor(
    900, hm), d), label='suburban 900 MHz')
plt.plot(d, Hata_Model_suburban(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d),  label='suburban 1800 MHz')
plt.plot(d, Hata_Model_rural(f[0], 35, Hata_Model_medium_city_correction_factor(
    900, hm), d), label='rural 900 MHz')
plt.plot(d, Hata_Model_rural(f[1], 35, Hata_Model_medium_city_correction_factor(
    1800, hm), d),  label='rural 1800 MHz')
# do large city correction for 1800 MHz
plt.plot(d, Hata_Model_urban(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, d), d, 3),  label='urban 1800 MHz large city')
plt.plot(d, Hata_Model_suburban(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, hm), d),  label='suburban 1800 MHz large city')
plt.plot(d, Hata_Model_rural(f[1], 35, Hata_Model_large_city_corection_factor(
    1800, hm), d, 3),  label='rural 1800 MHz large city')
# do large city correction for 900 MHz
plt.plot(d, Hata_Model_urban(f[0], 35, Hata_Model_large_city_corection_factor(
    900, d), d),  label='urban 900 MHz large city')
plt.plot(d, Hata_Model_suburban(f[0], 35, Hata_Model_large_city_corection_factor(
    900, hm), d),  label='suburban 900 MHz large city')
plt.plot(d, Hata_Model_rural(f[0], 35, Hata_Model_large_city_corection_factor(
    900, hm), d),  label='rural 900 MHz large city')
plt.plot(d, path_loss, label=' Free Space 900 MHz')
plt.plot(d, path_loss_2,  label=' Free Space 1800 MHz')
plt.plot(d, CCIR_path_loss_1, label='CCIR 900 MHz')
plt.plot(d, CCIR_path_loss_2, label='CCIR 1800 MHz')


plot_default(
    "All Models CICR Free space Hata COMPARISON (urban, suburban, rural) for 900 and 1800 MHz")

save_path = r'E:\OneDrive - University of Bahrain\Documents\UNI\ITCE450\Lab\lab2\figures'
for i in range(1, 14):
    fig = plt.figure(i)
    fig.savefig(save_path + r'\figure' + str(i) + '.png', dpi=300)

plt.show()
