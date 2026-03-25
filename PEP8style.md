Good question—and this is exactly the kind of polish that quietly sets you apart in interviews.

### What is PEP 8?

**PEP 8** is the official style guide for writing Python code.
Think of it as **“how Python code should look”** so that other engineers can read it quickly.

It’s not about correctness—it’s about **clarity and consistency**.

---

## The 20% of PEP 8 you actually need for interviews

Don’t try to memorize everything. Focus on these:

### 1. Naming (MOST important)

* Variables & functions → `snake_case`

  ```python
  dummy_head = ListNode(0)
  merge_two_lists()
  ```

* Classes → `PascalCase`

  ```python
  class ListNode:
  ```

* Constants → `UPPER_CASE`

  ```python
  MAX_SIZE = 100
  ```

👉 This is the one interviewers actually notice.

---

### 2. Spacing & formatting

* Use spaces around operators:

  ```python
  if a == b:
  ```

* No extra spaces:

  ```python
  curr = curr.next   # good
  curr=curr.next     # bad
  ```

---

### 3. Indentation

* Always **4 spaces** (never tabs)

---

### 4. Keep it readable

* Avoid overly long lines (roughly < 79–100 chars)
* Break things cleanly if needed

---

### 5. Imports (less relevant for interviews)

```python
import math
from typing import Optional
```

---

## What Microsoft & Bloomberg actually expect

At companies like Microsoft and Bloomberg:

* They **won’t reject you for small style issues**
* But clean style signals:

  * professionalism
  * production experience
  * attention to detail

Think of PEP 8 as:

> “quiet bonus points,” not “pass/fail criteria”

## Quick mental checklist during interviews

Before you hit “done”, do this in 5 seconds:

* Did I use `snake_case`?
* Is indentation clean?
* Any obvious spacing issues?

That’s it. Move on.

---

If you want, I can do a **mock Microsoft-style question with feedback on both logic + style**—that would be the highest ROI right now.
