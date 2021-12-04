print("\n*** Day One ***\n")
# Part ONE
print("+++ Part ONE +++\n")

import numpy as np

with open("day1_21.txt", "r") as fp:
    raw_input = fp.readlines()
depths = [(i.split("\n")[0]) for i in raw_input]
depths = list(map(int, depths))

depths_diff = np.diff(depths)
print(f"Increasing Depths: {sum(1 for d in depths_diff if d > 0)}\n")

# Part TWO
print("\n+++ Part TWO +++\n")

depths3m = []

for i in range(len(depths)-2):
    depths3m.append((depths[i] + depths[i + 1] + depths[i + 2])/3)

depths3m_diff = np.diff(depths3m)
print(f"Increasing Depths (three mean): {sum(1 for d in depths3m_diff if d > 0)}\n")