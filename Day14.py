from collections import defaultdict, Counter

file1 = open('inputs/input14.txt', 'r')
lines = file1.readlines()

current = lines[0][:-1]
print("Current: ", current)
mappings = {}

for line in lines[2:]:
    left, right = line[:-1].split(' -> ')
    mappings[left] = right

counts = Counter([a+b for a,b in zip(current, current[1:])])

print(mappings)
print(counts.items())

for i in range(40):
    new_counts = defaultdict(int)
    for pair, count in counts.items():
        for new_pair in [pair[0]+mappings[pair], mappings[pair]+pair[1]]:
            new_counts[new_pair] += count
    counts = new_counts

final = [max(sum(count for (p1,_),count in counts.items() if c == p1),
             sum(count for (_,p2),count in counts.items() if c == p2))
         for c in set(''.join(counts.keys()))]

print(max(final) - min(final))
