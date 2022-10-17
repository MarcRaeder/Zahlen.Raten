import random


def compareDistance(distanceGuessToNumber, distanceLastGuessToNumber, number):

    if distanceGuessToNumber > distanceLastGuessToNumber:
        print("kälter")
    elif distanceGuessToNumber < distanceLastGuessToNumber:
        print("wärmer")


def game():

    number = random.randint(1, 100)
    trys = 0
    min = 1
    max = 100

    print("Moinsen! Wie lautet dein Name?")

    name = str(input())

    print(name, "denk dir eine Zahl zwischen 1 und 100 aus :)")

    while True:

        try:
            currentGuess = int(input())
        except ValueError:
            print("Nur Zahlen sind erlaubt")
            continue

        guessInGame = currentGuess < min or currentGuess > max
        distanceGuessToNumber = abs(currentGuess - number)
        firstTryColdStatement = distanceGuessToNumber > 10 and trys == 0 and currentGuess != number
        firstTryWarmStatement = distanceGuessToNumber < 10 and trys == 0 and currentGuess != number

        if guessInGame:
            print("Bitte gebe nur eine Zahl zwischen 1 und 20 ein!")
        else:
            if firstTryColdStatement:
                print("Kalt")
                trys += 1
                lastGuess = currentGuess
            elif firstTryWarmStatement:
                print("Warm")
                trys += 1
                lastGuess = currentGuess
            elif currentGuess < number:
                print("Deine Zahl ist zu niedrig. Versuch es erneut!")
                trys += 1
                distanceLastGuessToNumber = abs(lastGuess - number)
                compareDistance(distanceGuessToNumber,
                                distanceLastGuessToNumber, number)
                lastGuess = currentGuess
            elif currentGuess > number:
                print("Deine Zahl ist zu hoch. Versuch es erneut!")
                trys += 1
                distanceLastGuessToNumber = abs(lastGuess - number)
                compareDistance(distanceGuessToNumber,
                                distanceLastGuessToNumber, number)
                lastGuess = currentGuess
            elif currentGuess == number:
                print("Das war richtig. Nice! Du hast",
                      trys, "Versuche gebraucht.\nMöchtest du nochmal spielen? Dann gebe 'JA' ein.\nFalls nicht dann gib irgendwas anderes ein.")

                decision = str(input())

                if decision.upper() == "JA":
                    trys = 0
                    game()
                else:
                    print("Auf Wiedersehen")
                    break
                break


game()
