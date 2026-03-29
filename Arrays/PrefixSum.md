Good — prefix sums are one of those patterns that feel abstract until they “click,” and then you start seeing them everywhere (arrays, maps, sliding windows, even DP).

Let’s make it click.

---

# 🧠 Core idea (don’t skip this)

> **Prefix sum = cumulative sum up to an index**

```text
nums:        [2, 4, 1, 3]
prefix_sum:  [2, 6, 7, 10]
```

So:

* `prefix[i] = sum of nums[0 → i]`

---

# 🔑 Why this is powerful

👉 You can compute any subarray sum in **O(1)**

Instead of:

```text
sum(i → j) = nums[i] + nums[i+1] + ... + nums[j]   ❌ O(n)
```

You do:

```python
sum(i → j) = prefix[j] - prefix[i - 1]   ✅ O(1)
```

---

# 🔥 Pattern 1: Range Sum (basic)

### Use when:

* “Find sum of subarray quickly”
* Multiple queries

### Code:

```python
prefix = [0] * len(nums)
prefix[0] = nums[0]

for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]
```

Then:

```python
def range_sum(i, j):
    if i == 0:
        return prefix[j]
    return prefix[j] - prefix[i - 1]
```

---

# 🔥 Pattern 2: Subarray Sum = K (MOST IMPORTANT)

This is the one interviewers love.

## Idea:

Instead of checking all subarrays → use math

We want:

```text
sum(i → j) = k
```

Using prefix:

```text
prefix[j] - prefix[i] = k
```

Rearrange:

```text
prefix[i] = prefix[j] - k
```

---

## 💡 Insight

> “Have I seen a prefix sum = (current_sum - k) before?”

---

## ✅ Code pattern

```python
from collections import defaultdict

count = 0
prefix_sum = 0
freq = defaultdict(int)
freq[0] = 1   # important

for num in nums:
    prefix_sum += num
    
    if (prefix_sum - k) in freq:
        count += freq[prefix_sum - k]
    
    freq[prefix_sum] += 1
```

---

## 🧠 Why `freq[0] = 1`?

Handles case where:

```text
prefix_sum == k
```

---

# 🔥 Pattern 3: Longest Subarray with Sum K

Same idea, but store **first occurrence only**

```python
prefix_map = {0: -1}
prefix_sum = 0
max_len = 0

for i in range(len(nums)):
    prefix_sum += nums[i]
    
    if (prefix_sum - k) in prefix_map:
        max_len = max(max_len, i - prefix_map[prefix_sum - k])
    
    if prefix_sum not in prefix_map:
        prefix_map[prefix_sum] = i
```

---

# 🔥 Pattern 4: Binary array tricks (0s and 1s)

### Example:

“Equal number of 0s and 1s”

👉 Trick:

* Convert `0 → -1`
* Then problem becomes:
  → “subarray with sum = 0”

---

# ⚡ How to recognize prefix sum problems

Look for:

* “subarray sum”
* “number of subarrays”
* “sum equals k”
* “continuous subarray”
* “longest/shortest subarray”

---

# 🧠 Mental checklist

When you see a problem, ask:

1. Can I convert it to:

   ```text
   prefix[j] - prefix[i] = something
   ```
2. Can I rewrite as:

   ```text
   prefix[i] = prefix[j] - something
   ```
3. Can I store prefix sums in a hashmap?

If yes → **prefix sum pattern**

---

# 🚫 Common mistakes

* Forgetting:

  ```python
  freq[0] = 1
  ```
* Using list instead of hashmap (won’t work for negative numbers)
* Updating hashmap in wrong order

---

# 🎯 The real takeaway

Prefix sum is not about arrays.

It’s about this transformation:

> **Turn a range problem into a lookup problem**
