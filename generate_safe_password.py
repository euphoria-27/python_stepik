import random
digits = '0123456789';
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
exclude = 'il1Lo0O'

def check_if_num(n):
    if n.isnumeric():
        return n
    else:
        print('Please input a valid number')
        n = input()
        n = check_if_num(n)
        return n
        
def check_if_answer(t):
    if t.lower() in ['y', 'n']:
        return t
    else:
        print('Please input a valid answer')
        t = input()
        t = check_if_answer(t)
        return t


def generate_password(length, chars):
    return random.sample(chars, length)


def safe_pass():
    chars = ''
    print('how many passwords?')
    
    pw_count = check_if_num(input())
    for i in range(1, int(pw_count) + 1):
        
        print('password length?')
        pw_len = check_if_num(input())
        print('include digits? y/n')
        inc_dig = check_if_answer(input())
        print('include lowercase letters? y/n')
        inc_lw_letters = check_if_answer(input())
        print('include uppercase letters? y/n')
        inc_up_letters = check_if_answer(input())
        print('include punctuation? y/n')
        inc_pun = check_if_answer(input())
        print('exclude "il1Lo0O" ? y/n')
        exc_wtf = check_if_answer(input())
    
        if inc_dig == 'y': chars += digits
        if inc_lw_letters == 'y': chars += lowercase_letters
        if inc_up_letters == 'y': chars += uppercase_letters
        if inc_pun == 'y': chars += punctuation
        if exc_wtf == 'y':
            for c in chars:
                if c in exclude:
                    chars = chars.replace(c, "")
        print(f'Password {i}: {"".join(generate_password(int(pw_len), chars))}')
    return 
    
print(safe_pass())
