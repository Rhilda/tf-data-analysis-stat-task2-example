import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 71
    alpha = 1 - p
    n = len(x)
    return (-min(-x) - 1/2)*2/time**2, (-np.log(alpha)/n - min(-x) - 1/2)*2/time**2
