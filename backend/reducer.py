#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    skill, count = line.strip().split("\t")
    counts[skill] += int(count)

for skill, total in counts.items():
    print(f"{skill}\t{total}")
