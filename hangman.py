import random
def readWords():
    f = open("new 1.txt", "r")
    lines = f.readlines()
    return (lines)

def message(answer):
    for i in (answer):
        new_answer = random.choice(answer)
        return new_answer

def guess(answer,user_guess):
    word_guessed = []
    for i in (answer):
        word_guessed = word_guessed[i]

        if i in user_guess:
            word_guessed.append(i)
        else:
            word_guessed.append("_")
    return "".join(word_guessed)
def gameOver(answer,user_guess):

    count = 0
    while user_guess != answer or count != 7:
        count+=1
        return ("Try again")

    else:
        return True



def main():
    # Heading/welcome message
    words = readWords()
    f = message(words)
    x = guess(f,"b")
    print(x)

    chances = 7
    #user_answer = input("Lets play hangman, 7 guesses is what you get ", )
    #user_guess = guess(f,user_answer)
    #end = gameOver(f,user_guess)


    count =0
    """for i in range(7):
        print("Hello welcome to my hangman game")
        user_guess = input("Guess a letter but remember you only get 7 chances")
        f = message(words)
        x = guess(f, user_guess)
        print(x)
        new_x = x
        q = gameOver(new_x)
        print(q)
        message = message(x.split())

    while len(message) > x:
        message.remove(random.choice(list(message)))

    print(user_guess)"""

main()