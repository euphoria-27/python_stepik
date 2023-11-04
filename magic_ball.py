import random
answers="Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Whats your name?')
username = input()
print('Hi,', username)

def magic_ball():
    while(True):
        print('Whats your question?')
        question = input()
        print(random.choice(answers))
        print('Wanna play again? y/n')
        text = input()
        if(text == 'y'):
            continue
        elif(text == 'n'):
            print('Возвращайся если возникнут вопросы!')
            break
            return
    
magic_ball()
