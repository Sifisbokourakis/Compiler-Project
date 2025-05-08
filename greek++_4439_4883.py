#Mpokourakis Iosif 4439 Vasilliki Maria Mpalaska 4883

import sys

alphabito =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω',
'Ά','Έ','Ή','Ί','Ό','Ύ','Ώ',
'α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω','ς',
'ά','έ','ή','ί','ό','ύ','ώ']

noumera =['0','1','2','3','4','5','6','7','8','9']

file = open(sys.argv[1],'r',encoding='utf-8')
#file = open('check_pinakas.gre', 'r', encoding='utf-8')

space = 0
letters = 1
numbers = 2
plus = 3
minus = 4
multi = 5
div = 6      
less = 7
greater = 8
equal = 9
#assign = 10
new_line = 10
semicolon = 11
coma = 12
colon = 13
left_parenthesis = 14
right_parenthesis = 15
left_bracket = 16
right_bracket = 17
#quotes = 18
left_comment = 18
right_comment = 19
modu = 20
underscore = 21
EOF = 22
wrong_symbol = 23

start_state = 0
letter_state = 1
number_state = 2
less_state = 3
greater_state = 4
assign_state =  5
comment_state = 6

#All the tokens for the symbols that the language have.
identifier_tk = 50
number_tk = 51
plus_tk = 52
minus_tk = 53
multi_tk = 54
div_tk = 55
less_tk = 56
greater_tk = 57
equal_tk = 58
lessOrEqual_tk = 59
greaterOrEqual_tk = 60
assign_tk = 61
semicolon_tk = 62
coma_tk = 63
colon_tk = 64
left_parenthesis_tk = 65
right_parenthesis_tk = 66
left_bracket_tk = 67
right_bracket_tk = 68
#quotes_tk = 69
left_comment_tk = 69
right_comment_tk = 70
modu_tk = 71
#underscore_tk = 72
EOF_tk = 72
different_tk = 73

#Tokens for all the words of the language.

program_tk = 100
declare_tk = 101
if_tk = 102
then_tk = 103
else_tk = 104
end_if_tk = 105
repeat_tk = 106
until_tk = 107
while_tk = 108
end_while_tk = 109
for_tk = 110
to_tk = 111
with_step_tk = 112
end_for_tk = 113
read_tk = 114
write_tk = 115
function_tk = 116
procedure_tk = 117
interface_tk = 118
input_tk = 119
output_tk = 120
begin_function_tk = 121
end_function_tk = 122
begin_procedure_tk = 123
end_procedure_tk = 124
begin_program_tk = 125
end_program_tk = 126
or_tk = 127
and_tk = 128
not_tk = 129
execute_tk = 130

ERROR_WRONG_SYMBOL = -1
ERROR_NUMBER_LETTER = -2
ERROR_EXCEDEED_LIMIT_OF_CHARACTERS = -3
ERROR_COMMENTS_WITH_EOF = -4
ERROR_RIGHT_COMMENT_ALONE = -5
ERROR_UNDERSCORE_ALONE = -6

states_array = [
    #start state
        [start_state, letter_state, number_state, plus_tk, minus_tk, multi_tk, div_tk, less_state, greater_state, equal_tk,
         start_state, semicolon_tk, coma_tk, assign_state, left_parenthesis_tk, right_parenthesis_tk, left_bracket_tk, right_bracket_tk,
         comment_state, ERROR_RIGHT_COMMENT_ALONE, modu_tk, ERROR_UNDERSCORE_ALONE, EOF_tk, ERROR_WRONG_SYMBOL],
    #letter_state
        [identifier_tk, letter_state, letter_state, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk,
         identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk, identifier_tk,
         identifier_tk, identifier_tk, identifier_tk, identifier_tk, letter_state, identifier_tk, ERROR_WRONG_SYMBOL],
    #number state
        [number_tk, ERROR_NUMBER_LETTER, number_state, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk,
         number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk, number_tk,
         ERROR_WRONG_SYMBOL],
    #less state
        [less_tk, less_tk, less_tk, less_tk, less_tk, less_tk, less_tk, less_tk, different_tk, lessOrEqual_tk, less_tk, less_tk, less_tk, less_tk, less_tk, less_tk, less_tk,
         less_tk, less_tk, less_tk, less_tk, less_tk, less_tk, ERROR_WRONG_SYMBOL],
    #greater state
        [greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greaterOrEqual_tk, greater_tk, greater_tk, greater_tk,
         greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, greater_tk, ERROR_WRONG_SYMBOL],
    #assign state
        [colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, assign_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk,
         colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, colon_tk, ERROR_WRONG_SYMBOL],
    #comment state
        [comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,
         comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, start_state, comment_state, comment_state,
         ERROR_COMMENTS_WITH_EOF, comment_state]

]

line = 1

