hex_digits = [str(i) for i in range(10)] + [chr(i) for i in range(ord('A'), ord('A') + 6)]

def bin_to_dec(num):
    result = 0
    counter = 0
    while(num > 0):
        cur_digit = num % 10
        result += cur_digit * 2 ** counter
        counter += 1
        num //= 10
    return result
    
def hex_to_dec(num):
    result = 0
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        result += hex_digits.index(num[i]) * 16 ** counter
        counter += 1
    return result
#print(bin_to_dec(111111))

def dec_to_hex(num):
    result = ''
    while(num > 0):
        digit = num % 16
        if digit >= 10:
            result += hex_digits[digit]
        else:
            result += str(digit)
        num //= 16
    
    return result[::-1]

def dec_to_bin(num):
    result = ''
    while(num > 0):
        digit = num % 2
        result += str(digit)
        num //= 2
    
    return result[::-1]
#print(dec_to_bin(513))

def num_to_stuff(num):
    print(bin(num)[2:])
    print(oct(num)[2:])
    print(hex(num)[2:].upper())
    
num_to_stuff(10)
#print(hex_to_dec('1AF2'))
