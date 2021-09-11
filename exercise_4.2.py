ask_list = {'Как твои дела?': 'хорошо', 'Сколько тебе лет?': '23', 'Ты работаешь?':'Да, много', 'У тебя много друзей?': 'Да, очень'}

def ask_user(ask1):
    ask1 = True
    while ask1:
        ask = f'"Вопрос: " {str(input())}'
        if ask == 'Как твои дела?':
            print(ask_list['Как твои дела?'])
    
        elif ask == 'Сколько тебе лет?':
            print(ask_list['Сколько тебе лет?'])
        
        elif ask == 'Ты работаешь?':
            print(ask_list['Ты работаешь?'])
        
        elif ask == 'У тебя много друзей?':
            print(ask_list['У тебя много друзей?'])               
        else:
            print('Вопрос не распознан...')   
            ask1 = False      


ask_user('12')
