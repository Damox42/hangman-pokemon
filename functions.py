import connection
import random

db = connection.client['hangman_pokemon']
collection_names = db['names']

def selectWord():
    hiddenName = ""
    pokemon = db['names'].find()
    randomName = random.choice(list(pokemon))['name'].capitalize()
    print(f"{randomName}")
    for char in randomName:
        if char == " ":
            hiddenName += " "
        else:
            hiddenName += "_"
    return randomName, hiddenName

def guessLetter(guess, randomName, hiddenName, guessed_letters, attempts):
    if len(guess) != 1 or not guess.isalpha():
        print("Per favore inserisci una singola lettera.")
        return

    if guess in guessed_letters:
        print("Hai già usato questa lettera. Prova un'altra.")
        return hiddenName, attempts

    if guess in randomName.lower():
        newHiddenName = ""
        for i in range(len(randomName)):
            if randomName[i].lower() == guess:
                newHiddenName += randomName[i]
            else:
                newHiddenName += hiddenName[i]
        hiddenName = newHiddenName
        print("Lettera corretta!")
    else:
        attempts -= 1
        print("Lettera sbagliata!")
    
    return hiddenName, attempts
