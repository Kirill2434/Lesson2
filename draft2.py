ask_list = {'Как твои дела?': 'хорошо', 'Сколько тебе лет?': '23', 'Ты работаешь?':'Да, много', 'У тебя много друзей?': 'Да, очень'}

def ask_user(what):
    ask = str(input())
    what = True
    
    while what:
        
        if ask == 'Как твои дела?':
            print(ask_list['Как твои дела?'])
        
        if ask == 'Сколько тебе лет?':
            print(ask_list['Сколько тебе лет?'])
        
        if ask == 'Ты работаешь?':
            print(ask_list['Ты работаешь?'])
        
        if ask == 'У тебя много друзей?':
            print(ask_list['У тебя много друзей?'])
        

          
ask_user('sd')