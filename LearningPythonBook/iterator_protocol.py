#!/usr/bin/python3

L = [1, 2, 3]

# Manual iteration (what for loops do behind the scenes)
it = iter(L)

while True:
    try:
        x = next(it)
    # StopIteration is raised when there are no more elements
    except StopIteration:
        break
    print(x ** 2, end=' ')

print("Next bit\n")

test = list(range(10))
print(test[2])
