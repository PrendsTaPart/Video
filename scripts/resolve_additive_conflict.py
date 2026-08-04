#!/usr/bin/env python3
# Resolve a git conflict on an additive markdown tracking file (table rows
# appended independently on both sides) by keeping BOTH sides' lines,
# de-duplicated, instead of picking one. Used only for files where we've
# confirmed the conflict is "both branches appended different rows to the
# same table", never for code.
import sys, re

path = sys.argv[1]
text = open(path, encoding="utf-8").read()

pattern = re.compile(
    r"<<<<<<< [^\n]*\n(.*?)\n=======\n(.*?)\n>>>>>>> [^\n]*\n?",
    re.DOTALL,
)

def resolve(m):
    ours = m.group(1).split("\n")
    theirs = m.group(2).split("\n")
    seen = set()
    out = []
    for line in ours + theirs:
        if line not in seen:
            seen.add(line)
            out.append(line)
    return "\n".join(out) + "\n"

new_text, n = pattern.subn(resolve, text)
if n == 0:
    print(f"NO CONFLICT MARKERS FOUND in {path}")
    sys.exit(1)
open(path, "w", encoding="utf-8").write(new_text)
print(f"Resolved {n} conflict block(s) in {path}")
