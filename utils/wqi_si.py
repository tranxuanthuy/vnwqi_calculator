from utils.tables import ph_table
from utils.formula import first_fomula, second_fomula
'''GROUP I: pH'''
def wqi_ph(value):
    '''pH Water Quality Index
    input:
        value: pH value
    output:
        if pH < 5.5 or pH > 9, wqi_ph = 10
        if 6 <= pH <= 8.5, wqi_ph = 100
        if 5.5 < pH < 6 use second formula
        if 8.5 < pH < 9 use first formula
    '''

    bpi = ph_table['bpi']
    qi = ph_table['qi']
    if value < bpi[0] or value > bpi[3]:
        return 10
    elif value >= bpi[1] and value <= bpi[2]:
        return 100
    elif value > bpi[2] and value <= bpi[3]:
        return first_fomula(qi[2], qi[3], bpi[2], bpi[3], value)
    elif value >= bpi[0] and value < bpi[1]:
        return second_fomula(qi[0], qi[1], bpi[0], bpi[1], value)


'''GROUP II: (nhóm thông số thuốc bảo vệ thực vật)'''
from utils.tables import group2_threshold
def wqi_aldrin(value):
    '''Aldrin Water Quality Index
    input:
        value: Aldrin value (unit: ug/L)
        threshold: threshold value (unit: ug/L)
    output:
        if value <= threshold, wqi_aldrin = 100
        else, wqi_aldrin = 10
    '''
    if value <= group2_threshold['Aldrin']:
        return 100
    return 10

def wqi_bhc(value):
    '''BHC Water Quality Index 
    input:
        value: BHC value (unit: ug/L)
    output:
        if value <= threshold, wqi_BHC = 100
        else, wqi_BHC = 10
    '''
    if value <= group2_threshold['BHC']:
        return 100
    return 10

def wqi_dieldrin(value):
    '''Dieldrin Water Quality Index
    input:
        value: Dieldrin value (unit: ug/L)
        threshold: threshold value (unit: ug/L)
    output:
        if value <= thresold, wqi_dieldrin = 100
        else, wqi_dieldrin = 10
    '''
    if value <= group2_threshold['Dieldrin']:
        return 100
    return 10

def wqi_ddts(value):
    '''DDT Water Quality Index 
    input:
        value: DDT value (unit: ug/L)
    output:
        if value <= threshold, wqi_DDT = 100
        else, wqi_DDT = 10
    '''
    if value <= group2_threshold['DDTs']:
        return 100
    return 10

def wqi_heptachlor_heptachlorepoxide(value):
    '''Heptachlor & Heptachlorepoxide Water Quality Index 
    input:
        value: Heptachlor & Heptachlorepoxide value (unit: ug/L)
    output:
        if value <= threshold, wqi_heptachlor_heptachlorepoxide = 100
        else, wqi_heptachlor_heptachlorepoxide = 10
    '''
    if value <= group2_threshold['Heptachlor & Heptachlorepoxide']:
        return 100
    return 10

'''GROUP III: (nhóm thông số kim loại nặng): bao gồm các thông số As, Cd, 
Pb, Cr6+, Cu, Zn, Hg. '''

def wqi_as(value):
    '''As Water Quality Index
    input:
        value: As value (unit: mg/L)
    output:
        if value <= 0.01, wqi_as = 100
        else if value > 0.1, wqi_as = 10
        else follow the first fomula
    '''
    from utils.tables import as_table
    bpi = as_table['bpi']
    qi = as_table['qi']
    if value <= bpi[0]:
        return 100
    elif value > bpi[3]:
        return 10
    elif value > bpi[0] and value <= bpi[1]:
        return first_fomula(qi[0], qi[1], bpi[0], bpi[1], value)
    elif value > bpi[1] and value <= bpi[2]:
        return first_fomula(qi[1], qi[2], bpi[1], bpi[2], value)
    elif value > bpi[2] and value <= bpi[3]:
        return first_fomula(qi[2], qi[3], bpi[2], bpi[3], value)
