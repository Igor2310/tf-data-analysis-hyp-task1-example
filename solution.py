import pandas as pd
import numpy as np

from statsmodels.stats.proportion import proportions_ztest


chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

sgn_lvl = 0.03

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    _,p_val = proportions_ztest([x_success,y_success],[x_cnt,y_cnt], alternative = 'smaller')
    if(p_val > sgn_lvl):
        return False
    return True 
