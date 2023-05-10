import numpy


def dBm_to_Watts(dBm):
    return 10 ** (dBm / 10) / 1000


def Watts_to_dBm(Watts):
    if Watts > 0:
        return 10 * numpy.log10(Watts) + 30
    elif Watts < 0:
        return 10 * numpy.log10(-Watts) + 30


def noise_power(noise_spectral_density, bandwidth):
    # Convert dBm/Hz to Watts/Hz
    noise_spectral_density = dBm_to_Watts(noise_spectral_density)

    # Calculate the noise power
    noise_power = noise_spectral_density * bandwidth

    # Convert Watts to dBm
    noise_power_dbm = Watts_to_dBm(noise_power)

    return noise_power_dbm


def calculate_received_power(Pt, f, d, Gt, Gr):
    # Convert Pt to Watts
    Pt_W = dBm_to_Watts(Pt)

    # Convert frequency to Hz
    f_Hz = f * numpy.power(10, 6)

    # Convert distance to meters
    d_m = d * numpy.power(10, 3)

    # Calculate the received power using the Friis transmission equation
    Pr_W = Pt_W + Gt + Gr - 32.45 - 20 * \
        numpy.log10(d_m) - 20 * numpy.log10(f_Hz)
    # Convert received power back to dBm
    pr = Watts_to_dBm(Pr_W)

    return pr


def calculate_noise_power(nf, kb, T, B):
    # Calculate the noise power
    N_W = kb*T*B*numpy.power(10, nf/10)

    # Convert noise power to dBm
    N = Watts_to_dBm(N_W)
    return N

# Pr dBm , N dBm


def calculate_SNR(Pr, N):
    SNR = Pr - N
    return SNR


# nf dB , kB Boltzmann constant  , T K , B hz
N = calculate_noise_power(5, 1.38e-23, 290, 10*numpy.power(10, 6))

# pt dBm , f MHz , d km , Gt dBi , Gr dBi
power_receive = calculate_received_power(39, 1800, 10, 28, 28)

# noise_spectral_density dBm/hz, bandwidth MHz
noise_power = noise_power(-174, 10.94 * numpy.power(10, 3))

print("Noise power:", noise_power, "dBm")

print("Received power:", power_receive, "dBm")

print("Noise power:", N, "dBm")

print("SNR:", calculate_SNR(power_receive, noise_power), "dB")
