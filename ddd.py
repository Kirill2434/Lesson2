a = "да"
b = "нет"
j = "Соня"

what = True

while what:
    guess = str(input("Димас девственник?"))

    if guess == a:
        print("хаххахах")
    elif guess == j:
        print("Вот кидок, сука, шлиете его нахуй посаны!!!")
    elif guess == b:
        print("да это пиздеж,ахахаха")

    else:
        print("А может это ты девственник?")
        what = False
else:
    print("Ну все пок")