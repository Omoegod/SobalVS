from functools import wraps
def requires_auth(name):
    @wraps(name)
    def decorated(*args, **kwargs):
        request = input('Введите ваше имя: ')
        if request == str:
            choice_second(2)
        return name(*args, **kwargs)
    return decorated

print('На какой вопрос в Новом Году вы бы хотели получить ответ? \n1) В чем смысл жизни? \n2) Самая главная цель создания Area 51? \n3) Где и как получить самые качественные знание и навыки на языке Python?')

answer = int(input('Что бы вы хотели узнать(1-3)? '))

def choice_first(answer):
    if answer == 1:
        print('Будда верил, что смысл жизни состоит в том, чтобы прожить ее в гармонии, отринув желания и ненависть. \nМухаммед сказал, что жизнь доверена людям Богом, с тем, чтобы посвятить ее пониманию Бога, и это ведет к вечной жизни. \nПлатон заметил, что «неисследованная жизнь не стоит того, чтобы ее жить».') 
    return "Надеюсь вы получили тот ответ который вы хотели"

@requires_auth
def choice_second(answer):
    if answer == 2:
        print('Главная цель создания Area 51 изучение советского кинематографа и поиск формулы создания таких гениальных фильмов, изучение НЛО это прикрытие')
    return "Надеюсь вы получили тот ответ который вы хотели"

def choice_third(answer):
    if answer == 3:
        print('На официальном сайте python.org в разделе документация, либо пройти курс в it-academy.by')
    return "Надеюсь вы получили тот ответ который вы хотели"

if answer == 1:
    choice_first(1)
elif answer == 2:
    choice_second(2)
elif answer == 3:
    choice_third(3)
else:
    pass        

