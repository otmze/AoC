# Part ONE
print("+++ Part ONE +++\n")

import numpy as np

with open("day10.txt", "r") as fp:
    raw_input = fp.readlines()
adapters = [(i.split("\n")[0]) for i in raw_input]
adapters = list(map(int, adapters))
adapters = adapters + [0, max(adapters) + 3]

adapters.sort()
jolt_diffs = np.diff(adapters)
unique, counts = np.unique(jolt_diffs, return_counts=True)
count_dict = dict(zip(unique, counts))
print("1-jolt: ", count_dict[1])
print("3-jolt: ", count_dict[3])
print("Multiplication:", (count_dict[1])*(count_dict[3]))

# Part TWO
print("\n+++ Part TWO +++\n")

from collections import defaultdict

diffs = defaultdict(int)
counts = defaultdict(int, {0: 1})

for a in (adapters[1:]):
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]

print("Distinct arrangements:", counts[adapters[-1]], "\n")