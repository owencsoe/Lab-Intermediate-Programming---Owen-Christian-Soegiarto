def updateText(secret, aerror):
    gueses = []
    correct = False

    while not correct:
        for letter in secret:
            if letter. lower() in gueses:
                print(letter, end=" ")
            else: 
                print("_", end=" ")
        print("")

        guess = input(f"Chances left {aerror}, Next Guess: ")
        gueses.append (guess. lower ())
        if guess.lower() not in secret.lower():
            aerror -= 1
            if aerror == 0:
                break

        correct = True
        for letter in secret:
            if letter.lower () not in gueses:
                correct = False
    if correct:
        print(f"Correct! it was {secret}!")
    else:
        print(f"Wrong! It was {secret}!")
secretw = "rapunzel"
updateText(secretw, 6)