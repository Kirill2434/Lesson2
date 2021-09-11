def hello_user(what):
    word = 'хорошо'
    what = True

    while what:
        user_say = str(input('Как твои дела? '))
        if user_say == word:
            print('До свидания)')
            break
hello_user('sd')