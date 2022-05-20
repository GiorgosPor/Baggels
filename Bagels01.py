import turtle
import random
import winsound
import time
winsound.PlaySound("108888__tim-kahn__begin",winsound.SND_ASYNC) # Ηχος εναρξης του παιχνιδιου

NUM_DIGITS = 3
MAX_GUESS = 10


def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        winsound.PlaySound("423265__datajunk__levelup-short-by-datajunk", winsound.SND_ASYNC) # Ηχος επιτυχιας του παικτη να βρει τον αριθμο

        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            winsound.PlaySound("72066__robinhood76__01027-applause-small-25", winsound.SND_ASYNC) #Ηχος αντιστοιχιας στο αποτελεσμα Fermi : One digit is correct in right position
            clues.append('Fermi')
        elif guess[i] in secretNum:
            winsound.PlaySound("582970__rocketpancake__mission-successful", winsound.SND_ASYNC) #Ηχος αντιστοιχιας στο αποτελεσμα Pico : One digit correct in wrong position
            clues.append('Pico')
    if len(clues) == 0:
        winsound.PlaySound("391422__audiortv__pigarro-bravo", winsound.SND_ASYNC) #Ηχος αντιστοιχιας στο αποτελεσμα Bagels : Κανενα ψηφιο δεν ειναι σωστο
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels       None of the digits is correct.')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' % (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:

            winsound.PlaySound("gameover", winsound.SND_ASYNC) # Ηχος τερματισμου , χωρις να βρεθει ο αριθμος απο τον παικτη

            print('You ran out of guesses. The answer was %s.' % (secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break










