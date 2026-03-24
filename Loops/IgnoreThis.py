Using _ is good when a value is required syntactically (you must bind something), but you intentionally won’t use it. It’s a readability signal: “ignore this”.

Common cases
1) Repeat something n times (like the article’s range(len(program)) pattern)
for _ in range(3):
    do_something()
You don’t care about the loop counter.

2) Unpacking when you only need some parts
pair = (10, 20)
x, _ = pair   # ignore the second value
With enumerate when you don’t need the index:

for _, instruction in enumerate(program):
    process(instruction)
(Though for instruction in program: is even cleaner.)

3) Ignoring a return value you don’t need
_, remainder = divmod(10, 3)  # ignore quotient
4) Placeholder variable (temporary / “to be used later”)
Sometimes used when sketching code, but it’s better to replace it with a meaningful name once you actually use it.

Caution
In Python REPL and some codebases, _ is also used to mean “last expression result” or for translations (gettext). In normal scripts, using _ as “unused” is fine, but avoid it if your project already uses _ for something else.
