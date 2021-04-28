from numpy import binary_repr
opcode = {"ADD": "00001", "SUB": "00011", "AND": "00100", "OR": "00101", "XOR": "00110", "SR": "01000", "SRA": "01001", "SL": "01010", "ADDI": "10010", "ANDI": "10100", "ORI": "10101", "XORI": "10110", "LW": "11100", "SW": "11101", "BEQ": "11110", "BNE": "11111"}
reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "R7": "111"}
data = open("InstructionTestAssembler.asm", "r")
file = data.read()
file = file.split('\n')
label = {}
for i in range(len(file)):
    if file[i].find(':') != -1:
        label[file[i]] = i
for n in range(len(file)):
    if file[n].find('%') != -1:
        file[n] = file[n][0:file[n].find('%')]
    file[n] = file[n].replace(',', '')
    file[n] = file[n].replace('(', ' ')
    file[n] = file[n].replace(')', ' ')
    file[n] = file[n].split()
    if file[n][0] == 'SW' or file[n][0] == 'LW':
        temp = file[n][3]
        file[n][3] = file[n][2]
        file[n][2] = temp
    for i in range(len(file[n])):
        if i == 0:
            if file[n][0] == 'ADD' or file[n][0] == 'ADDI' or file[n][0] == 'BNE' or file[n][0] == 'SW' or file[n][0] == 'LW' or file[n][0] == 'SUB' or file[n][0] == 'BEQ' or file[n][0] == 'AND' or file[n][0] == 'XOR' or file[n][0] == 'XORI' or file[n][0] == 'SR' or file[n][0] == 'SRA' or file[n][0] == 'OR' or file[n][0] == 'ANDI' or file[n][0] == 'ORI' or file[n][0] == 'SL':
                file[n][i] = file[n][i].replace(file[n][i], opcode[file[n][i]])
            continue
        if i == 3:
            if file[n][0] == '11110' or file[n][0] == '11111':
                file[n][3] = file[n][3] + ':'
                x = (label[file[n][3]] - n * 2 / 2)
                file[n][3] = str(binary_repr(int(x), width=5))
                continue
            elif file[n][0] == '10010' or file[n][0] == '10100' or file[n][0] == '10101' or file[n][0] == '10110' or file[n][0] == '11100' or file[n][0] == '11101':
                file[n][i] = str(binary_repr(int(file[n][3]), width=5))
            else:
                file[n][i] = file[n][i].replace(file[n][i], reg[file[n][i]])
                file[n][3] = file[n][3] + '00'
            continue
        file[n][i] = file[n][i].replace(file[n][i], reg[file[n][i]])
    print(file[n])


file_new = open("binary_new.txt", "w")
for n in range(len(file)):
    for x in file[n]:
        if x == 'FAIL:':
            continue
        file_new.write(x)
    if x == 'FAIL:':
        continue
    file_new.write('\n')

file_new.close()
data.close()



















