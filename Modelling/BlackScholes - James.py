# James Fleming
# Black Scholes Model

import numpy as np
import math
from math import sqrt, exp, log

def black_scholes(v, r, p, T):
    eps = np.random.normal(0, 1)
    mean = ((r - math.pow(v, 2)/2) * T)
    stand_dev = v * math.sqrt(T)
    to_return = p * exp(mean + (stand_dev * eps))
    return to_return

def main():
    volitility = float(input('Volitility: '))
    interest = float(input('Interest: '))
    initial = float(input('Initial price: '))
    time = float(input('Time: '))

    # model
    print(black_scholes(volitility, interest, initial, time))

main()
