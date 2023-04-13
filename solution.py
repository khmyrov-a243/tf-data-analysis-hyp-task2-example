import numpy as np
from scipy.stats import ttest_ind

chat_id = 973327975  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:  # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргумент
    # проверяем, что выборки не пустые
    if len(x) == 0 or len(y) == 0:
        return False

    # используем t-критерий Стьюдента для проверки гипотезы однородности выборок
    p_value = ttest_ind(x, y)[1]

    # если p-value меньше уровня значимости, то отклоняем гипотезу
    if p_value < 0.04:
        return True
    else:
        return False
