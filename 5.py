def calc(program, value):
    acc = value
    for i in program:
        if i == '1':
            acc += 2
        elif i == '2':
            acc *= 3
    return acc

def build(start, finish):
    for i in '*12':
        for j in '*12':
            for k in '*12':
                for l in '*12':
                    for m in '*12':
                        program = "".join([i, j, k, l, m])
                        result = calc(program, start)
                        if result == finish:
                            return program.replace("*", "")
    return None

if __name__ == "__main__":
    program = build(1,31)
    if program is None:
        print("нет решений")
    else:
        print(f'Программа {program}')