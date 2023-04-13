import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 973327975 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # применяем тест Колмогорова-Смирнова к выборкам x и y
    test_result = ks_2samp(x, y)

    # сравниваем p-value с уровнем значимости
    return test_result.pvalue < 0.04
