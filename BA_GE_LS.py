import turtle
import math
import random
import winsound
import time



# Create functions
def show_image(player_guess):

    # Game Setup
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Bagels")
    wn.setup(width=800, height=600)


    if player_guess == "start":
        wn.bgpic("game_start-gifmaker.gif")                               #Προσθηκη εικονας εναρξης παιχνιδιου
        winsound.PlaySound("108888__tim-kahn__begin",winsound.SND_ASYNC) #Προσθηκη ηχου εναρξης του παιχνιδιου

    elif player_guess == "end":
        wn.bgpic("Game-over-2gifmaker.gif")                                         #Προσθηκη εικονας ληξης παιχνιδιου
        winsound.PlaySound("123silencer1337__machinefail", winsound.SND_ASYNC)      #Προσθηκη ηχου ληξης παιχνιδιου
        
    elif player_guess == "Fermi":
        wn.bgpic("Vimpressivve.net-gifmaker.gif")                                         #Προσθηκη εικονας για Fermi
        winsound.PlaySound("72066__robinhood76__01027-applause-small-25",winsound.SND_ASYNC) #Προσθηκη ηχου για Fermi

    elif player_guess == "Pico":
        wn.bgpic("Goodwork-gifmaker.gif")                                                 #Προσθηκη εικονας για Pico
        winsound.PlaySound("582970__rocketpancake__mission-successful", winsound.SND_ASYNC)  #Προσθηκη ηχου για Pico
    else:
        wn.bgpic("TryHarder-gifmaker.gif")                                         #Προσθηκη ηχου για Bagels
        winsound.PlaySound("274867__alienxxx__gotta-do-better-than-that", winsound.SND_ASYNC)  #Προσθηκη ηχου για Bagels

    wn.update()      #Ενημερωση οθονης
    time.sleep(2)    #Delay οθονης
    wn.bye()         #Κλεισιμο οθονης


    

NUM_DIGITS = 3
MAX_GUESS = 10



def getSecretNum():
    #Επιστρεφει string τυχαιων αριθμων/ random και shuffle se μηκος λιστας NUM_DIGITS
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Επιστρεφει string Pico, Fermi, Bagels ως ενδειξη για τον χρηστη
    if guess == secretNum:
        show_image("end")
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            
            show_image("Fermi")
            
            clues.append('Fermi')
            
        elif guess[i] in secretNum:
            
            show_image("Pico")
            
            clues.append('Pico')
            
    if len(clues) == 0:
        
        show_image("Bagels")
        
        return 'Bagels'





    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):

    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

show_image("start")
# Εκκινηση Παιχνιδιου
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
            show_image("end")
            break
        if guessesTaken > MAX_GUESS:
            show_image("end")

            print('You ran out of guesses. The answer was %s.' % (secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
