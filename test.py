import time


def start():
    print ("Naar welke functie wil je gaan?")
    antwoord = input()

    if antwoord == "1":
        functie1()
    
    if antwoord == "2":
        functie2()
    
    else:
        print ("Optie niet herkend. Probeer het opnieuw...")
        time.sleep(2)
        return start()

def functie1():
    print ("Dit is functie1")
    time.sleep(2)
    return start()

def functie2():
    print ("Dit is functie2")
    time.sleep(2)
    return start()

start()