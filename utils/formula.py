# This file contains the fomula to calculate the WQI SI value
import pandas as pd
import numpy as np
def first_fomula(qi, qi_add_1, bpi, bpi_add_1, cp):
    '''First fomula
    input:
        qi: qi value (Giá trị WQI ở mức i đã cho trong
            bảng tương ứng với giá trị BPi)
        qi_add_1: qi+1 value (Giá trị WQI ở mức i+1 cho
              trong bảng tương ứng với giá trị BPi+1 )
        bpi: bpi value (Nồng độ giới hạn dưới của giá 
            trị thông số quan trắc)
        bpi_add_1: bpi+1 value (Nồng độ giới hạn trên 
        của giá trị thông số quan trắc)
        cp: Cp value (Giá trị của thông số quan trắc 
        được đưa vào tính toán. )
    output:
        follow the first fomula
    '''
    wqisi = (qi - qi_add_1) * (bpi_add_1 - cp) \
            / (bpi_add_1 - bpi) \
            + qi_add_1
    return wqisi

def second_fomula(qi, qi_add_1, bpi, bpi_add_1, cp):
    '''Second fomula
    input:
        qi: qi value (Giá trị WQI ở mức i đã cho trong
            bảng tương ứng với giá trị BPi)
        qi_add_1: qi+1 value (Giá trị WQI ở mức i+1 cho
              trong bảng tương ứng với giá trị BPi+1 )
        bpi: bpi value (Nồng độ giới hạn dưới của giá 
            trị thông số quan trắc)
        bpi_add_1: bpi+1 value (Nồng độ giới hạn trên 
        của giá trị thông số quan trắc)
        cp: Cp value (Giá trị của thông số quan trắc 
        được đưa vào tính toán. )'
    output:
        follow the second fomula
    '''
    wqisi = (qi_add_1 - qi) * (cp - bpi) \
            / (bpi_add_1 - bpi) \
            + qi
    return wqisi