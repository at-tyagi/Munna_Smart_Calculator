from mathy import *
print(response[0])
while True:
    print()
    string=input(response[1]+"\n")
    print()
    for word in string.split(' '):
        if word.upper() in operations.keys():
            try:
                L=taking_num_from_text(string)
                r=operations[word.upper()](L[0],L[1])
                print(string+" is ",r)
            except:
                print("Something is wrong !!")
            break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
        else:
            print("Use some other name of operation !!\n")
