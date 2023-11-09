# ---------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("---------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C,or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)  # increasing value of correct_guesses
        question_num += 1  # increasing value of question_num
    display_score(correct_guesses, guesses)
# ---------------------------------


def check_answer(answer, guess):   # return functions
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0
# ---------------------------------


def display_score(correct_guesses, guesses):
    print("---------------------------------")
    print("results")
    print("---------------------------------")
    print("Answers: ", end="")  # let's use for loop
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("your score is: "+str(score)+"%")


# ---------------------------------
def play_again():
    response = input("Do you want to play again?(yes/no): ").upper()
    if response == "YES":
        return True
    else:
        return False


# ---------------------------------

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


new_game()

while play_again():
    new_game()
print("bye!")
