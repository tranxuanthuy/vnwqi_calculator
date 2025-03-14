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

def wqi(wqi_i_sis, wqi_ii_sis, wqi_iii_sis, wqi_iv_sis, wqi_v_sis, temperature, weighted = False):
    '''Third fomula
    input:
        wqi_i_sis: dictionary (wqi_i values)
        wqi_ii_sis: dictionary (wqi_ii values)
        wqi_iii_sis: dictionary (wqi_iii values)
        wqi_iv_sis: dictionary (wqi_iv values)
        wqi_v_sis: dictionary (wqi_v values)
    output:
        follow the 3, 4, 5 fomula
    '''


    non_empty_groups = 0
    for group_dict in [wqi_i_sis, wqi_ii_sis, wqi_iii_sis, wqi_iv_sis, wqi_v_sis]:
        if group_dict and any(not pd.isna(value) for value in group_dict.values()):
            non_empty_groups += 1
    if non_empty_groups < 3:
        raise ValueError("Dữ liệu không đủ, cần ít nhất 3 nhóm có giá trị.")
    # Check ( Group IV must have at least 3 parameters)
    num_params_g_iv = 0
    for key, value in wqi_iv_sis.items():
        if key == 'do_value':
            if not pd.isna(temperature):
                num_params_g_iv += 1
                continue
            else:
                continue
        if not pd.isna(value):
            num_params_g_iv += 1
    if num_params_g_iv < 3:
        raise ValueError("Nhóm IV cần ít nhất 3 giá trị.")
    
    from units.wqi_group import wqi_i, wqi_ii, wqi_iii, wqi_iv, wqi_v
    wqi_i_value = wqi_i(wqi_i_sis)
    wqi_ii_value = wqi_ii(wqi_ii_sis)
    wqi_iii_value = wqi_iii(wqi_iii_sis)
    wqi_iv_value = wqi_iv(wqi_iv_sis, temperature)
    wqi_v_value = wqi_v(wqi_v_sis)
    
    if not weighted:
        if len(wqi_v_sis) == 0:
            # fomula 4
            wqi = wqi_i_value * wqi_ii_value * wqi_iii_value * wqi_iv_value
        else:
            # fomula 3
            wqi = wqi_i_value * wqi_ii_value * wqi_iii_value * (wqi_iv_value * wqi_v_value)**(1/2)
    elif weighted:
        if len(wqi_v_sis) == 0:
            raise ValueError("Không thể tính toán WQI có trọng số khi không có nhóm V.")
        else:
            # fomula 5
            wqi = wqi_i_value * wqi_ii_value * wqi_iii_value * ( (wqi_iv_value**2) * wqi_v_value)**(1/3)
    return wqi