def lex():
    global line
    word = ''
    current = start_state

    linecounter = line
    resultLex = []
    char_tk = 0
    while (current >= 0 and current <= 6):
        char = file.read(1)

        if(char == ' ' or char == '\t'):
            char_tk = space
        elif(char in alphabito):
            char_tk  = letters
        elif(char in noumera):
            char_tk = numbers
        elif(char == '+'):
            char_tk = plus
        elif(char == '-'):
            char_tk = minus
        elif(char == '*'):
            char_tk = multi
        elif(char == '/'):
            char_tk = div
        elif(char == '<'):
            char_tk = less
        elif(char == '>'):
            char_tk = greater
        elif(char == '='):
            char_tk = equal
        elif(char == '\n'):
            linecounter = linecounter + 1
            char_tk = new_line
        elif(char == ';'):
            char_tk = semicolon
        elif(char == ','):
            char_tk = coma
        elif(char == ':'):
            char_tk = colon
        elif(char == '('):
            char_tk = left_parenthesis
        elif(char == ')'):
            char_tk = right_parenthesis
        elif(char == '['):
            char_tk = left_bracket
        elif(char == ']'):
            char_tk = right_bracket
        elif(char == '{'):
            char_tk = left_comment
        elif(char == '}'):
            char_tk = right_comment
        elif(char == '%'):
            char_tk = modu
        elif(char == '_'):
            char_tk = underscore
        elif(char == ''):
            char_tk = EOF
        else:
            char_tk = wrong_symbol

        #print("Trexousa katastas", current)
        #print("Vlepo xaraktira", char)

        current = states_array[current][char_tk]

        #print("nea katastasi", current)
        #input("Press enter to continue")

        if(len(word)< 30):
            if(current != start_state and current != comment_state):
                word += char
        else:
            current = ERROR_EXCEDEED_LIMIT_OF_CHARACTERS
        #print(word)

    if(current == identifier_tk or current == number_tk or current == less_tk or current == greater_tk or current == colon):
        if(char == '\n'):
           linecounter -= 1
        file.seek(file.tell()-1,0)
        word = word[:-1]


    if(current == identifier_tk):
        if(word == 'πρόγραμμα'):
            current = program_tk
        elif(word == 'δήλωση'):
            current = declare_tk
        elif(word == 'εάν'):
            current = if_tk
        elif(word == 'τότε'):
            current = then_tk
        elif(word == 'αλλιώς'):
            current = else_tk
        elif(word == 'εάν_τέλος'):
            current = end_if_tk
        elif(word == 'επανάλαβε'):
            current = repeat_tk
        elif(word == 'μέχρι'):
            current = until_tk
        elif(word == 'όσο'):
            current = while_tk
        elif(word == 'όσο_τέλος'):
            current = end_while_tk
        elif(word == 'για'):
            current = for_tk
        elif(word == 'έως'):
            current = to_tk
        elif(word == 'με_βήμα'):
            current = with_step_tk
        elif(word == 'για_τέλος'):
            current = end_for_tk
        elif(word == 'διάβασε'):
            current = read_tk
        elif(word == 'γράψε'):
            current = write_tk
        elif(word == 'συνάρτηση'):
            current = function_tk
        elif(word == 'διαδικασία'):
            current = procedure_tk
        elif(word == 'διαπροσωπεία'):
            current = interface_tk
        elif(word == 'είσοδος'):
            current = input_tk
        elif(word == 'έξοδος'):
            current = output_tk
        elif(word == 'αρχή_συνάρτησης'):
            current = begin_function_tk
        elif(word == 'τέλος_συνάρτησης'):
            current = end_function_tk
        elif(word == 'αρχή_διαδικασίας'):
            current = begin_procedure_tk
        elif(word == 'τέλος_διαδικασίας'):
            current = end_procedure_tk
        elif(word == 'αρχή_προγράμματος'):
            current = begin_program_tk
        elif(word == 'τέλος_προγράμματος'):
            current = end_program_tk
        elif(word == 'ή'):
            current = or_tk
        elif(word == 'και'):
            current = and_tk
        elif(word == 'όχι'):
            current = not_tk
        elif(word == 'εκτέλεσε'):
            current = execute_tk

    if (current == ERROR_WRONG_SYMBOL):
        print("ERROR: Έχουμε λαθος συμβολο")
    elif (current == ERROR_NUMBER_LETTER):
        print("ERROR: Ακολουθει γραμμα μετα απο ψηφιο")
    elif (current == ERROR_COMMENTS_WITH_EOF):
        print("ERROR: Τα σχολια ανοιξαν αλλα δεν εκλεισαν πριν το τελος του αρχειου")
    elif (current == ERROR_EXCEDEED_LIMIT_OF_CHARACTERS):
        print("ERROR: Η λεξη εχει πανω απο 30 χαρακτηρες")
    elif (current == ERROR_RIGHT_COMMENT_ALONE):
        print("ERROR: Υπαρχει ενα } μονο του")
    elif (current == ERROR_UNDERSCORE_ALONE):
        print("ERROR: Υπαρχει ενα _ μονο του")

    resultLex.append(current)
    resultLex.append(word)
    resultLex.append(linecounter)
    line = linecounter

    return resultLex

'''
while(1):
    lexres = lex()
    if(lexres[0] == EOF_tk):
        break
    print(lexres)
'''
class Argument():
    def __init__(self):
        self.name = ''
        self.type = 'Int'
        self.parMode = ''

class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.variable = self.Variable()
        self.subprogram = self.SubProgram()
        self.parameter = self.Parameter()
        self.tempVar = self.TempVar()

    class Variable:
        def __init__(self):
            self.type = 'Int'
            self.offset = 0
    class SubProgram:
        def __init__(self):
            self.type = ''
            self.startQuad = 0
            self.frameLength = 0
            self.argumentList = []
    class Parameter:
        def __init__(self):
            self.mode = ''
            self.offset = 0
    class TempVar:
        def __init__(self):
            self.type = 'Int'
            self.offset = 0
class Scope():
    def __init__(self):
        self.name = ''
        self.entityList = []
        self.nestingLevel = 0
scopeList = []

def new_argument(object):
    global scopeList

    scopeList[-1].entityList[-1].subprogram.argumentList.append(object)
def new_entity(object):
    global scopeList

    scopeList[-1].entityList.append(object)
def new_scope(name):
    global scopeList

    nextScope = Scope()
    nextScope.name = name
    if(not scopeList):
        nextScope.nestingLevel = 0
    else:
        nextScope.nestingLevel = scopeList[-1].nestingLevel + 1
    scopeList.append(nextScope)
def delete_scope():
    global scopeList

    freeScope = scopeList.pop()
    del freeScope
