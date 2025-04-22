# -*- coding: utf-8 -*-
"""
six_knapsack_models.py

Reproduction en Python/PuLP des modèles GMPL pour :
 1) maxKP 0/1
 2) minKP 0/1
 3) maxKP int (non borné)
 4) minKP int (non borné)
 5) maxKP LP (relaxation 0/1)
 6) minKP LP (relaxation 0/1)

Installez PuLP si nécessaire :
    pip install pulp
"""

import pulp


def solve_maxKP_01(p, w, capacity):
    """0/1 Knapsack max : var x_j ∈ {0,1}"""
    prob = pulp.LpProblem("maxKP_01", pulp.LpMaximize)
    # Variables
    x = {j: pulp.LpVariable(f"x_{j}", cat="Binary") for j in p}
    # Objectif
    prob += pulp.lpSum(p[j] * x[j] for j in p), "TotalProfit"
    # Contrainte de capacité
    prob += pulp.lpSum(w[j] * x[j] for j in w) <= capacity, "Capacity"
    # Résolution
    prob.solve()
    print("=== maxKP 0/1 ===")
    print("Status:", pulp.LpStatus[prob.status])
    print("Profit optimal =", pulp.value(prob.objective))
    print("Solution x =", {j: int(pulp.value(x[j])) for j in x})
    print()


def solve_minKP_01(c, s, demand):
    """0/1 Knapsack min : var x_j ∈ {0,1}, ∑ s_j x_j ≥ demand"""
    prob = pulp.LpProblem("minKP_01", pulp.LpMinimize)
    x = {j: pulp.LpVariable(f"x_{j}", cat="Binary") for j in c}
    prob += pulp.lpSum(c[j] * x[j] for j in c), "TotalCost"
    prob += pulp.lpSum(s[j] * x[j] for j in s) >= demand, "Demand"
    prob.solve()
    print("=== minKP 0/1 ===")
    print("Status:", pulp.LpStatus[prob.status])
    print("Coût optimal =", pulp.value(prob.objective))
    print("Solution x =", {j: int(pulp.value(x[j])) for j in x})
    print()


def solve_maxKP_int(p, w, capacity):
    """Unbounded Knapsack max : var x_j ∈ ℤ₊"""
    prob = pulp.LpProblem("maxKP_int", pulp.LpMaximize)
    x = {j: pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in p}
    prob += pulp.lpSum(p[j] * x[j] for j in p), "TotalProfit"
    prob += pulp.lpSum(w[j] * x[j] for j in w) <= capacity, "Capacity"
    prob.solve()
    print("=== maxKP int ===")
    print("Status:", pulp.LpStatus[prob.status])
    print("Profit optimal =", pulp.value(prob.objective))
    print("Solution x =", {j: int(pulp.value(x[j])) for j in x})
    print()


def solve_minKP_int(c, s, demand):
    """Unbounded Knapsack min : var x_j ∈ ℤ₊, ∑ s_j x_j ≥ demand"""
    prob = pulp.LpProblem("minKP_int", pulp.LpMinimize)
    x = {j: pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in c}
    prob += pulp.lpSum(c[j] * x[j] for j in c), "TotalCost"
    prob += pulp.lpSum(s[j] * x[j] for j in s) >= demand, "Demand"
    prob.solve()
    print("=== minKP int ===")
    print("Status:", pulp.LpStatus[prob.status])
    print("Coût optimal =", pulp.value(prob.objective))
    print("Solution x =", {j: int(pulp.value(x[j])) for j in x})
    print()


def solve_maxKP_lp(p, w, capacity):
    """LP relaxation of maxKP 0/1 : var 0 ≤ x_j ≤ 1"""
    prob = pulp.LpProblem("maxKP_lp", pulp.LpMaximize)
    x = {j: pulp.LpVariable(f"x_{j}", lowBound=0, upBound=1, cat="Continuous") for j in p}
    prob += pulp.lpSum(p[j] * x[j] for j in p), "TotalProfit"
    prob += pulp.lpSum(w[j] * x[j] for j in w) <= capacity, "Capacity"
    prob.solve()
    print("=== maxKP LP ===")
    print("Status:", pulp.LpStatus[prob.status])
    print("Profit LP =", pulp.value(prob.objective))
    print("Solution x =", {j: pulp.value(x[j]) for j in x})
    print()


def solve_minKP_lp(c, s, demand):
    """LP relaxation of minKP 0/1 : var 0 ≤ x_j ≤ 1"""
    prob = pulp.LpProblem("minKP_lp", pulp.LpMinimize)
    x = {j: pulp.LpVariable(f"x_{j}", lowBound=0, upBound=1, cat="Continuous") for j in c}
    prob += pulp.lpSum(c[j] * x[j] for j in c), "TotalCost"
    prob += pulp.lpSum(s[j] * x[j] for j in s) >= demand, "Demand"
    prob.solve()
    print("=== minKP LP ===")
    print("Status:", pulp.LpStatus[prob.status])
    print("Coût LP =", pulp.value(prob.objective))
    print("Solution x =", {j: pulp.value(x[j]) for j in x})
    print()


if __name__ == "__main__":
    p = {1: 42, 2: 42, 3: 68, 4: 68, 5: 77, 6: 57, 7: 17, 8: 19, 9: 94, 10: 34}
    w = {1: 81, 2: 42, 3: 56, 4: 25, 5: 14, 6: 63, 7: 75, 8: 41, 9: 19, 10: 12}
    capacity = 214

    c = {1: 42, 2: 42, 3: 68, 4: 68, 5: 77, 6: 57, 7: 17, 8: 19, 9: 94, 10: 34}
    s = {1: 81, 2: 42, 3: 56, 4: 25, 5: 14, 6: 63, 7: 75, 8: 41, 9: 19, 10: 12}
    demand = 214

    # Appels
    solve_maxKP_01(p, w, capacity)
    solve_minKP_01(c, s, demand)
    solve_maxKP_int(p, w, capacity)
    solve_minKP_int(c, s, demand)
    solve_maxKP_lp(p, w, capacity)
    solve_minKP_lp(c, s, demand)
