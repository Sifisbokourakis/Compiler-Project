j L20
   


L1: 
sw ra,(sp)
L2: 
li t2,0
beq,t1,t2,L6
L3: 
b L4
L4: 
li t2,1
beq,t1,t2,L6
L5: 
b L8
L6: 
L7: 
b L18
L8: 
li t2,1
sub,t1,t1,t2 
sw t1, -16(sp)
L9: 
L10: 
L11: 
L12: 
li t2,2
sub,t1,t1,t2 
sw t1, -24(sp)
L13: 
L14: 
L15: 
L16: 
add,t1,t1,t2
sw t1, -32(sp)
L17: 
lw t1, -32(sp)
L18: 
lw ra, (sp)
jr ra
L19: 
addi sp,sp,20
mv gp,sp
L20: 
li a7,5 
ecall 
mv t1,a0 
sw t1,-12(gp)
L21: 
L22: 
L23: 
L24: 
mv a0 , t1 
li a7,1 
ecall 
L25: 
li a0,0
li a7,93
ecall
L26: 
