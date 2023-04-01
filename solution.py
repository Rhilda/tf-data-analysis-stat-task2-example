import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    for i in range(n):
        x[i] -= 0.038
    max_val = np.max(x)
    first, second = (1 - p) / 2, (1 + p) / 2
    return max_val / (second**(1/n)) + 0.038, max_val / (first**(1/n)) + 0.038
