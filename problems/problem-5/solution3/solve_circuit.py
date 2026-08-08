#!/usr/bin/env python3
"""เครื่องแก้โจทย์ 303212 ข้อ 5: conductance network + directed graph.

Topology/orientation:
  1 e->a: G1 in series with E1, i1=G1(E1-Va)
  2 a->b: E3 in series with G2, i2=G2(Va-E3-Vb)
  3 a->e: G3, i3=G3 Va
  4 b->e: G4, i4=G4 Vb
  5 b->e: ideal E2 with negative terminal at b, Vb=-E2

Run: python3 solve_circuit.py [--G1 ... --json result.json]
Uses Python standard library only; no NumPy required.
"""
from __future__ import annotations
import argparse, json, math, random
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a): return [list(x) for x in zip(*a)]

def solve2(a, b):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    if abs(det)<1e-14: raise ValueError("singular 2x2 matrix")
    return ((b[0]*a[1][1]-a[0][1]*b[1])/det,
            (a[0][0]*b[1]-b[0]*a[1][0])/det)

def network(g1,g2,g3,g4,e1,e2,e3):
    if min(g1,g2,g3,g4)<0: raise ValueError("conductance must be non-negative")
    den=g1+g2+g3
    if den<=0: raise ValueError("G1+G2+G3 must be positive")
    vb=-e2
    va=(g1*e1+g2*e3-g2*e2)/den
    # A x=b: second row is the ideal-source constraint Vb=-E2
    A=[[den,-g2],[0.0,1.0]]
    rhs=[g1*e1+g2*e3,-e2]
    va2,vb2=solve2(A,rhs)
    i1=g1*(e1-va); i2=g2*(va-e3-vb); i3=g3*va; i4=g4*vb
    ie2=i2-i4                         # direction b->e in stated KCL
    kcla=i1-i3-i2
    kclb=i2-i4-ie2
    # Complete/reduced incidence convention: +1 leaves node, -1 enters node
    Aa=[[-1,1,1,0,0],[0,-1,0,1,1],[1,0,-1,-1,-1]] # rows a,b,e
    Ar=[row[:] for row in Aa[:2]]
    Qg=[[-1,1,1,0],[0,-1,0,1]]       # conductance columns 1..4
    Y=[[g1,0,0,0],[0,g2,0,0],[0,0,g3,0],[0,0,0,g4]]
    M=matmul(matmul(Qg,Y),transpose(Qg))
    return {
      "parameters":{"G1":g1,"G2":g2,"G3":g3,"G4":g4,"E1":e1,"E2":e2,"E3":e3},
      "A":A,"rhs":rhs,"Aa":Aa,"Ar":Ar,"Qg":Qg,"Yb":Y,"QYQT":M,
      "voltage":{"Va":va,"Vb":vb},
      "current":{"iG1":i1,"iG2":i2,"iG3":i3,"iG4":i4,"iE2":ie2},
      "residual":{"formula_vs_matrix":max(abs(va-va2),abs(vb-vb2)),"KCL_a":kcla,"KCL_b":kclb},
      "note":"RHS sign is +G2*E3 because i2=G2(Va-E3-Vb); the alternative -G2*E3 is inconsistent with that constitutive equation."
    }

def main():
    p=argparse.ArgumentParser()
    for name,default in [("G1",.4),("G2",.3),("G3",.2),("G4",.5),("E1",12.),("E2",6.),("E3",2.)]:
        p.add_argument("--"+name,type=float,default=default)
    p.add_argument("--trials",type=int,default=1000)
    p.add_argument("--json",nargs="?",const="result.json")
    a=p.parse_args(); r=network(a.G1,a.G2,a.G3,a.G4,a.E1,a.E2,a.E3)
    print("=== ข้อ 5: Directed Conductance Network ===")
    print("A x = b")
    for row,bb in zip(r["A"],r["rhs"]): print(f"  {row}   {bb:.6f}")
    print(f"Va = {r['voltage']['Va']:.12f} V")
    print(f"Vb = {r['voltage']['Vb']:.12f} V")
    for k,v in r["current"].items(): print(f"{k:>4} = {v:.12f} A")
    print("QG Yb QG^T =")
    for row in r["QYQT"]: print(" ", [round(x,12) for x in row])
    print("residuals =",r["residual"])
    assert max(abs(x) for x in r["residual"].values())<1e-10
    worst=0.0; rng=random.Random(30321205)
    for _ in range(a.trials):
        vals=[rng.uniform(.02,5) for _ in range(4)]+[rng.uniform(-30,30) for _ in range(3)]
        t=network(*vals); worst=max(worst,max(abs(x) for x in t["residual"].values()))
    print(f"random cross-check: {a.trials} cases, worst residual = {worst:.3e} ✅")
    if a.json:
        Path(a.json).write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding="utf-8")
        print("saved:",Path(a.json).resolve())
if __name__=="__main__": main()
