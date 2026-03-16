import math

def calculate_orbital_period(radius, mass):
    # Calculate the orbital period
    return 2 * math.pi * math.sqrt(radius**3 / mass)