def compute_offset():
    global scopeList

    counter = 0
    if(scopeList[-1].entityList is not []):
        for ent in (scopeList[-1].entityList):
            if(ent.type == 'VAR' or ent.type == 'TEMP' or ent.type == 'PARAM'):
                counter += 1
    offset = 12+(counter*4)

    return offset
def compute_startQuad():
    global scopeList

    scopeList[-2].entityList[-1].subprogram.startQuad = nextQuad()
def compute_framelength():
    global scopeList

    scopeList[-2].entityList[-1].subprogram.frameLength = compute_offset()
def add_parameters():
    global scopeList

    for arg in scopeList[-2].entityList[-1].subprogram.argumentList:
        ent = Entity()
        ent.name = arg.name
        ent.type = 'PARAM'
        ent.parameter.mode = arg.parMode
        ent.parameter.offset = compute_offset()
        new_entity(ent)
def print_Symbol_table():
    global scopeList
    global symFile

    symFile.write("###########################################################")
    symFile.write('\n')

    for sco in reversed(scopeList):
        symFile.write("SCOPE: "+"name:"+sco.name+" nestingLevel:"+str(sco.nestingLevel))
        symFile.write('\n\tENTITIES:\n')
        for ent in sco.entityList:
            if(ent.type == 'VAR'):
                symFile.write('\tENTITY: '+' name:'+ent.name+'\t type:'+ent.type+'\t variable-type:'+ent.tempVar.type+'\t offset:'+str(ent.variable.offset))
            elif(ent.type == 'TEMP'):
                symFile.write("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t temp-type:"+ent.tempVar.type+"\t offset:"+str(ent.tempVar.offset))
            elif(ent.type == 'SUBPR'):
                symFile.write("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t subprogram-type:"+ent.subprogram.type+"\t startQuad:"+str(ent.subprogram.startQuad)+"\t frameLength:"+str(ent.subprogram.frameLength))
                symFile.write("\t\tARGUMENTS:")
            elif(ent.type == 'PARAM'):
                symFile.write("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t mode:"+ent.parameter.mode+"\t offset:"+str(ent.parameter.offset))
            symFile.write('\n')
        symFile.write('\n\n\n')
    symFile.write('############################################################')
    symFile.write('\n\n\n\n\n')

def search_comb(n):
    global scopeList

    for sco in reversed(scopeList):
        for ent in sco.entityList:
            if(ent.name == n):
                return (sco, ent)
    print("In the symbols table there is no entity named: ", str(n))
    exit(-1)


ascFile = open('ascFile.asm', 'w')
ascFile.write('         \n\n\n')

def gnlvcode(name):
    global scopeList
    global ascFile

    ascFile.write('lw t0, -4(sp)\n')

    (sc1,ent1)=search_comb(name)

    myHel = scopeList[-1].nestingLevel - sc1.nestingLevel;
    myHel = myHel - 1

    for i in range(0, myHel):
        ascFile.write('lw t0, -3(t0)\n')

    if ent1.type=='VAR':
        x = ent1.variable.offset
    elif ent1.type=='PARAM':
        x=ent1.variable.offset
    
    ascFile.write('addi t0, t0, -%d\n' % (x))


def loadver(v, r):
    global scopeList
    global ascFile

    if v.isdigit():
        ascFile.write('li t%d,%s\n' % (r,v))
    else:
        (sc1, ent1) = search_comb(v)

        if sc1.nestingLevel==0 and ent1.type=='VAR':
            ascFile.write('lw t%d, -%d(gp)\n' %(r,ent1.variable.offset))
        elif (sc1.nestingLevel == scopeList[-1].nestingLevel):
            if (ent1.type == 'VAR'):
                ascFile.write('lw t%d, -%d(sp)\n' % (r,ent1.variable.offset))
            elif ent1.type == 'TEMP':
                ascFile.write('lw t%d, -%d(sp)\n' % (r, ent1.tempVar.offset))
            elif ent1.type == 'PARAM' and ent1.parameter.mode=='REF':
                ascFile.write('lw t0, -%d(sp)\n' % (ent1.parameter.offset))
                ascFile.write('lw t%d, (t0)\n' % (r))
        elif (sc1.nestingLevel < scopeList[-1].nestingLevel):
            if ent1.type == 'VAR':
                gnlvcode(v)
                ascFile.write('lw t%d, (t0)\n' %(r))
            elif (ent1.type == 'PARAM' and ent1.parameter.mode == 'CV'):
                gnlvcode(v)
                ascFile.write('lw t%d, (t0)\n' % (r))
            elif ent1.type == 'PARAM' and ent1.parameter.mode == 'REF':
                gnlvcode(v)
                ascFile.write('lw t0, (t0)\n')
                ascFile.write('lw t%d, (t0)\n' %(r))
def storev(r,v):
    global scopeList                
    global ascFile

    (sc1, ent1) = search_comb(v)

    if (sc1.nestingLevel == 0 and ent1.type == 'VAR'):
        ascFile.write('sw t%d,-%d(gp)\n' % (r,ent1.variable.offset))
    elif(sc1.nestingLevel == scopeList[-1].nestingLevel):
        if ent1.type == 'VAR':
            ascFile.write('sw t%d, %d(sp)\n' % (r,ent1.variable.offset))
        elif ent1.type == 'TEMP':
            ascFile.write('sw t%d, -%d(sp)\n' % (r, ent1.temVar.offset))
        elif ent1.type == 'PARAM' and ent1.parameter.mode == 'CV':
            ascFile.write('sw t%d,%d(sp)\n' % (r,ent1.add.parameter.offset))
        elif ent1.type == 'PARAM' and ent1.parameter.mode == 'REF':
            ascFile.write('lw t0,-%d(sp)\n' % (ent1.parameter.offset))
            ascFile.write('sw t%d, (t0)\n' % (r))
    elif sc1.nestinglevel < scopeList[-1].nestingLevel:
        if ent1.type == 'VAR':
            gnlvcode(v)
            ascFile.write('sw t%d,(t0)\n' % (r))
        elif ent1.type == 'PARAM' and ent1.parameter.mode=='CV':
            gnlvcode(v)
            ascFile.write('sw t%d, (t0)\n' % (r))
        elif ent1.type == 'PARAM' and ent1.parameter.mode == 'REF':
            gnlvcode(v)
            ascFile.write('lw t0,(t0)\n')
            ascFile.write('sw t%d, (t0)\n' % (r))
        elif ent1.type == 'SUBR' and ent1.subprogram.type == 'Fucntion':
            ascFile.write('lw t0,-8(sp)\n')
            ascFile.write('sw t%d,(t0)\n' % (r))

