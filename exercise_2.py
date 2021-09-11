def comparison(string1, string2):
    
    if isinstance(string1, str) and isinstance(string2, str):
        print (0)
    if string1 == string2:
        print (1)
    if len(str(string1)) > len(str(string2)):
        print (2)
    if str(string1) != str(string2) and string2 == ('learn'):
        print (3)
    else:
        return (int(string1), int(string2))

comparison ('0','learn')
comparison ('01', '2')
comparison ('0','0')