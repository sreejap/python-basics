1) for p in program: (most common / cleanest)
Use when you only need the instruction itself.

for p in program:
    # p is an instruction like "push 3", "peek", "pop"
    ...
2) for i, p in enumerate(program):
Use when you need both the index and the instruction (e.g., debugging, referencing position).

for i, p in enumerate(program):
    # i is 0..n-1, p is the instruction
    ...
3) for i in range(len(program)): (index-based)
Use when you specifically want index-based access (less idiomatic in Python unless you need indexing).

for i in range(len(program)):
    p = program[i]
    ...
Rule of thumb: prefer for p in program unless you need the index; then use enumerate(program).
