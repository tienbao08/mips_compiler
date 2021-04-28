ADDI     R1, R0, 5 % R1 = 5
ADDI     R2, R0, 7 % R2 = 7
ADDI     R3, R0, 12
ADD      R4, R1, R2
BNE      R3, R4, FAIL
SW       R3, 0(R0)
LW       R5, 0(R0)
BNE      R3, R5, FAIL
SUB      R6, R2, R1
BEQ      R6, R3, FAIL
SR       R7, R4, R6
AND      R7, R7, R3
SUB      R1, R1, R2
XOR      R4, R1, R7
XORI     R5, R0, 2
SRA      R2, R5 ,R7
SW       R4, 0(R5)
LW       R6, 0(R5)
SW       R3, 2(R5)
LW       R7, 2(R5)
OR       R7, R5, R7
ANDI     R6, R6, 13
BNE      R7, R3, FAIL
SRA      R2, R4, R2
SW       R2, 8(R0)
SW       R7, 10(R0)
LW       R5, 2(R5)
OR       R1, R5, R1
SL       R1, R5, R5
ORI      R3, R1, 11
FAIL:
         ADDI     R3, R3, 2
XOR     R0, R0, R3