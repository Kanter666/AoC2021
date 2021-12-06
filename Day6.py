from collections import Counter
from collections import defaultdict


file1 = open('inputs/input6.txt', 'r')
lines = file1.readlines()

days = [int(x) for x in lines[0].split(',')]
print(days)
counts = Counter(days)
print(counts)
for i in range(9):
    if not counts[i]:
        counts[i] = 0

for day in range(80):
    new_counts = defaultdict(int)
    new_counts[8] += counts[0]
    new_counts[6] += counts[0]

    for stage in range(8):
        new_counts[stage] += counts[stage+1]
    print(new_counts)
    counts = new_counts.copy()

total = 0
for i in range(9):
    total += new_counts[i]

print(total)
