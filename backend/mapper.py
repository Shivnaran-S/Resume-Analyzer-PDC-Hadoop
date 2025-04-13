#!/usr/bin/env python3
import sys

skills = {"python", "java", "sql", "excel", "machine", "learning", "flask"}

for line in sys.stdin:
    for word in line.lower().split():
        if word in skills:
            print(f"{word}\t1")
