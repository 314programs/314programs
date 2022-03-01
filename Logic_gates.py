Logic_gate = input('Input the desired logic gate: ')

def convert(val):
    if val == '0':
        return False
    else:
        return True

def convert_num(val):
    if val == True:
        return 1
    else:
        return 0

if Logic_gate == 'NOT':
    A = input('Enter input A: ')
    A = convert(A)
    print(convert_num(not A))
else:
    A = input('Enter input A: ')
    B = input('Enter input B: ')
    A = convert(A)
    B = convert(B)

    if Logic_gate == 'AND':
        print(convert_num(A and B))
    if Logic_gate == 'NAND':
        print(convert_num(not (A and B)))
    if Logic_gate == 'OR':
        print(convert_num(A or B))
    if Logic_gate == 'NOR':
        print(convert_num(not (A or B)))
