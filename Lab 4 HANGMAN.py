import random
wins = 0
losses = 0

def updateText(secret, aerror):
    global wins, losses
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
        print(f"You nailed it! The secret word is {secret}!")
        wins += 1
    else:
        print(f"You lost! The correct secret word is {secret}!")
        losses += 1

def play():
    global wins, losses

    secretw = ["rapunzel", "cinderella", "belle", "mulan", "tiana"]

    while secretw:
        secret = random.choice(secretw)
        secretw.remove(secret)
        chances = 6
        updateText(secret, chances)
        print(f"Score: Wins - {wins}, Losses - {losses}")
        play_again = input("wanna to play again? (y/n): ")
        if play_again.lower() != "y":
            break
play()
