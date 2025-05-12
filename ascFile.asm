         


L1: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L2: 
li t2,1
ble,t1,t2,L4
L3: 
b L6
L4: 
L5: 
b L16
L6: 
li t2,1
sub,t1,t1,t2 
sw t1, -16(sp)
L7: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L8: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L9: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L10: 
li t2,2
sub,t1,t1,t2 
sw t1, -24(sp)
L11: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L12: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L13: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L14: 
add,t1,t1,t2
sw t1, -32(sp)
L15: 
lw t1, -32(sp)
L16: 
li a7,5 
ecall 
mv t1,a0 
sw t1,12(sp)
L17: 
li a7,5 
ecall 
mv t1,a0 
sw t1,16(sp)
L18: 
div,t1,t1,t2
sw t1, -24(sp)
L19: 
lw t1, -24(sp)
mul,t1,t1,t2 
sw t1, -28(sp)
L20: 
lw t2, -28(sp)
beq,t1,t1,L22
L21: 
b L24
L22: 
li t1,1
lw t0,-20(sp)
sw t1, (t0)
L23: 
b L25
L24: 
li t1,0
lw t0,-20(sp)
sw t1, (t0)
L25: 
li a7,5 
ecall 
mv t1,a0 
sw t1,16(sp)
L26: 
li a7,5 
ecall 
mv t1,a0 
