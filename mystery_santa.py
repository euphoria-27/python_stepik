from random import choice as c

def mystery_santa(n):
    participants = []
    for _ in range(n):
        participants.append(input())
    mystery_friends = participants.copy()

    for _ in range(len(participants)):

        if len(participants) == 2:
            if participants[0] == mystery_friends[0]:
                print(f'{participants[0]} - {mystery_friends[1]}')
                print(f'{participants[1]} - {mystery_friends[0]}')
            else:
                print(f'{participants[0]} - {mystery_friends[0]}')
                print(f'{participants[1]} - {mystery_friends[1]}')
            return
        santa = participants.pop()
        friend = c(mystery_friends)
        while(friend == santa):
            friend = c(mystery_friends)
        print(f'{santa} - {friend}')
        mystery_friends.remove(friend)
    return

mystery_santa(int(input()))
