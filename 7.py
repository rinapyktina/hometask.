from itertools import product

def calculator(program, value):
    acc = value
    for i in program:
        if i == "1":
            acc += 1
        elif i == "2":
            acc *= 2
    return acc

def build_program(k, b, r):
    for i in range(1, r + 1):
        space = ["12"] * r
        for h in product(*space):
            program = "".join(h)
            result = calculator(program, k)
            c = 0
            if result == b:
                c += 1
                return c
    return None

if __name__ == '__main__':
    program = build_program(1, 16, 15)
    if program != None:
        print(program)