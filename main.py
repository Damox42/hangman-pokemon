import functions

attempts = 10
randomName, hiddenName = functions.selectWord()
guessed_letters = ""

while attempts > 0 and "_" in hiddenName:
    print(f"Parola da Indovinare: {hiddenName}")
    print(f"Tentativi rimasti: {attempts}")
    guess = input("Indovina una lettera: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Per favore inserisci una singola lettera.")
        continue

    hiddenName, attempts = functions.guessLetter(guess, randomName, hiddenName, guessed_letters, attempts)
    guessed_letters += guess

if attempts == 0:
    print(f"Hai perso! La parola era: {randomName}")
else:
    print(f"Congratulazioni! Hai indovinato la parola: {randomName}")