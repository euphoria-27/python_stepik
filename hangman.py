from random import *
word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']

def get_word():
    return choice(word_list).upper()
    
def display_hangman(tries):
    stages = [
'''
--------
|      |
|      O
|     \\|/
|      |
|     / \\
-
''',
'''
--------
|      |
|      O
|     \\|/
|      |
|     / 
-
''',
'''
--------
|      |
|      O
|     \\|/
|      |
|      
-
''',
'''
--------
|      |
|      O
|     \\|
|      |
|     
-
''',
'''
--------
|      |
|      O
|      |
|      |
|     
-
''',
'''
--------
|      |
|      O
|    
|      
|     
-
''',
'''
--------
|      |
|      
|    
|      
|     
-
'''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    print('Lets Play!')
    print(display_hangman(tries))
    print(word_completion)
    print(word)
    
    while(tries > 0):
        print('your letter?')
        letter = input()
        while(not letter.isalpha() or letter in guessed_letters):
            if not letter.isalpha():
                print('please give valid letter')
                letter = input()
            elif letter in guessed_letters:
                print('letter is guessed already, give another')
                letter = input()
            
        
    
        if letter.upper() in word:
            for index, value in enumerate(word_completion):
                if word[index] == letter.upper():
                    word_completion = word_completion[0:index] + letter.upper() + word_completion[index + 1:]
                    guessed_letters.append(letter)
        else:
            tries -= 1
        print(display_hangman(tries))
        print('guessed lettters:', *guessed_letters)
        print('tries left:', tries)
        print(word_completion)
        if(word_completion == word.upper()):
            break
    
    if(tries == 0):
        print('you lost')
        print('the word was', word)
        
    else:
        print('you won')
        print('the word was', word)
    
    print('wanna play again? y/n')
    if input() == 'y': play(get_word())
    else: print('goodbye')
        
play(get_word())
