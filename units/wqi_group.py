# Description: Calculate WQI for each group
import numpy as np
import pandas as pd
def wqi_i(wqi_i_sis):
    '''Calculate WQI for group I: ph
    input:
        ph: ph value
    output:
        WQI I
    '''
    if 'ph_value' in wqi_i_sis.keys() and not pd.isna(wqi_i_sis['ph_value']):
        ph_value = wqi_i_sis['ph_value']
    else:
        return 1.0
    
    from units.wqi_si import wqi_ph
    wqi_ph_value = wqi_ph(ph_value)
    wqi_i_value = wqi_ph_value*1.0
    return wqi_i_value

def wqi_ii(wqi_ii_sis):
    '''Calculate WQI for group II: aldrin, bhc, dieldrin,
    DDT, heptachlor_heptachlorepoxide
    input:
        aldrin_value: aldrin value
        bhc_value: bhc value
        dieldrin_value: dieldrin value
        ddt_value: DDT value
        heptachlor_heptachlorepoxide_value: heptachlor_heptachlorepoxide value
    output:
        WQI II
    '''
    from units.wqi_si import wqi_aldrin, wqi_bhc, wqi_dieldrin, wqi_ddt,\
      wqi_heptachlor_heptachlorepoxide
    wqi_group2_si = []
    if 'aldrin_value' in wqi_ii_sis.keys() and not pd.isna(wqi_ii_sis['aldrin_value']):
        aldrin_value = wqi_ii_sis['aldrin_value']
        wqi_aldrin_value = wqi_aldrin(aldrin_value)
        wqi_group2_si.append(wqi_aldrin_value)
    if 'bhc_value' in wqi_ii_sis.keys() and not pd.isna(wqi_ii_sis['bhc_value']):
        bhc_value = wqi_ii_sis['bhc_value']
        wqi_bhc_value = wqi_bhc(bhc_value)
        wqi_group2_si.append(wqi_bhc_value)
    if 'dieldrin_value' in wqi_ii_sis.keys() and not pd.isna(wqi_ii_sis['dieldrin_value']):
        dieldrin_value = wqi_ii_sis['dieldrin_value']
        wqi_dieldrin_value = wqi_dieldrin(dieldrin_value)
        wqi_group2_si.append(wqi_dieldrin_value)
    if 'ddt_value' in wqi_ii_sis.keys() and not pd.isna(wqi_ii_sis['ddt_value']):
        ddt_value = wqi_ii_sis['ddt_value']
        wqi_ddt_value = wqi_ddt(ddt_value)
        wqi_group2_si.append(wqi_ddt_value)
    if 'heptachlor_heptachlorepoxide_value' in wqi_ii_sis.keys() and not pd.isna(wqi_ii_sis['heptachlor_heptachlorepoxide_value']):
        heptachlor_heptachlorepoxide_value = wqi_ii_sis['heptachlor_heptachlorepoxide_value']
        wqi_heptachlor_heptachlorepoxide_value = \
            wqi_heptachlor_heptachlorepoxide(heptachlor_heptachlorepoxide_value)
        wqi_group2_si.append(wqi_heptachlor_heptachlorepoxide_value)
    if len(wqi_group2_si) == 0:
        return 1
    wqi_group2 = (np.prod(wqi_group2_si) ** (1/len(wqi_group2_si)))
    return wqi_group2

def wqi_iii(
        wqi_iii_sis):
    '''Calculate WQI for group III: as, cd, pb, cr6, cu, zn, hg
    input:
        as_value: as value
        cd_value: cd value
        pb_value: pb value
        cr6_value: cr6 value
        cu_value: cu value
        zn_value: zn value
        hg_value: hg value
    output:
        WQI III
    '''
    from units.wqi_si import wqi_as, wqi_cd, wqi_pb, wqi_cr6,\
      wqi_cu, wqi_zn, wqi_hg
    wqi_group3_si = []
    if 'as_value' in wqi_iii_sis.keys() and not pd.isna(wqi_iii_sis['as_value']):
        as_value = wqi_iii_sis['as_value']
        wqi_as_value = wqi_as(as_value)
        wqi_group3_si.append(wqi_as_value)
    if 'cd_value' in wqi_iii_sis.keys() and not pd.isna(wqi_iii_sis['cd_value']):
        cd_value = wqi_iii_sis['cd_value']
        qwi_cd_value = wqi_cd(cd_value)
        wqi_group3_si.append(qwi_cd_value)
    if 'pb_value' in wqi_iii_sis.keys() and not pd.isna(wqi_iii_sis['pb_value']):
        pb_value = wqi_iii_sis['pb_value']
        wqi_pb_value = wqi_pb(pb_value)
        wqi_group3_si.append(wqi_pb_value)
    if 'cr6_value' in wqi_iii_sis.keys() and not pd.isna(wqi_iii_sis['cr6_value']):
        cr6_value = wqi_iii_sis['cr6_value']
        wqi_cr6_value = wqi_cr6(cr6_value)
        wqi_group3_si.append(wqi_cr6_value)
    if 'cu_value' in wqi_iii_sis.keys() and not pd.isna(wqi_iii_sis['cu_value']):
        cu_value = wqi_iii_sis['cu_value']
        wqi_cu_value = wqi_cu(cu_value)
        wqi_group3_si.append(wqi_cu_value)
    if 'zn_value' in wqi_iii_sis.keys() and not pd.isna(wqi_iii_sis['zn_value']):
        zn_value = wqi_iii_sis['zn_value']
        wqi_zn_value = wqi_zn(zn_value)
        wqi_group3_si.append(wqi_zn_value)
    if 'hg_value' in wqi_iii_sis.keys() and not pd.isna(wqi_iii_sis['hg_value']):
        hg_value = wqi_iii_sis['hg_value']
        wqi_hg_value = wqi_hg(hg_value)
        wqi_group3_si.append(wqi_hg_value)
    if len(wqi_group3_si) == 0:
        return 1
    wqi_group3 = ((np.prod(wqi_group3_si) ** (1/len(wqi_group3_si))))
    return wqi_group3

