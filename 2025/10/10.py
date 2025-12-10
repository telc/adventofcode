#!/usr/bin/env python

import sys
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

def init(filename: str):
    with open(filename, 'r') as f:
        return [x.split() for x in f.read().splitlines()]
    
def decode_machine(machine: list[str]):
    lights = {i for i, v in enumerate(machine[0][1:-1]) if v == '#'}
    buttons = [(y,) if isinstance(y, int) else y for y in (eval(x) for x in machine[1:-1])]
    joltage = tuple(map(int, machine[-1][1:-1].split(',')))
    return lights, buttons, joltage

def calculate_light_presses(lights: set[int], buttons: list[tuple[int]]):
    """
    Find minimum button presses to reach target light configuration.
    Uses Gaussian elimination over GF(2).
    """
    # Determine number of lights (max light index + 1)
    max_light = max(lights) if lights else -1
    for button in buttons:
        if button:
            max_light = max(max_light, max(button))

    n = max_light + 1  # number of lights
    m = len(buttons)   # number of buttons

    if n == 0:
        return 0

    # Create target vector (which lights should be on)
    target = np.array([1 if i in lights else 0 for i in range(n)], dtype=np.int8)

    # Create matrix where A[light][button] = 1 if button toggles light
    A = np.zeros((n, m), dtype=np.int8)
    for j, button in enumerate(buttons):
        for i in button:
            A[i, j] = 1

    # Augmented matrix [A | target]
    aug = np.column_stack([A, target])

    # Gaussian elimination to RREF over GF(2)
    pivot_cols = []
    for col in range(m):
        # Find pivot in column col
        pivot_row = None
        for row in range(len(pivot_cols), n):
            if aug[row, col] == 1:
                pivot_row = row
                break
        if pivot_row is None:
            continue
        # Swap to put pivot in correct position
        target_row = len(pivot_cols)
        if pivot_row != target_row:
            aug[[target_row, pivot_row]] = aug[[pivot_row, target_row]]
        pivot_cols.append(col)
        # Eliminate all other 1s in this column (XOR in GF(2))
        for row in range(n):
            if row != target_row and aug[row, col] == 1:
                aug[row] ^= aug[target_row]

    # Check for inconsistency (no solution)
    for row in range(len(pivot_cols), n):
        if aug[row, m] == 1:
            return None

    # Find particular solution (all free variables = 0)
    particular = np.zeros(m, dtype=np.int8)
    for i, col in enumerate(pivot_cols):
        particular[col] = aug[i, m]

    # Free variables (buttons not in pivot columns)
    free_vars = [i for i in range(m) if i not in pivot_cols]

    # Try all combinations of free variables to find minimum presses
    min_presses = int(particular.sum())
    for mask in range(1, 1 << len(free_vars)):
        solution = np.zeros(m, dtype=np.int8)
        # Set free variables according to mask
        for i, var in enumerate(free_vars):
            solution[var] = (mask >> i) & 1
        # Update basic variables based on free variables
        for i, col in enumerate(pivot_cols):
            val = aug[i, m]
            for fv in free_vars:
                if solution[fv] == 1:
                    val ^= aug[i, fv]
            solution[col] = val
        min_presses = min(min_presses, int(solution.sum()))

    return min_presses

def p1(machines: list[list[str]]):
    presses = 0
    for machine in machines:
        lights, buttons, _ = decode_machine(machine)
        presses += calculate_light_presses(lights, buttons)
    print(presses)

def calculate_joltage_presses(joltage: tuple[int], buttons: list[tuple[int]]):
    """
    Find minimum button presses to reach target joltage configuration.
    Uses Integer Linear Programming (ILP) to solve efficiently.
    """
    # Determine number of counters
    n = len(joltage)  # number of counters
    m = len(buttons)  # number of buttons

    if n == 0:
        return 0

    # Create matrix where A[counter][button] = 1 if button affects counter
    A = np.zeros((n, m), dtype=float)
    for j, button in enumerate(buttons):
        for i in button:
            if i < n:
                A[i][j] = 1.0

    # Target vector
    target = np.array(joltage, dtype=float)

    # Objective: minimize sum of button presses (coefficients all 1)
    c = np.ones(m)

    # Constraint: A * x = target
    constraints = LinearConstraint(A, target, target)

    # Bounds: x >= 0 (non-negative integer)
    bounds = Bounds(0, np.inf)

    # Solve as integer linear program
    # Use integrality constraint: all variables must be integers
    integrality = np.ones(m, dtype=int)  # 1 means integer variable

    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

    if result.success:
        return int(round(result.fun))
    else:
        return None

def p2(machines: list[list[str]]):
    presses = 0
    for i, machine in enumerate(machines):
        _, buttons, joltage = decode_machine(machine)
        result = calculate_joltage_presses(joltage, buttons)
        if result is None:
            print(f"Warning: Machine {i} has no solution", file=sys.stderr)
            continue
        presses += result
    print(presses)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    machines = init(filename)
    p1(machines)
    p2(machines)
