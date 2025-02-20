import sys

alphabito =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω',
'Ά','Έ','Ή','Ί','Ό','Ύ','Ώ',
'α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω','ς',
'ά','έ','ή','ί','ό','ύ','ώ']

noumera =['0','1','2','3','4','5','6','7','8','9']

file = open("test.gre",'r',encoding='utf-8')

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

while(1):
    lexres = lex()
    if(lexres[0] == EOF_tk):
        break
    print(lexres)


