import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import gamma
from scipy.stats import expon


chat_id = 422119389 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = [ -x for x in x]
    alpha = 1 - p
    return (expon.ppf(alpha / 2, len(x)) - min(x) - 1/2) / (65**2 / 2), \
           (expon.ppf(1 - alpha / 2, len(x)) - min(x) - 1/2) /(65**2 / 2)