def search_list_for_call(i):
    global quadLst
    start = i
    while start > i:
        if(quadLst[start][i] == 'call'):
            return str(quadLst[start][2])
        start = start + 1

series = 1

def final():
    global scopeList
    global quadLst, series
    global ascFile

    for i in range(len(quadLst)):
        ascFile.write('L' + str(quadLst[i][0]) + ': \n')
        if(quadLst[i][1] == 'jump'):
            ascFile.write('b L'+str(quadLst[i][4])+'\n')
        elif(quadLst[i][1] == '='):
            loadver(quadLst[i][2], 1)
            loadver(quadLst[i][3],2)
            ascFile.write('beq,t1,t1,L'+str(quadLst[i][4]+'\n'))
        elif(quadLst[i][1] == '<>'):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],1)
            ascFile.write('bne,t1,t2,L'+str(quadLst[i][4]+'\n'))
        elif(quadLst[i][1] == '>'):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile.write('bgt,t1,t2,L'+str(quadLst[i][4])+'\n')
        elif(quadLst[i][1] == '<'):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile.write('blt t1,t2,L'+str(quadLst[i][4])+'\n')
        elif(quadLst[i][1] == '>='):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile.write('bqe,t1,t2,L'+str(quadLst[i][4])+'\n')
        elif(quadLst[i][1] == '<='):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile('ble,t1,t2,L'+str(quadLst[i][4])+'\n')
        elif(quadLst[i][1] == ':='):
            loadver(quadLst[i][2],1)
            storev(1, quadLst[i][4])
        elif(quadLst[i][1] == '+'):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile.write('add,t1,t1,t2'+'\n')
            storev(1,quadLst[i][4])
        elif(quadLst[i][1] == '-'):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile.write('sub,t1,t1,t2 \n')
            storev(1,quadLst[i][4])
        elif(quadLst[i][1] == '*'):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile.write('mul,t1,t1,t2 \n')
            storev(1,quadLst[i][4])
        elif(quadLst[i][1] == '/'):
            loadver(quadLst[i][2],1)
            loadver(quadLst[i][3],2)
            ascFile.write('div,t1,t1,t2\n')
            storev(1,quadLst[i][4])
        elif(quadLst[i][1] == 'out'):
            loadver(quadLst[i][4])
            ascFile.write('mv a0 , t1 \n')
            ascFile.write('li a7,1 \n')
            ascFile.write('ecall \n')
        elif(quadLst[i][1]):
            ascFile.write('li a7,5 \n')
            ascFile.write('ecall \n')
            ascFile.write('mv t1,a0 \n')
            storev(1, quadLst[1][2])
        elif(quadLst[i][1]  == 'par'):
            if series == -1:
                name1 = search_list_for_call(i)
                (sc1, ent1) = search_comb(name1)
                ascFile.write('sw t0,-%d(fp)\n' % (12+4*series))
                series = 0
            if(quadLst[i][3] == 'CV'):
                loadver(quadLst[i][2], 0)
                ascFile.write('sw t0,-%d\n' % (ent1.temVar.offset))
                series += 1
            elif(quadLst[i][3] == 'RET'):
                (sc1, ent1) = search_comb(quadLst[i][2])
                ascFile.write('addi t0,sp,-%d\n' % (ent1.tempVar.offset))
                ascFile.write('sw t0,-8(fp)\n')
            elif(quadLst[i][3] == 'REF'):
                (sc1, ent1) == search_comb(quadLst[i][2])
                if sc1.nestingLevel == scopeList[-1].nestingLevel:
                    if ent1.type == 'VAR':
                        ascFile.write('addi t0,sp,-%d\n' % (ent1.variable.offset))
                        ascFile.write('sw t0,-%d(fp)\n' % (12+4*series))
                    elif ent1.type == 'PARAM' and ent1.parameter.mode == 'CV':
                        ascFile.write('addi t0,sp,-%d\n' % (ent1.parameter.offset))
                        ascFile.write('sw t0, -%d(fp)\n' % (12+4*series))
                    elif ent1.type == 'PARAM' and ent1.parameter.mode == 'REF':
                        ascFile.write('lw t0,-%d(sp)\n' % (ent1.parameter.offset))
                        ascFile.write('sw t0,-%d(fp)\n' % (12+4*series))
            elif (sc1.nestingLevel < scopeList[-1].nestingLevel):
                if ent1.type == 'PARAM' and etn1.parameter.mode == 'REF':
                    gnlvcode(quadLst[i][2])
                    ascFile.write('lw t0,(t0)\n')
                    ascFile.write('sw t0, -%d(fp)\n' % (12+4*series))
                else:
                    gnlvcode(quadLst[i][2])
                    ascFile.write('sw t0,-%d(fp)\n' % (12+4*series))
            series += 1
        elif(quadLst[i][1] == 'begin_block' and scopeList[-1].nestingLevel !=0):
            ascFile.write('sw ra,(sp)\n')
        elif (quadLst[i][1] == 'begin_block' and scopeList[-1].nestingLevel == 0):
            ascFile.seek(0, os.SEEK_SET)
            ascFile.write('j L%d\n' % (compute_offset()))
            ascFile.seek(0, os.SEEK_END)
            ascFile.write('addi sp,sp,%d\n' % (compute_offset()))
            ascFile.write('mv gp,sp\n')
        elif (quadLst[i][1] == 'end_block' and scopeList[-1].nestingLevel != 0):
            ascFile.write('lw ra, (sp)\n')
            ascFile.write('jr ra\n')
        elif (quadLst[i][1] == 'halt'):
            ascFile.write('li a0,0\n')
            ascFile.write('li a7,93\n')
            ascFile.write('ecall\n')
    quadLst = []






