import random

def game():
    print("you are playing a game...")
    
    score = random.randint(1, 62)

    # Fetching the High score 
    with open("hiscore.txt") as f:
        hiscore = f.read()

        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score: {score}")

    if score > hiscore:
        # write this high score to the file 
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()