def studing (age):
    age = abs(age)

    if 3 <= age <= 7:
        print ('Должен учиться в детском саду')
    elif 7 <= age <= 18:
        print ('Должен учиться в школе')
    else:
        print ('Должен учиться в институте')
studing ()