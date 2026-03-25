text = "Hello"
print(len(text))     # 5
print(text[0])       # 'H'
print(text[4])       # 'o'
# Python strings are **immutable** - you cannot change individual characters after creation.

# accessing from the end
word = "hello"
print(word[-1])  # 'o' (last character)
print(word[-2])  # 'l' (second to last)
print(word[-5])  # 'h' (first character)
# Python supports negative indices counting from the end.

text = "hello"

# Iterate using for-in (gets characters directly)
for char in text:
    print(char)  # h, e, l, l, o

# Iterate using indices
for i in range(len(text)):
    print(text[i])  # h, e, l, l, o

# to convert to lower case:
char.lower() 

Below is a practical, fairly complete reference of what you’ll use for character handling.

## 1) `str` methods commonly used for characters

### Classification / checks (return `True/False`)

- `c.isalpha()` — alphabetic (Unicode letters)
- `c.isdigit()` — digit (Unicode digits)
- `c.isdecimal()` — decimal digit (more strict than `isdigit`)
- `c.isnumeric()` — numeric (includes fractions, Roman numerals, etc.)
- `c.isalnum()` — alphanumeric
- `c.islower()` — lowercase
- `c.isupper()` — uppercase
- `c.istitle()` — titlecase (mostly for strings/words)
- `c.isspace()` — whitespace
- `c.isascii()` — ASCII only (`0-127`)
- `c.isidentifier()` — valid identifier (more meaningful for longer strings)
- `c.isprintable()` — printable character

### Case conversion

- `c.lower()`
- `c.upper()`
- `c.casefold()` — aggressive case-insensitive normalization (best for caseless matching)
- `c.capitalize()` — mostly for strings/words
- `c.title()` — mostly for strings/words
- `c.swapcase()`

### Search / membership-related (works on strings; for chars too)

- `s.count(sub)`
- `s.find(sub)`, `s.rfind(sub)`
- `s.index(sub)`, `s.rindex(sub)`
- `s.startswith(prefix)`, `s.endswith(suffix)`

### Unicode/encoding-related

- `c.encode(encoding="utf-8", errors="strict")`

### Whitespace trimming (more for strings, but works)

- `s.strip([chars])`, `s.lstrip([chars])`, `s.rstrip([chars])`

### Replacement / translation

- `s.replace(old, new, count=-1)`
- `s.translate(table)`
- `str.maketrans(...)` (helper to build translation tables)

## 2) Built-in functions useful for characters

- `len(c)` — length (a “char” should be `1`)
- `ord(c)` — character → Unicode code point (int)
- `chr(n)` — code point (int) → character
- `repr(c)` — printable representation (shows escapes)
- `ascii(c)` — ASCII-only representation with escapes
- `str(x)` — convert to string
- `format(x, spec)` — formatting (less char-specific)
- `print(c)` — output

## 3) Standard library for character properties: `unicodedata`

This is the main “character library” in Python’s stdlib.

```python
import unicodedata as ud

ud.name(c)          # official Unicode name
ud.category(c)      # general category, e.g. 'Lu', 'Ll', 'Nd'
ud.bidirectional(c) # bidi class
ud.combining(c)     # combining class (0 means not combining)
ud.east_asian_width(c)
ud.mirrored(c)      # 1 if mirrored in bidi contexts else 0
ud.normalize(form, s)  # 'NFC', 'NFD', 'NFKC', 'NFKD'
ud.decimal(c, default=None)
ud.digit(c, default=None)
ud.numeric(c, default=None)
```

## 4) Common “char constants” (not functions) in `string` module

```python
import string

string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
string.digits
string.hexdigits
string.octdigits
string.punctuation
string.whitespace
string.printable

# for string formatting
# Using f-strings (preferred for formatting)
message = f"{greeting}, {name}!"
print(message)  # "Hello, Alice!"

# String concatenation

# Inefficient: creates many temporary strings
result = ""
for i in range(1000):
    result += str(i) + " "

# Efficient: join builds once
pieces = [str(i) for i in range(1000)]
result = " ".join(pieces)
# join is much more efficient than repeated +=

# Case insensitive string comparison
Use a normalized version of both strings (most commonly `.lower()`, or better `.casefold()` for robust Unicode case-insensitive matching):
print(text1.casefold() != text3.casefold())  # case-insensitive not-equal
# or
print(text1.casefold() == text3.casefold())  # case-insensitive equal

If you only care about basic ASCII letters, `.lower()` is fine:
print(text1.lower() != text3.lower())
# upper() - is the method to convert to Upper case

## string comparison

def compare_strings(s1: str, s2: str) -> int:
    s1 = s1.casefold() # to convert to lowercase
    s2 = s2.casefold()
    len1 = len (s1)
    len2 = len (s2)
    i= j = 0
    while i < len1 and j < len2: # invalid syntax to use && 
        if s1[i] < s2[j]:
            return -1
        elif s1[i] > s2[j]:
            return 1
        else:
            i +=1
            j +=1
        
    if len1 == len2:        
        return 0
    elif i < len1:
        return 1
    else:
        return -1

# to call a method
def compare_strings_case_insensitive(s1: str, s2: str) -> int:
    s1 = s1.casefold()
    s2 = s2.casefold()
    return compare_strings(s1, s2)

# String libraries
text = "  Hello World  "
# String Methods

# Searching
print(text.find("World"))      # 8 (position)
print("World" in text)         # True
print(text.startswith("  H"))  # True
print(text.endswith("d  "))    # True

# Extracting
print(text[2:7])               # "Hello"
print(text.strip())            # "Hello World"

# Transforming
print(text.upper())            # "  HELLO WORLD  "
print(text.lower())            # "  hello world  "
print(text.replace("World", "Python"))  # "  Hello Python  "

# Splitting
words = "apple,banana,orange".split(",")
print(words)  # ['apple', 'banana', 'orange']
# Python strings have rich method libraries for text processing.

# Method categories
# Length and checking
text = "hello"
print(len(text))           # 5
print(text.isalpha())      # True
print(text.isdigit())      # False
print("123".isdigit())     # True

# Case methods
print("hello".capitalize())     # "Hello"
print("hello world".title())    # "Hello World"

# Padding
print("42".zfill(5))            # "00042"
print("left".ljust(10, "-"))    # "left------"
print("right".rjust(10, "-"))   # "-----right"

# Splitting variations
print("a,b,,c".split(","))      # ['a', 'b', '', 'c']
print("line1\nline2".splitlines())  # ['line1', 'line2']

# In Python, strings are immutable. Direct character assignment raises a `TypeError`. Methods like `upper()` or `replace()` return new strings rather than modifying the original. The same pattern applies across these languages: string operations always produce new strings.
# In Python, assignment like `text[0] = 'H'` raises a `TypeError` at runtime.

# Efficient: build list, join once
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)


# isalnum - is alpanumeric

# Quick comparison
c = s[i]
c.isalnum()        # normal / idiomatic
str.isalnum(c)     # equivalent, less common
isalnum(c)          # NameError (unless you defined isalnum yourself)


