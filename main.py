class MyRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value = self.start
        self.start += self.step
        return value
```

```python
# Testlash
my_range = MyRange(1, 10)
for i in my_range:
    print(i)

my_range = MyRange(10, 1)
try:
    for i in my_range:
        print(i)
except StopIteration:
    print("Iteratsiya tugagan")
