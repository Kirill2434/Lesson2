a = "да"
b = "нет"
j = "Соня"

what = True

while what:
    guess = str(input("Димас "))

    if guess == a:
        print(")))")
    elif guess == j:
        print("Вот кидок!!!")
    elif guess == b:
        print("нет")

    else:
        print("А может это ты?")
        what = False
else:
    print("Ну все пок")