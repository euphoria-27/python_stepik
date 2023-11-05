eng_list = [chr(i) for i in range(ord('a'), ord('a') + 26)]
msg = input()
split_msg = msg.lower().split()


for index,value in enumerate(split_msg):
    counter = 0
    posi = index
    cur_el = value
    for c in cur_el:
        if c in eng_list:
            counter += 1
        
    for index, value in enumerate(cur_el):
        if value in eng_list: 
            letter = eng_list[(eng_list.index(value) + counter) % 26]
            cur_el = cur_el[0:index] + letter + cur_el[index + 1:]
            
            
    split_msg[posi] = cur_el

cypher_msg = ' '.join(split_msg)
for index,value in enumerate(cypher_msg):
        if msg[index].isupper():
            cypher_msg = cypher_msg[0:index] + value.upper() + cypher_msg[index + 1:]

print(cypher_msg)
