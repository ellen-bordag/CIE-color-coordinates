import numpy as np
import pandas as pd
import scipy

# Funktion zur Berechnung des Lichtspektrums basierend auf der gegebenen Formel
def light_spectrum(lambd):
    """
    intensity curve
    """
    i = 1.0
    return i * np.exp(-((lambd - 500) ** 2) / (20 ** 2))

# Funktion zur numerischen Integration
def integrate_spectrum(values, sensitivity):
    """
    numeric integration according to integration formula
    see https://en.wikipedia.org/wiki/CIE_1931_color_space
    """
    return scipy.integrate.simpson(values * sensitivity,x=lambd)


lambd = np.linspace(390, 830, 4400)
data = pd.read_csv('color_matching_functions.csv')

wavelengths = data.iloc[:, 0].values
sensitivity_x = data.iloc[:, 1].values
sensitivity_y = data.iloc[:, 2].values
sensitivity_z = data.iloc[:, 3].values

light_values = light_spectrum(lambd)

light_values = light_values[:len(sensitivity_x)]

#  XYZ color coordinates
X = integrate_spectrum(light_values, sensitivity_x)
Y = integrate_spectrum(light_values, sensitivity_y)
Z = integrate_spectrum(light_values, sensitivity_z)

# normalized xyz color coordinates
XYZ_sum = X + Y + Z
x = X / XYZ_sum
y = Y / XYZ_sum
z = Z / XYZ_sum

print("XYZ color coordinates:")
print("X:", X)
print("Y:", Y)
print("Z:", Z)

print("\nnormalized xyz color coordinates:")
print("x:", x)
print("y:", y)
print("z:", z)

