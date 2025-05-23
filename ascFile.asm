j L32
   


L1: 
sw ra,(sp)
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
L8: 
L9: 
L10: 
li t2,2
sub,t1,t1,t2 
sw t1, -24(sp)
L11: 
L12: 
L13: 
L14: 
add,t1,t1,t2
sw t1, -32(sp)
L15: 
lw t1, -32(sp)
L16: 
lw ra, (sp)
jr ra
L17: 
sw ra,(sp)
L18: 
div,t1,t1,t2
sw t1, -24(sp)
L19: 
lw t1, -24(sp)
mul,t1,t1,t2 
sw t1, -28(sp)
L20: 
lw t2, -28(sp)
beq,t1,t2,L22
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
lw ra, (sp)
jr ra
L26: 
sw ra,(sp)
L27: 
li t1,1
L28: 
li t1,2
sw t1, 16(sp)
L29: 
lw t1, -16(sp)
blt t1,t2,L31
L30: 
b L42
L31: 
L32: 
L33: 
L34: 
L35: 
lw t1, -20(sp)
li t2,1
beq,t1,t2,L37
L36: 
b L39
L37: 
li t1,0
L38: 
b L39
L39: 
lw t1, -16(sp)
li t2,1
add,t1,t1,t2
sw t1, -24(sp)
L40: 
lw t1, -24(sp)
sw t1, 16(sp)
L41: 
b L29
L42: 
lw ra, (sp)
jr ra
L43: 
addi sp,sp,32
mv gp,sp
L44: 
li a7,5 
ecall 
mv t1,a0 
sw t1,-12(gp)
L45: 
L46: 
L47: 
L48: 
