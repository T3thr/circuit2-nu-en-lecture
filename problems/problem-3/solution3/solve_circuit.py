#!/usr/bin/env python3
# -*- font-encoding: utf-8 -*-
"""
solve_circuit.py - Problem 3 Matrix Solver & Cut-set Verification Script
วิเคราะห์และแก้สมการชุดตัด (Cut-set Equations) และคำนวณแรงดันปม Va, Vb, Vc, Vd
วิชา 303212 Electrical Circuit Analysis II
"""

import numpy as np

def solve_problem_3(E1=12.0, E2=6.0, E3=4.0, G1=0.5, G2=0.25, G3=0.2, G4=0.1):
    """
    คำนวณแรงดันปม Va, Vb, Vc, Vd และพิสูจน์ KCL/Cut-set Equations
    
    พารามิเตอร์:
      E1 : แรงดันแหล่งกำเนิด 1 [V] (Va = E1)
      E2 : แรงดันแหล่งกำเนิด 2 [V] (ขั้วลบที่ปม d => Vd = -E2)
      E3 : แรงดันแหล่งกำเนิด 3 [V] (Vc - Vb = E3)
      G1, G2, G3, G4 : ความนำไฟฟ้า [S หรือ Mho]
    """
    print("=" * 65)
    print("⚡ โปรแกรมประมวลผลวงข่ายความนำไฟฟ้าและสมการชุดตัด (ข้อที่ 3)")
    print("=" * 65)
    print(f"ค่าตัวแปรขาเข้า (Inputs):")
    print(f"  E1 = {E1:.4f} V, E2 = {E2:.4f} V, E3 = {E3:.4f} V")
    print(f"  G1 = {G1:.4f} S, G2 = {G2:.4f} S, G3 = {G3:.4f} S, G4 = {G4:.4f} S")
    print("-" * 65)

    # 1. แรงดันปม Va และ Vd (ทราบค่าจาก Independent Voltage Sources ตรงๆ)
    Va = E1
    Vd = -E2

    # 2. คำนวณ Vb จากสมการ KCL Supernode (b, c)
    # G1*(Vb - E1) + G3*Vb + G2*(Vb + E3 - (-E2)) = 0
    # (G1 + G2 + G3)*Vb = G1*E1 - G2*E2 - G2*E3
    denom = G1 + G2 + G3
    num_b = G1 * E1 - G2 * E2 - G2 * E3
    Vb = num_b / denom

    # 3. คำนวณ Vc จากสมการ Supernode Vc = Vb + E3
    Vc = Vb + E3

    # 4. แรงดัน Ve (Reference Ground)
    Ve = 0.0

    print("📊 ผลลัพธ์แรงดันปม (Node Voltages):")
    print(f"  V_a = {Va:10.4f} V  (เท่ากับ E1)")
    print(f"  V_b = {Vb:10.4f} V  (คำนวณจาก KCL Supernode)")
    print(f"  V_c = {Vc:10.4f} V  (เท่ากับ Vb + E3)")
    print(f"  V_d = {Vd:10.4f} V  (เท่ากับ -E2 เนื่องจากขั้วลบอยู่ที่ปม d)")
    print(f"  V_e = {Ve:10.4f} V  (Reference Ground)")
    print("-" * 65)

    # 5. คำนวณกระแสไหลในกิ่งต่างๆ (Branch Currents)
    i_G1 = G1 * (Va - Vb)
    i_G3 = G3 * (Vb - Ve)
    i_G2 = G2 * (Vc - Vd)
    i_G4 = G4 * (Vd - Ve)

    print("🔌 กระแสไฟฟ้าในกิ่งความนำ (Branch Currents):")
    print(f"  i_G1 (a -> b) = {i_G1:10.4f} A")
    print(f"  i_G3 (b -> e) = {i_G3:10.4f} A")
    print(f"  i_G2 (c -> d) = {i_G2:10.4f} A")
    print(f"  i_G4 (d -> e) = {i_G4:10.4f} A")
    print("-" * 65)

    # 6. ตรวจสอบ KCL ที่ Supernode (b, c): i_G1 - i_G3 - i_G2 == 0
    kcl_check = i_G1 - i_G3 - i_G2
    print(f"✅ ตรวจสอบ KCL ที่ Supernode (b, c): i_G1 - i_G3 - i_G2 = {kcl_check:.12f} A (ต้องเป็น 0)")
    print("=" * 65)

    return {
        "Va": Va, "Vb": Vb, "Vc": Vc, "Vd": Vd, "Ve": Ve,
        "i_G1": i_G1, "i_G3": i_G3, "i_G2": i_G2, "i_G4": i_G4
    }

if __name__ == "__main__":
    solve_problem_3()
