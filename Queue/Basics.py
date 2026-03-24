from collections import deque

queue = deque ()
queue.append(1)
queue.append(2)


1) Empty queue
from collections import deque
queue = deque()
2) Queue with initial elements
deque(...) takes an iterable. If you want to start with one element, you typically pass a 1-item iterable like a list:

queue = deque([item])   # one initial element
3) Why [] is commonly used
Because many single items (like an int) are not iterable, so you can’t do:

queue = deque(item)     # TypeError if item is an int
4) Alternatives to []
If item is iterable (like a string), deque(item) will split it into elements:
deque("ab")   # deque(['a', 'b'])
If you want exactly one element without using [], you can use a 1-tuple:
queue = deque((item,))
So: [] isn’t required, it’s just a convenient way to provide an iterable—especially for the “single initial element” case.


###
queue = deque(["Task 1", "Task 2", "Task 3"]) ... so this is a queue which is created with an iterable list of 3 items
if you did deque("Task 1") (one argument), it would create a deque of characters ('T', 'a', 's', ...), because a string is an iterable of characters.
  
Python's deque uses popleft() for efficient dequeue operations.



