secret = "rapunzel"
aerror = 6
gueses = []
correct = False

while not correct:
    for letter in secret:
        if letter. lower() in gueses:
            print(letter, end=" ")
        else: 
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors Left {aerror}, Next Guess: ")
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