def syntax():
    global line
    global res

    def program():
        global line 
        global res

        if(res[0] == program_tk):
            res = lex()
            line = res[2]

            if(res[0] == identifier_tk):
                id = res[1]

                res = lex()
                line = res[2]

                programblock(id)
            
            else:
                print("Error: There is no name for the program", line)
                exit(-1)
        else:
            print("Error: There is not the keyword 'πρόγραμμα' at the start", line)
            exit(-1)
    
    def programblock(name):
        global line
        global res

        new_scope(name)

        declarations()

        subprograms()

        if(res[0] == begin_program_tk):
            res = lex()
            line = res[2]

            genQuad('begin_block', name, '_', '_')
            sequence()
            genQuad('halt', '_', '_', '_')
            genQuad('end_block', name, '_', '_')

            print_Symbol_table()
            final()
            delete_scope()

            if(res[0] == end_program_tk):
                res = lex()
                line = res[2]
            
            else:
                print("Error: There is not the keyword 'τέλος_προγράμματος' at the end", line)
                exit(-1)
        else:
            print("Error: There is not the keyword 'αρχή_πρόγραμματος' at the beginning.", line)
            exit(-1)
    
    def declarations():
        global line
        global res

        while(res[0] == declare_tk):
            res = lex()
            line = res[2]

            varlist(1)

    def varlist(flag):
        global line
        global res

        if(res[0] == identifier_tk):
            id = res[1]

            res = lex()
            line = res[2]

            if(flag == 1):
                ent = Entity()
                ent.type = 'VAR'
                ent.name = id
                ent.variable.offset = compute_offset()
                new_entity(ent)
            elif(flag == 2):
                arg = Argument()
                arg.name = id
                arg.parMode = ''
                new_argument(arg)
            elif(flag == 3):
                for arg in  scopeList[-1].entityList[-1].subprogram.argumentList:
                    if(arg.name == id):
                        arg.parMode = 'CV'
            elif(flag == 4):
                for arg in scopeList[-1].entityList[-1].subprogram.argumentList:
                    if(arg.name == id):
                        arg.parMode = 'REF'
            

            while(res[0] == coma_tk):
                res = lex()
                line = res[2]

                if(res[0] == identifier_tk):
                    id = res[1]

                    res = lex()
                    line = res[2]

                    if(flag == 1):
                        ent = Entity()
                        ent.type = 'VAR'
                        ent.name = id
                        ent.variable.offset = compute_offset()
                        new_entity(ent)
                    elif(flag == 2):
                        arg = Argument()
                        arg.name = id
                        arg.parMode = ''
                        new_argument(arg)
                    elif(flag == 3):
                        for arg in scopeList[-1].entityList[-1].subprogram.argumentList:
                            if(arg.name == id):
                                arg.parMode = 'CV'
                    elif(flag == 4):
                        for arg in scopeList[-1].entityList[-1].subprogram.argumentList:
                            if(arg.name == id):
                                arg.parMode = 'REF'

                
                else:  
                    print("Error: There is no identifier after the ,", line)
                    exit(-1)

        else:
            print("Error: There is no identifier in the beginning.", line)
            exit(-1)

    def subprograms():
        global line
        global res

        while(res[0] == function_tk or res[0] == procedure_tk):

            if(res[0] == function_tk):
                func()

            else:
                proc()

    def func():
        global line
        global res

        if(res[0] == function_tk):
            res = lex()
            line = res[2]

            if(res[0] == identifier_tk):
                id = res[1]

                res = lex()
                line = res[2]

                if(res[0] == left_parenthesis_tk):
                    res = lex()
                    line = res[2]

                    ent = Entity()
                    ent.type = 'SUBPR'
                    ent.name = id
                    ent.subprogram.type = 'Function'
                    new_entity(ent)

                    formalparlist()

                    if(res[0] == right_parenthesis_tk):
                        res = lex()
                        line = res[2]

                        funcblock(id)

                    else:
                        print("Error: There is no ) at the end of the function.", line)
                        exit(-1)

                else:
                    print("Error: There is no ( at the function.", line)
                    exit(-1)

            else:
                print("Error: There is no name for the function.", line)
                exit(-1)


    def proc():
        global line
        global res 

        if(res[0] == procedure_tk):
            res = lex()
            line = res[2]

            if(res[0] == identifier_tk):
                id = res[1]

                res = lex()
                line = res[2]

                if(res[0] == left_parenthesis_tk):
                    res = lex()
                    line = res[2]

                    ent = Entity()
                    ent.type = 'SUBPR'
                    ent.name = id
                    ent.subprogram.type = 'Procedure'
                    new_entity(ent)


                    formalparlist()

                    if(res[0] == right_parenthesis_tk):
                        res = lex()
                        line = res[2]

                        procblock(id)

                    else:
                        print("Error: There is no ) at the end.", line)
                        exit(-1)

                else:
                    print("Error: There is no ( at the beginning.", line)
                    exit(-1)

            else: 
                print("Error: There is no name for the procedure.", line)
                exit(-1)

    def formalparlist():
        global line
        global res

        if(res[0] == identifier_tk):
            varlist(2)
    
    def funcblock(name):
        global line
        global res

        if(res[0] == interface_tk):
            res = lex()
            line = res[2]

            funcinput()
            funcoutput()

            new_scope(name)
            add_parameters()

            declarations()
            subprograms()

            if(res[0] == begin_function_tk):
                res = lex()
                line = res[2]

                compute_startQuad()
                genQuad('begin_block', name, '_', '_')
                sequence()
                compute_framelength()
                genQuad('end_block', name, '_', '_')

                print_Symbol_table()
                final()
                delete_scope()

                if(res[0] == end_function_tk):
                    res = lex()
                    line = res[2]

                else:
                    print("Error: There is not the keyword 'τέλος_συνάρτησης'.", line)
                    exit(-1)

            else:
                print("Error: There is not the keyword 'αρχή_συνάρτησης'.", line)
                exit(-1)

        else:
            print("Error: There is not the keyword 'διαπροσωπεα'.", line)
            exit(-1)

    def procblock(name):
        global line
        global res

        if(res[0] == interface_tk):
            res = lex()
            line = res[2]

            funcinput()
            funcoutput()

            new_scope(name)
            add_parameters()

            declarations()
            subprograms()

            if(res[0] == begin_procedure_tk):
                res = lex()
                line = res[2]

                compute_startQuad()
                genQuad('begin_block', name, '_', '_')
                sequence()
                compute_framelength
                genQuad('end_block', name, '_', '_')

                print_Symbol_table()
                final()
                delete_scope()

                if(res[0] == end_procedure_tk):
                    res = lex()
                    line = res[2]

                else:
                    print("Error: There is not the keyword 'τέλος_συνάρτησης'.", line)
                    exit(-1)

            else:
                print("Error: There is not the keyword 'αρχή_συνάρτησης'.", line)
                exit(-1)

        else:
            print("Error: There is not the keyword 'διαπροσωπεα'.", line)
            exit(-1)

    def funcinput():
        global line
        global res

        if(res[0] == input_tk):
            res = lex()
            line = res[2]

            varlist(3)

    def funcoutput():
        global line
        global res

        if(res[0] == output_tk):
            res = lex()
            line = res[2]

            varlist(4)

    def sequence():
        global line
        global res

        statement()

        while(res[0] == semicolon_tk):
            res = lex()
            line = res[0]

            statement()
    
    def statement():
        global line
        global res

        if(res[0] == identifier_tk):
            assignment_stat()
        elif(res[0] == if_tk):
            if_stat()
        elif(res[0] == while_tk):
            while_stat()
        elif(res[0] == repeat_tk):
            do_stat()
        elif(res[0] == for_tk):
            for_stat()
        elif(res[0] == read_tk):
            input_stat()
        elif(res[0] == write_tk):
            print_stat()
        elif(res[0] == execute_tk):
            call_stat()
        else:
            print("Error: The command is not recognized.", line)
            exit(-1)

    def assignment_stat():
        global line
        global res

        if(res[0] == identifier_tk):
            id = res[1]

            res = lex()
            line = res[2]

            if(res[0] == assign_tk):
                res = lex()
                line = res[2]

                Eplace = expression()
                genQuad(':=', Eplace, '_', id)

            else:
                print("Error: There is no := after the variable.", line)
                exit(-1)

    def if_stat():
        global line
        global res

        if(res[0] == if_tk):
            res = lex()
            line = res[2]

            c =condition()
            backPatch(c[0], nextQuad())

            if(res[0] == then_tk):
                res = lex()
                line = res[2]

                sequence()

                ifLst = makeList(nextQuad())
                genQuad('jump', '_', '_', '_')
                backPatch(c[1], nextQuad())

                elsepart()

                backPatch(ifLst, nextQuad())

                if(res[0] == end_if_tk):
                    res = lex()
                    line = res[2]

                else:
                    print("Error: There is no 'εάν_τέλος' at the end of the if statement.", line)
                    exit(-1)
            
            else:
                print("Error: There is no 'τότε' after the if statement.", line)
                exit(-1)

    def elsepart():
        global line
        global res

        if(res[0] == else_tk):
            res = lex()
            line = res[2]

            sequence()
    
    def while_stat():
        global line
        global res

        if(res[0] == while_tk):
            res = lex()
            line = res[2]

            cQ = nextQuad()

            c = condition()

            backPatch(c[0], nextQuad())

            if(res[0] == repeat_tk):
                res = lex()
                line = res[2]

                sequence()

                genQuad('jump', '_', '_', cQ)
                backPatch(c[1], nextQuad())

                if(res[0] == end_while_tk):
                    res = lex()
                    line = res[2]

                else:
                    print("Error: There is no 'όσο_τέλος' at the end.", line)
                    exit(-1)

            else:
                print("Error: There is no 'επανάλαβε' after the while.", line)
                exit(-1)


    def do_stat():
        global line
        global res

        if(res[0] == repeat_tk):
            res = lex()
            line = res[2]

            cQ = nextQuad()

            sequence()
            
            if(res[0] == until_tk):
                res = lex()
                line = res[2]

                c = condition()

                backPatch(c[1], cQ)
                backPatch(c[0], nextQuad())

            else:
                print("Error: These is no 'μέχρι' at the end.", line)
                exit(-1)

    def for_stat():
        global line
        global res

        if(res[0] == for_tk):
            res = lex()
            line = res[2]

            if(res[0] == identifier_tk):
                id = res[1]

                res = lex()
                line = res[2]

                if(res[0] == assign_tk):
                    res = lex()
                    line = res[2]

                    Eplace1 = expression()
                    genQuad(':=', Eplace1, '_', id)

                    if(res[0] == to_tk):
                        res = lex()
                        line = res[2]

                        Eplace2 = expression()
                        
                        stp = step()

                        CQ = nextQuad()

                        L_ex_pos = makeList(nextQuad())
                        genQuad('>', stp, '0', '_')
                        L_ex_neg = makeList(nextQuad())
                        genQuad('<', stp, '0', '_')
                        L_ex_zero = makeList(nextQuad())
                        genQuad('=', stp, '0', '_')

                        backPatch(L_ex_pos, nextQuad())
                        L_ch_pos_out = makeList(nextQuad())
                        genQuad('>=', id, Eplace2, '_')
                        L_ch_pos_in = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')

                        backPatch(L_ex_neg, nextQuad())
                        L_ch_neg_out = makeList(nextQuad())
                        genQuad('<=', id, Eplace2, '_')
                        L_ch_neg_in = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')

                        backPatch(L_ex_zero, nextQuad())

                        if(res[0] == repeat_tk):
                            res = lex()
                            line = res[2]

                            backPatch(L_ch_pos_in, nextQuad())
                            backPatch(L_ch_neg_in, nextQuad())

                            sequence()

                            genQuad('+', id, stp, id)
                            genQuad('jump', '_', '_', CQ)

                            backPatch(L_ch_pos_out, nextQuad())
                            backPatch(L_ch_neg_out, nextQuad())

                            if(res[0] == end_for_tk):
                                res = lex()
                                line = res[2]

                            else:
                                print("Error: There is no 'για_τέλος' at the end. ", line)
                                exit(-1)

                        else:
                            print("Error: There is no 'επανάλαβε' at the end. ", line)
                            exit(-1)
                    else:
                        print("Error: There is no 'έως' after the for statement. ", line)
                        exit(-1)
                else:
                    print("Error: There is no := . ", line)
                    exit(-1)
            else:
                print("Error: There is no variable after the for statement. ", line)
                exit(-1)


    def step():
        global line
        global res

        if(res[0] == with_step_tk):
            res = lex()
            line = res[2]

            Eplace3 = expression()
            return Eplace3

        else:
            return '1'
    

    def print_stat():
        global line
        global res

        if(res[0] == write_tk):
            res = lex()
            line = res[2]

            Eplace = expression()
            genQuad('out', Eplace, '_', '_')

    def input_stat():
        global line
        global res

        if(res[0] == read_tk):
            res = lex()
            line = res[2]

            if(res[0] == identifier_tk):
                id = res[1]

                res = lex()
                line = res[2]

                genQuad('inp', id, '_', '_')

            else:
                print("Error: There is no variable after 'διάβασε'. ", line)
                exit(-1)

    def call_stat():
        global line
        global res

        if(res[0] == execute_tk):
            res = lex()
            line = res[2]

            if(res[0] == identifier_tk):
                idName = res[1]

                res = lex()
                line = res[2]

                idtail(idName, 0)
                genQuad('call', idName, '_', '_')

            else:
                print("Error: There is no identifier after 'εκτέλεσε'. ", line)
                exit(-1)

    def idtail(name, called):
        global line
        global res
        if(res[0] == left_parenthesis_tk):
            actualpars()

            if(called == 1):
                w = newTemp()
                genQuad('par', w, 'RET', '_')
                genQuad('call', name, '_', '_')
                return w
            else:
                return name
            
    def actualpars():
        global line
        global res

        if(res[0] == left_parenthesis_tk):
            res = lex()
            line = res[2]

            actualparlist()

            if(res[0] == right_parenthesis_tk):
                res = lex()
                line = res[2]

            else:
                print("Error: There is no ')' at the end. ", line)
                exit(-1)

    def actualparlist():
        global line
        global res

        actualparitem()

        while(res[0] == coma_tk):
            res = lex()
            line = res[2]

            actualparitem()

    def actualparitem():
        global line
        global res

        if(res[0] == modu_tk):
            res = lex()
            line = res[2]

            if(res[0] == identifier_tk):
                name = res[1]

                res = lex()
                line = res[2]

                genQuad('par', name, 'REF', '_')

            else:
                print("Error: There is no identifier. ", line)
                exit(-1)

        else:
            
            thExpre = expression()
            genQuad('par', thExpre, 'CV', '_')

    def condition():
        global line
        global res

        BT1 = boolterm()

        trueCon = BT1[0]
        falseCon = BT1[1]


        while(res[0] == or_tk):
            res = lex()
            line = res[2]

            backPatch(falseCon,nextQuad())

            BT2 = boolterm()
            trueCon = merge(trueCon,BT2[0])
            falseCon = BT2[1]
        return trueCon,falseCon

    def boolterm():
        global line
        global res

        BF1 = boolfactor()

        BTtrue = BF1[0] #list1
        BTfalse = BF1[1] #list2


        while(res[0] == and_tk):
            res = lex()
            line = res[2]

            backPatch(BTtrue,nextQuad()) #one quad if it's true

            BF2 = boolfactor()

            BTfalse = merge(BTfalse,BF2[1]) #jump quad
            BTtrue = BF2[0]


           # boolfactor()
        return BTtrue , BTfalse

    def boolfactor():
        global line
        global res

        if(res[0] == not_tk):
            res = lex()
            line = res[2]

            if(res[0] == left_bracket_tk):
                res = lex()
                line = res[2]

                con = condition()

                BFtrue = con[1]
                BFfalse = con[0]


                if(res[0] == right_bracket_tk):
                    res = lex()
                    line = res[2]

                else:
                    print("Error: There is no ']' at the end. ", line)
                    exit(-1)
            else:
                print("Error: There is no '[' at the start. ", line)
                exit(-1)
            
        elif(res[0] == left_bracket_tk):
            res = lex()
            line = res[2]

            con = condition()

            BFtrue = con[0]
            BFfalse = con[1]

            if(res[0] == right_bracket_tk):
                res = lex()
                line = res[2]

            else:
                print("Error: There is no ']' at the end. ", line)
                exit(-1)

        else:

           Eplace1 = expression()

           relop =  relational_oper()

           Eplace2 =  expression()
           BFtrue = makeList(nextQuad())
           genQuad(relop,Eplace1,Eplace2,'_')
           BFfalse=makeList(nextQuad())
           genQuad('jump', '_', '_', '_')
        return BFtrue,BFfalse

    def expression():
        global line
        global res

        optional_sign()

        T1place = term()

        while(res[0] == plus_tk or res[0] == minus_tk):
            plusOrMinus = add_oper()

            T2place = term()
            w = newTemp()
            genQuad(plusOrMinus, T1place, T2place, w)
            #res = lex()
            #line = res[2]

            #add_oper()

            T1place = w

        Eplace = T1place
        return Eplace
            
    
    def term():
        global line
        global res

        F1place = factor()

        while(res[0] == multi_tk or res[0] == div_tk):
            mulOrDiv = mul_oper()
            
            F2place = factor()
            w = newTemp()
            genQuad(mulOrDiv, F1place, F2place, w)
            F1place = w
            #res = lex()
            #line = res[2]

            #mul_oper()

            #factor()

        Tplace = F1place
        return Tplace
    
    def factor():
        global line 
        global res 

        if(res[0] == number_tk):
            val = res[1]
            res = lex()
            line = res[2]
            return val
        elif(res[0] == left_parenthesis_tk):
            
            res = lex()
            line = res[2]

            val = expression()

            if(res[0] == right_parenthesis_tk):
                res = lex()
                line = res[2]
                return val

            else:
                print("Error: There is no ')' at the end. ", line)
                exit(-1)
        elif(res[0] == identifier_tk):
            #print(res[1])
            val = res[1]
            res = lex()
            line = res[2]
            #print (res[0])
            #print("I'm here.")
            idtail(val, 1)
            return val
        else:
            print("Error: There is no variable or constant or expression. ", line)
            exit(-1)

    def relational_oper():
        global line
        global res

        if(res[0] == equal_tk):
            relatOp = res[1]

            res = lex()
            line = res[2]

        elif(res[0] == lessOrEqual_tk):
            relatOp = res[1]

            res = lex()
            line = res[2]\

        elif(res[0] == greaterOrEqual_tk):
            relatOp = res[1]

            res = lex()
            line = res[2]

        elif(res[0] == different_tk):
            relatOp = res[1]

            res = lex()
            line = res[2]

        elif(res[0] == less_tk):
            relatOp = res[1]

            res = lex()
            line = res[2]

        elif(res[0] == greater_tk):
            relatOp = res[1]

            res = lex()
            line = res[2]
        else:
            print("Error: There is no relational operator. ", line)
            exit(-1)
        return relatOp
    
    def add_oper():
        global line 
        global res

        if(res[0] == plus_tk):
            res = lex()
            line = res[2]
            return '+'
        elif(res[0] == minus_tk):
            res = lex()
            line = res[2]
            return '-'
    
    def mul_oper():
        global line
        global res

        if(res[0] == multi_tk):
            res = lex()
            line = res[2]
            return '*'
        elif(res[0] == div_tk):
            res = lex()
            line = res[2]
            return '/'
    
    def optional_sign():
        global line
        global res

        if(res[0] == plus_tk or res[0] == minus_tk):
            
            add_oper()
    
    res = lex()
    line = res[2]
    program()


