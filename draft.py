#Черновик
ask_list = {'Как твои дела?': 'хорошо', 'Сколько тебе лет?': '23', 'Ты работаешь?':'Да, много', 'У тебя много друзей?': 'Да, очень'}

def ask_user(what):
    
    what = True
    while what:
        ask = str(input())
        if ask == 'Как твои дела?':
            print(ask_list['Как твои дела?'])
            break
ask_user('sd')