import os
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fab(5)
proDir = os.path.split(os.path.realpath(__file__))[0]
print(proDir)