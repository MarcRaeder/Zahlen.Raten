import random

minNumber = 1
maxNumber = 100


def compareDistance(distanceGuessToNumber, distanceLastGuessToNumber, number):

    if distanceGuessToNumber > distanceLastGuessToNumber:
        print("kälter")
    elif distanceGuessToNumber < distanceLastGuessToNumber:
        print("wärmer")


def game():

    number = random.randint(1, 100)
    tries = 0

    print("Moinsen! Wie lautet dein Name?")

    name = str(input())

    print(name, "denk dir eine Zahl zwischen 1 und 100 aus :)")

    while True:

        try:
            currentGuess = int(input())
        except ValueError:
            print("Nur Zahlen sind erlaubt")
            continue

        guessInGame = currentGuess < minNumber or currentGuess > maxNumber
        distanceGuessToNumber = abs(currentGuess - number)
        firstTryColdStatement = distanceGuessToNumber > 10 and tries == 0 and currentGuess != number
        firstTryWarmStatement = distanceGuessToNumber < 10 and tries == 0 and currentGuess != number

        if guessInGame:
            print("Bitte gebe nur eine Zahl zwischen 1 und 20 ein!")
        else:
            if firstTryColdStatement:
                print("Kalt")
                tries += 1
                lastGuess = currentGuess
            elif firstTryWarmStatement:
                print("Warm")
                tries += 1
                lastGuess = currentGuess
            elif currentGuess < number:
                print("Deine Zahl ist zu niedrig. Versuch es erneut!")
                tries += 1
                distanceLastGuessToNumber = abs(lastGuess - number)
                compareDistance(distanceGuessToNumber,
                                distanceLastGuessToNumber, number)
                lastGuess = currentGuess
            elif currentGuess > number:
                print("Deine Zahl ist zu hoch. Versuch es erneut!")
                tries += 1
                distanceLastGuessToNumber = abs(lastGuess - number)
                compareDistance(distanceGuessToNumber,
                                distanceLastGuessToNumber, number)
                lastGuess = currentGuess
            elif currentGuess == number:
                print("Das war richtig. Nice! Du hast", tries, "Versuche gebraucht.\n\
                    Möchtest du nochmal spielen? Dann gebe 'JA' ein.\n\
                    Falls nicht dann gib irgendwas anderes ein.")
                break


game()

while True:

    decision = str(input())

    if decision.upper() == "JA":
        tries = 0
        game()
    else:
        print("Auf Wiedersehen")
        break
