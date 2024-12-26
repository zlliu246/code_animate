from src.code_animate import animate
import inspect

ONE = 1
TWO = 2

@animate
def test():
    a = ONE
    b = TWO

    output = 0
    for i in range(5):
        output += a + b

    return output

print(test())
