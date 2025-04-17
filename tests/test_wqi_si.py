from utils.wqi_si import (
    wqi_ph,
    wqi_aldrin,
    wqi_bhc,
    wqi_dieldrin,
    wqi_ddts,
    wqi_heptachlor_heptachlorepoxide,
    wqi_as,
    wqi_cd,
    wqi_pb,
    wqi_cr6,
    wqi_cu,
    wqi_zn,
    wqi_hg,
    wqi_do,
    wqi_bod5,
    wqi_cod,
    wqi_toc,
    wqi_nnh4,
    wqi_nno3,
    wqi_nno2,
    wqi_ppo4,
    wqi_coliform,
    wqi_ecoli
)

def test_parameter(name, func, values):
    print(name + " " + "---" * 10)
    for value in values:
        print(f"{name} = {value} → WQI = {func(value)}")

if __name__ == "__main__":
    print("\n" + "="*30)
    print("🔹 Group I – pH")
    print("="*30)
    test_parameter("pH", wqi_ph, [5.0, 5.4, 5.5, 5.6, 5.9, 6.0, 7.0, 8.5, 8.6, 8.9, 9.0, 9.1])

    print("\n" + "="*30)
    print("🔹 Group II ")
    print("="*30)
    test_parameter("Aldrin", wqi_aldrin, [0.05, 0.1, 0.11])
    test_parameter("BHC", wqi_bhc, [0.01, 0.02, 0.03])
    test_parameter("Dieldrin", wqi_dieldrin, [0.05, 0.1, 0.15])
    test_parameter("DDTs", wqi_ddts, [0.5, 1.0, 1.5])
    test_parameter("Heptachlor", wqi_heptachlor_heptachlorepoxide, [0.1, 0.2, 0.3])

    print("\n" + "="*30)
    print("🔹 Group III ")
    print("="*30)
    test_parameter("As", wqi_as, [0.005, 0.01, 0.02, 0.05, 0.1, 0.11])
    test_parameter("Cd", wqi_cd, [0.002, 0.005, 0.008, 0.01, 0.1, 0.15])
    test_parameter("Pb", wqi_pb, [0.01, 0.02, 0.04, 0.05, 0.5, 0.6])
    test_parameter("Cr", wqi_cr6, [0.005, 0.01, 0.02, 0.04, 0.05, 0.1, 0.2])
    test_parameter("Cu", wqi_cu, [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 2.5])
    test_parameter("Zn", wqi_zn, [0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0])
    test_parameter("Hg", wqi_hg, [0.0005, 0.001, 0.0015, 0.002, 0.01, 0.02])

    print("\n" + "="*30)
    print("🔹 Group IV ")
    print("="*30)
    test_parameter("BOD5", wqi_bod5, [2, 4, 6, 15, 25, 50, 60])
    test_parameter("COD", wqi_cod, [5, 10, 15, 30, 50, 150, 160])
    test_parameter("TOC", wqi_toc, [2, 4, 6, 15, 25, 50, 60])
    test_parameter("NH4", wqi_nnh4, [0.1, 0.3, 0.6, 0.9, 5.0, 6.0])
    test_parameter("NO3", wqi_nno3, [1, 2, 5, 10, 15, 16])
    test_parameter("NO2", wqi_nno2, [0.01, 0.05, 0.06])
    test_parameter("PO4", wqi_ppo4, [0.05, 0.1, 0.2, 0.3, 0.5, 4.0, 5.0])

    print("\n" + "="*30)
    print("🔹 Group V ")
    print("="*30)
    test_parameter("Coliform", wqi_coliform, [1000, 2500, 5000, 7500, 10000, 11000])
    test_parameter("Ecoli", wqi_ecoli, [10, 20, 50, 100, 200, 250])
