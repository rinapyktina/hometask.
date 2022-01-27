from itertools import product

def calculator(program, value):
    acc=value
    for i in program:
        if i == "1":
            acc += 3
        elif i == "2":
            acc *= 2
    return acc

def build_program(v, g, m):
    for i in range(1, m + 1):
        space = ["12"] * m
        for k in product(*space):
            program = "".join(k)
            result = calculator(program, v)
            if result == g:
                return program
    return None

if __name__ == '__main__':
    program = build_program(2, 31, 6)
    if program != None:
        print(program)