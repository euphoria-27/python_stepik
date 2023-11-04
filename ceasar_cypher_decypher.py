rus_list = [chr(i) for i in range(ord('а'), ord('а') + 32)]
eng_list = [chr(i) for i in range(ord('a'), ord('a') + 26)]

def encode(lang, shift, message):
    copy_msg = message.lower()
    if(lang == 'r'):
        for index, value in enumerate(copy_msg):
            if value in rus_list: 
                letter = rus_list[(rus_list.index(value) + shift) % 32]
                copy_msg = copy_msg[0:index] + letter + copy_msg[index + 1:]
    elif(lang == 'e'):
        for index, value in enumerate(copy_msg):
            if value in eng_list: 
                letter = eng_list[(eng_list.index(value) + shift) % 26]
                copy_msg = copy_msg[0:index] + letter + copy_msg[index + 1:]
                
    for index,value in enumerate(copy_msg):
        if message[index].isupper():
            copy_msg = copy_msg[0:index] + value.upper() + copy_msg[index + 1:]
    
    return copy_msg
    
def decode(lang, shift, message):
    copy_msg = message.lower()
    if(lang == 'r'):
        for index, value in enumerate(copy_msg):
            if value in rus_list: 
                letter = rus_list[(rus_list.index(value) - shift) % 32]
                copy_msg = copy_msg[0:index] + letter + copy_msg[index + 1:]
    elif(lang == 'e'):
        for index, value in enumerate(copy_msg):
            if value in eng_list: 
                letter = eng_list[(eng_list.index(value) - shift) % 26]
                copy_msg = copy_msg[0:index] + letter + copy_msg[index + 1:]
                
    for index,value in enumerate(copy_msg):
        if message[index].isupper():
            copy_msg = copy_msg[0:index] + value.upper() + copy_msg[index + 1:]
    
    return copy_msg
    
def ceasar_cypher():
    
    print('rus/eng? r/e')
    lang_choice = input()
    while(lang_choice != 'r' and lang_choice != 'e'):
        print('please choose valid language! rus/eng? r/e')
        lang_choice = input()
    
    print('decypher/cypher? d/c')
    cypher_choice = input()
    while(cypher_choice != 'd' and cypher_choice != 'c'):
        print('please choose valid method! decypher/cypher? d/c')
        cypher_choice = input()
    
    print('choose shift')    
    shift_choice = input()
    while(not shift_choice.isnumeric()):
        print('please choose valid shift!')
        shift_choice = input()
        
    if lang_choice == 'r':
        shift_choice = int(shift_choice) % 32
    else:
        shift_choice = int(shift_choice) % 26
        
    print('enter your message')
    message = input()
    
    if(cypher_choice == 'c'):
        return encode(lang_choice, shift_choice, message)
    elif(cypher_choice == 'd'):
        return decode(lang_choice, shift_choice, message)
       
#for i in range(25):
 #   print(decode('e', i, 'Hawnj pk swhg xabkna ukq nqj.'), i)
print(ceasar_cypher())
