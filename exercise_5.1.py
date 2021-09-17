def hello_user(what):
    try:
        word = 'хорошо'
        what = True

        while what:
            user_say = str(input('Как твои дела? '))
            if user_say == word:
                print('До свидания)')
                
    except KeyboardInterrupt: 
        print('Пока!')
hello_user('sd')