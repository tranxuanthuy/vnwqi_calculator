import pandas as pd
import numpy as np

# table ph
ph_table = {
    'bpi': [5.5, 6, 8.5, 9],
    'qi': [50, 100, 100, 50]
}

# Table group II: Aldrin, BHC, Dieldrin, DDTs, Heptachlor & Heptachlorepoxide
group2_threshold = {
        "Aldrin" : 0.1,
        "BHC": 0.02,
        "Dieldrin" : 0.1,
        "DDTs" : 1.0,
        "Heptachlor & Heptachlorepoxide" : 0.2
}

# Table 1 in vn-wqi calculation guide
data_table_1 = {
    "i": [1, 2, 3, 4, 5],
    "qi": [100, 75, 50, 25, 10],
    "BOD5": [4, 6, 15, 25, 50],
    "COD": [10, 15, 30, 50, 150],
    "TOC": [4, 6, 15, 25, 50],
    "N_NH4": [0.3, 0.3, 0.6, 0.9, 5],
    "N_NO3": [2, 5, 10, 15, 15],
    "N_NO2": [0.05, np.nan, np.nan, np.nan, 0.05],
    "P_PO4": [0.1, 0.2, 0.3, 0.5, 4],
    "Coliform": [2500, 5000, 7500, 10000, 10000],
    "E_coli": [20, 50, 100, 200, 200]
}

table_1 = pd.DataFrame(data_table_1)

# Table 2 in vn-wqi calculation guide
data_table_2 = {
    "i": [1, 2, 3, 4, 5],
    "qi": [100, 75, 50, 25, 10],
    "As": [0.01, 0.02, 0.05, 0.1, 0.1],
    "Cd": [0.005, 0.005, 0.008, 0.01, 0.1],
    "Pb": [0.02, 0.02, 0.04, 0.05, 0.5],
    "Cr6+": [0.01, 0.02, 0.04, 0.05, 0.1],
    "Cu": [0.1, 0.2, 0.5, 1.0, 2.0],
    "Zn": [0.5, 1.0, 1.5, 2.0, 3.0],
    "Hg": [0.001, 0.001, 0.0015, 0.002, 0.01]
}

table_2 = pd.DataFrame(data_table_2)