################endiamesos kodikas1#############################################
global quadLst 
quadLst = []
counter =1 

def nextQuad():
    global counter
    return counter
quadLstFinal = []
def genQuad(op,x,y,z):
    global counter
    global quadLst
    global quadLstFinal

    quads = []
    quads = [nextQuad()] 
    quads += [op] + [x] + [y] + [z]

    counter += 1
    quadLst += [quads]
    quadLstFinal += [list]
    return quads

temp = 1
def newTemp():
    global temp

    lst = []
    lst.append('T$')
    lst.append(str(temp))
    tempVar = "".join(lst)
    temp += 1

    ent = Entity()
    ent.type = 'TEMP'
    ent.name = tempVar
    ent.tempVar.offset = compute_offset()
    new_entity(ent)
    
    return tempVar

def emptyList():
    pointerLst =[]

    return pointerLst


def makeList(x):
    xLst = [x]

    return xLst

def merge(list1,list2):
    lst = []
    lst += list1 + list2
    
    return lst

def backPatch(list,z):
    global quadLst

    for i in range(len(list)):
         for j in range(len(quadLst)):
                if(list[i] == quadLst[j][0] and quadLst[j][4] == '_'):
                    quadLst[j][4] = z
                    break
    return
'''
     for num in list:
         for quad in quadLst: 
             if num == quad[0]:
                 quad[4] = z
                 break
'''

def intCode(intF):
    for i in range(len(quadLst)):
        qd = quadLst[i]
        intF.write(str(qd[0]))
        intF.write(": ")
        intF.write(str(qd[1]))
        intF.write(" ")
        intF.write(str(qd[2]))
        intF.write(" ")
        intF.write(str(qd[3]))
        intF.write(" ")
        intF.write(str(qd[4]))
        intF.write("\n")

intFile = open('intFile2.int', 'w')
symFile = open('symFile.sym', 'w')
syntax()

print("OK")

intCode(intFile)

symFile.close()
intFile.close()


'''    
def print_Quads():
    for i in range(len(quadLst)):
        print(str(quadLst[i][0])+" "+str(quadLst[i][1])+" "+str(quadLst[i][2])+" "+str(quadLst[i][3])+" "+str(quadLst[i][4]))

print_Quads()                        
'''        
        
