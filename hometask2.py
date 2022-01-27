def calculator(program, value):
    acc = value
    for i in program:
        if i == "1":
            acc = acc**2
        elif i == "2":
            acc -= 1
    return acc
def build_program(start, finish):
    for l in '*12':
        for q in '*12':
            for k in '*12':
                for n in '*12':
                    program = "".join([l,q,k,n])
                    result = calculator(program, start)
                    if result == finish:
                        return program.replace('*', '')
if __name__ == "__main__":
    program = build_program(5,8)
    if program is None:
        print("решения нет")
    else:
        print(f'Программа {program}')