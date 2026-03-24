from collections import deque

def execute(program: list[str]) -> deque[int]:
    queue = deque ()
    for instruction in program:
        parts = instruction.split()
        if parts[0] == "push":
            queue.append(parts[1])
        elif parts [0] == "peek":
            if len (queue) == 0:
                print ("Queue is empty!")
            else:
                print (queue[0])
        elif parts [0] == "pop":
            if len (queue) == 0:
                print ("Queue is empty!")
            else:
                el = queue.popleft()             
    return queue