def wqi_iv(
        wqi_iv_sis, temperature
):
    '''Calculate WQI for group IV: do, bod5, cod, toc, nnh4, nno3, nno2, ppo4
    input:
        do_value: do value
        bod5_value: bod5 value
        cod_value: cod value
        toc_value: toc value
        nnh4_value: nnh4 value
        nno3_value: nno3 value
        nno2_value: nno2 value
        ppo4_value: ppo4 value
    output:
        WQI IV
    '''
    from units.wqi_si import wqi_do, wqi_bod5, wqi_cod, wqi_toc, wqi_nnh4,\
      wqi_nno3, wqi_nno2, wqi_ppo4
    wqi_group4_si = []
    if 'do_value' in wqi_iv_sis.keys() and\
          not pd.isna(wqi_iv_sis['do_value']) and\
              not pd.isna(temperature):
        do_value = wqi_iv_sis['do_value']
        wqi_do_value = wqi_do(do_value, temperature)
        wqi_group4_si.append(wqi_do_value)
    if 'bod5_value' in wqi_iv_sis.keys() and\
          not pd.isna(wqi_iv_sis['bod5_value']):
        bod5_value = wqi_iv_sis['bod5_value']
        wqi_bod5_value = wqi_bod5(bod5_value)
        wqi_group4_si.append(wqi_bod5_value)
    if 'cod_value' in wqi_iv_sis.keys() and\
          not pd.isna(wqi_iv_sis['cod_value']):
        cod_value = wqi_iv_sis['cod_value']
        wqi_cod_value = wqi_cod(cod_value)
        wqi_group4_si.append(wqi_cod_value)
    if 'toc_value' in wqi_iv_sis.keys() and\
         not pd.isna(wqi_iv_sis['toc_value']):
        toc_value = wqi_iv_sis['toc_value']
        wqi_toc_value = wqi_toc(toc_value)
        wqi_group4_si.append(wqi_toc_value)
    if 'nnh4_value' in wqi_iv_sis.keys() and\
          not pd.isna(wqi_iv_sis['nnh4_value']):
        nnh4_value = wqi_iv_sis['nnh4_value']
        wqi_nnh4_value = wqi_nnh4(nnh4_value)
        wqi_group4_si.append(wqi_nnh4_value)
    if 'nno3_value' in wqi_iv_sis.keys() and\
          not pd.isna(wqi_iv_sis['nno3_value']):
        nno3_value = wqi_iv_sis['nno3_value']
        wqi_nno3_value = wqi_nno3(nno3_value)
        wqi_group4_si.append(wqi_nno3_value)
    if 'nno2_value' in wqi_iv_sis.keys() and\
          not pd.isna(wqi_iv_sis['nno2_value']):
        nno2_value = wqi_iv_sis['nno2_value']
        wqi_nno2_value = wqi_nno2(nno2_value)
        wqi_group4_si.append(wqi_nno2_value)
    if 'ppo4_value' in wqi_iv_sis.keys() and\
          not pd.isna(wqi_iv_sis['ppo4_value']):
        ppo4_value = wqi_iv_sis['ppo4_value']
        wqi_ppo4_value = wqi_ppo4(ppo4_value)
        wqi_group4_si.append(wqi_ppo4_value)
    if len(wqi_group4_si) == 0:
        return 1
    wqi_group4 = np.mean(wqi_group4_si)
    return wqi_group4

def wqi_v(
        wqi_v_sis
):
    '''calculate WQI for group V: coliform, ecoli
    input:
        coliform_value: coliform value
        ecoli_value: ecoli value
    output:
        WQI V
    '''
    from units.wqi_si import wqi_coliform, wqi_ecoli
    wqi_group5_si = []
    if 'coliform_value' in wqi_v_sis.keys() and not pd.isna(wqi_v_sis['coliform_value']):
        coliform_value = wqi_v_sis['coliform_value']
        wqi_coliform_value = wqi_coliform(coliform_value)
        wqi_group5_si.append(wqi_coliform_value)
    if 'ecoli_value' in wqi_v_sis.keys() and not pd.isna(wqi_v_sis['ecoli_value']):
        ecoli_value = wqi_v_sis['ecoli_value']
        wqi_ecoli_value = wqi_ecoli(ecoli_value)
        wqi_group5_si.append(wqi_ecoli_value)
    if len(wqi_group5_si) == 0:
        return 1
    wqi_group5 = np.mean(wqi_group5_si)
    return wqi_group5