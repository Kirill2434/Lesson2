def comparison (string1, string2):
    string1 = str(string1)
    string2 = str(string2)
    if string1 != str(string1) or string2 != str(string2):
        print (0)
    elif string1 == string2:
        print (1)
    elif len(string1) > len(string2):
        print (2)
    elif string1 != string2 and string2 == ('Learn'):
        print (3)
    else:
        print(4)

comparison (0, 1)