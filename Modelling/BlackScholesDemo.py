import math
from math import sqrt, exp, log
import numpy as np


def main():
    #Inputs
    volatility = float(input("Volatility of the stock: "))
    interest = float(input("Interest rate (risk-free) of the stock: "))
    initial_price = float(input("Initial price of the stock: "))
    time = float(input("The time till expiry (in days): "))

    while time != "X":
        print(black_scholes_formula(volatility, interest, initial_price, time))
        time = float(input("Enter another time. Enter X to exit: "))


def black_scholes_formula(v, i, p, t):
    epsilon = np.random.normal(0, 1)
    distribution_mean = ((i - math.pow(v, 2)/2) * t)
    distribution_sd = v * math.sqrt(t);
    return p * exp(distribution_mean + distribution_sd*epsilon)


main()
